#!/usr/bin/env python3
"""
Automated Content Ingestion for Ignition Best Practices

This script processes URLs containing Ignition-related content and automatically
incorporates best practices into the repository.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional
import anthropic
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Repository sections mapping
SECTIONS = {
    "gateway-configuration": "sections/gateway-configuration.md",
    "perspective-views": "sections/perspective-views.md",
    "gateway-scripting": "sections/gateway-scripting.md",
    "tags": "sections/tags.md",
    "database-integration": "sections/database-integration.md",
    "testing-deployment": "sections/testing-deployment.md",
    "source-control": "sections/source-control.md",
    "reports": "sections/reports.md",
    "webdev": "sections/webdev.md",
    "alarms": "sections/alarms.md"
}


class ContentIngester:
    """Handles fetching, analyzing, and incorporating content from URLs."""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the content ingester with Claude API."""
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY must be set in environment or .env file")

        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.repo_root = Path(__file__).parent.parent

    def fetch_url_content(self, url: str) -> str:
        """Fetch and extract text content from a URL."""
        print(f"Fetching content from: {url}")

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Remove script and style elements
            for script in soup(["script", "style", "nav", "footer", "header"]):
                script.decompose()

            # Get text content
            text = soup.get_text()

            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)

            return text

        except Exception as e:
            raise Exception(f"Failed to fetch URL content: {str(e)}")

    def analyze_content(self, url: str, content: str) -> Dict:
        """Use Claude to analyze content and extract best practices."""
        print("Analyzing content with Claude AI...")

        sections_list = "\n".join([f"- {key}: {value}" for key, value in SECTIONS.items()])

        prompt = f"""You are analyzing content from this URL for an Ignition Best Practices repository:
URL: {url}

The repository has these sections:
{sections_list}

Here is the content to analyze:

{content[:8000]}  # Limit content to avoid token limits

Please analyze this content and provide a JSON response with the following structure:
{{
    "relevant": true/false,  // Is this relevant to Ignition SCADA platform?
    "sections": ["section-name1", "section-name2"],  // Which sections should this be added to?
    "best_practices": [
        {{
            "section": "section-name",
            "practice": "Brief best practice recommendation",
            "details": "More detailed explanation if needed"
        }}
    ],
    "external_links": [
        {{
            "section": "section-name",
            "title": "Link title/description",
            "url": "{url}"
        }}
    ],
    "summary": "Brief summary of the content and why it's relevant"
}}

Focus on extracting actionable best practices, tips, and recommendations. If the content is not relevant to Ignition SCADA, set relevant to false.

Return ONLY the JSON response, no additional text."""

        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=4096,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            response_text = message.content[0].text

            # Try to extract JSON from response
            try:
                analysis = json.loads(response_text)
            except json.JSONDecodeError:
                # Try to find JSON in the response
                import re
                json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                if json_match:
                    analysis = json.loads(json_match.group())
                else:
                    raise ValueError("Could not parse JSON from Claude response")

            return analysis

        except Exception as e:
            raise Exception(f"Failed to analyze content: {str(e)}")

    def update_sections(self, analysis: Dict, dry_run: bool = False) -> Dict[str, str]:
        """Update the appropriate section files with new content."""
        updates = {}

        if not analysis.get("relevant", False):
            print("Content is not relevant to Ignition. Skipping updates.")
            return updates

        print(f"\nContent Summary: {analysis.get('summary', 'N/A')}")
        print(f"Sections to update: {', '.join(analysis.get('sections', []))}")

        for practice in analysis.get("best_practices", []):
            section = practice.get("section")
            if section not in SECTIONS:
                print(f"Warning: Unknown section '{section}', skipping...")
                continue

            section_file = self.repo_root / SECTIONS[section]

            if not section_file.exists():
                print(f"Warning: Section file {section_file} does not exist, skipping...")
                continue

            # Read current content
            with open(section_file, 'r') as f:
                current_content = f.read()

            # Prepare the new practice text
            practice_text = f"- **{practice.get('practice', '')}**"
            if practice.get('details'):
                practice_text += f"\n  - {practice.get('details')}"

            # Find the "Tips and Recommendations" section and add the practice
            if "## Tips and Recommendations" in current_content:
                # Insert after the "Tips and Recommendations" header
                parts = current_content.split("## Tips and Recommendations")

                if len(parts) == 2:
                    # Find the next section or end
                    next_section_idx = parts[1].find("\n##")

                    if next_section_idx != -1:
                        before_next = parts[1][:next_section_idx]
                        after_next = parts[1][next_section_idx:]

                        # Add the new practice at the end of Tips section
                        new_content = (
                            parts[0] +
                            "## Tips and Recommendations" +
                            before_next.rstrip() +
                            "\n\n" + practice_text + "\n" +
                            after_next
                        )
                    else:
                        # No next section, add at the end
                        new_content = (
                            parts[0] +
                            "## Tips and Recommendations" +
                            parts[1].rstrip() +
                            "\n\n" + practice_text + "\n"
                        )

                    updates[str(section_file)] = new_content

        # Add external links
        for link in analysis.get("external_links", []):
            section = link.get("section")
            if section not in SECTIONS:
                continue

            section_file = self.repo_root / SECTIONS[section]

            if not section_file.exists():
                continue

            # Read current content (or get from updates)
            if str(section_file) in updates:
                current_content = updates[str(section_file)]
            else:
                with open(section_file, 'r') as f:
                    current_content = f.read()

            # Add link to "Links to More Information" section
            link_text = f"- [{link.get('title', 'Resource')}]({link.get('url', '')})"

            if "## Links to More Information" in current_content:
                parts = current_content.split("## Links to More Information")

                if len(parts) == 2:
                    # Find the next section
                    next_section_idx = parts[1].find("\n##")

                    if next_section_idx != -1:
                        before_next = parts[1][:next_section_idx]
                        after_next = parts[1][next_section_idx:]

                        new_content = (
                            parts[0] +
                            "## Links to More Information" +
                            before_next.rstrip() +
                            "\n" + link_text + "\n" +
                            after_next
                        )
                    else:
                        new_content = (
                            parts[0] +
                            "## Links to More Information" +
                            parts[1].rstrip() +
                            "\n" + link_text + "\n"
                        )

                    updates[str(section_file)] = new_content

        # Write updates if not dry run
        if not dry_run and updates:
            for file_path, content in updates.items():
                print(f"Updating: {file_path}")
                with open(file_path, 'w') as f:
                    f.write(content)
            print(f"\n✓ Updated {len(updates)} section file(s)")
        elif dry_run and updates:
            print(f"\nDry run: Would update {len(updates)} section file(s)")
            for file_path in updates.keys():
                print(f"  - {file_path}")

        return updates

    def ingest(self, url: str, dry_run: bool = False) -> Dict:
        """Main ingestion workflow."""
        print(f"\n{'='*60}")
        print(f"Ingesting content from URL")
        print(f"{'='*60}\n")

        # Step 1: Fetch content
        content = self.fetch_url_content(url)
        print(f"✓ Fetched {len(content)} characters\n")

        # Step 2: Analyze content
        analysis = self.analyze_content(url, content)
        print(f"✓ Analysis complete\n")

        # Step 3: Update sections
        updates = self.update_sections(analysis, dry_run=dry_run)

        return {
            "analysis": analysis,
            "updates": list(updates.keys())
        }


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Ingest Ignition best practices content from URLs"
    )
    parser.add_argument(
        "url",
        help="URL of the article/blog post to ingest"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Analyze content without making changes"
    )
    parser.add_argument(
        "--api-key",
        help="Anthropic API key (or set ANTHROPIC_API_KEY env var)"
    )
    parser.add_argument(
        "--output",
        help="Save analysis to JSON file"
    )

    args = parser.parse_args()

    try:
        ingester = ContentIngester(api_key=args.api_key)
        result = ingester.ingest(args.url, dry_run=args.dry_run)

        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"\nAnalysis saved to: {args.output}")

        print(f"\n{'='*60}")
        print("Ingestion complete!")
        print(f"{'='*60}\n")

    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
