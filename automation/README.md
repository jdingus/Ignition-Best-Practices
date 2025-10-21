# Automated Content Ingestion

This automation system allows you to automatically process and incorporate Ignition-related content from URLs (blog posts, articles, documentation) into the best practices repository.

## 🎉 Three Ways to Ingest Content

### Option 1: GitHub Issues (On The Go - FREE!)

**Perfect for mobile or when away from your computer!**

[Create an issue](../.github/ISSUE_TEMPLATE/ingest-content.md) with a URL, then process it later with Claude Code.

✅ Works from anywhere (mobile, tablet, desktop)
✅ No setup required
✅ No API key needed
✅ Process when you're ready

See [GITHUB_ISSUE_WORKFLOW.md](GITHUB_ISSUE_WORKFLOW.md) for details.

### Option 2: Claude Code Interactive (FREE - At Your Computer!)

**Uses your existing Claude Code subscription - no API key or extra costs!**

Simply run:
```bash
./automation/ingest_with_claude.sh "https://your-url-here.com"
```

Then follow the prompts to use Claude Code interactively. See [CLAUDE_CODE_WORKFLOW.md](CLAUDE_CODE_WORKFLOW.md) for details.

✅ No setup required
✅ No API key needed
✅ Uses your existing subscription
✅ Process unlimited URLs

### Option 3: API Script (Automated)

**For automation, CI/CD, and batch processing (requires API key)**

Best for:
- GitHub Actions automation
- Batch processing many URLs
- Scheduled/automated workflows
- Fully hands-off operation

Requires Anthropic API key (pay-per-token). See setup below.

---

## Features

- **Automated Content Extraction**: Fetches content from any URL
- **AI-Powered Analysis**: Uses Claude AI to analyze and categorize content
- **Smart Categorization**: Automatically determines which sections the content belongs to
- **Best Practice Extraction**: Identifies and extracts actionable best practices
- **Link Management**: Adds external resource links to appropriate sections
- **Dry Run Mode**: Preview changes before applying them

## Quick Start (Claude Code - FREE!)

**Just run the helper script and follow the prompts:**

```bash
./automation/ingest_with_claude.sh "https://inductiveautomation.com/blog/your-article"
```

For complete details, see [CLAUDE_CODE_WORKFLOW.md](CLAUDE_CODE_WORKFLOW.md)

---

# API Script Setup (Optional)

**Only needed if you want automated/batch processing. For manual use, stick with Claude Code above!**

## Setup

### 1. Install Dependencies

```bash
cd automation
pip install -r requirements.txt
```

### 2. Configure API Key

1. Get your Anthropic API key from [https://console.anthropic.com/](https://console.anthropic.com/)
2. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
3. Edit `.env` and add your API key:
   ```
   ANTHROPIC_API_KEY=your_actual_api_key_here
   ```

## Usage

### Basic Usage

Ingest content from a URL:

```bash
python ingest_content.py "https://example.com/ignition-blog-post"
```

### Dry Run (Preview Only)

Preview what changes would be made without modifying files:

```bash
python ingest_content.py --dry-run "https://example.com/ignition-blog-post"
```

### Save Analysis to File

Save the analysis results to a JSON file:

```bash
python ingest_content.py --output analysis.json "https://example.com/ignition-blog-post"
```

### Using API Key from Command Line

Instead of using a .env file, you can provide the API key directly:

```bash
python ingest_content.py --api-key "your_api_key" "https://example.com/ignition-blog-post"
```

## How It Works

1. **Fetch Content**: The script fetches the webpage and extracts the text content
2. **AI Analysis**: Claude AI analyzes the content to:
   - Determine if it's relevant to Ignition
   - Identify which sections it applies to
   - Extract best practices and recommendations
   - Identify useful external links
3. **Update Files**: The script updates the appropriate markdown files in the `sections/` directory
4. **Review**: Review the changes using `git diff` before committing

## Example Workflow

```bash
# 1. Run in dry-run mode to preview
python ingest_content.py --dry-run "https://inductiveautomation.com/blog/troubleshooting-cpu"

# 2. If it looks good, run for real
python ingest_content.py "https://inductiveautomation.com/blog/troubleshooting-cpu"

# 3. Review the changes
git diff

# 4. If satisfied, commit the changes
git add sections/
git commit -m "Add CPU troubleshooting best practices from IA blog"
git push
```

## Supported Content Types

The system works best with:
- Blog posts about Ignition
- Technical articles and tutorials
- Documentation pages
- Forum posts with best practices
- Case studies and implementation guides

## Repository Sections

The automation can add content to these sections:

- `gateway-configuration` - Gateway setup and configuration
- `perspective-views` - Perspective view development
- `gateway-scripting` - Gateway scripting best practices
- `tags` - Tag structure and organization
- `database-integration` - Database connectivity and queries
- `testing-deployment` - Testing and deployment workflows
- `source-control` - Version control practices
- `reports` - Report development
- `webdev` - Web Development Module
- `alarms` - Alarm notification pipelines

## Output Format

The script provides detailed output:

```
============================================================
Ingesting content from URL
============================================================

Fetching content from: https://example.com/article
✓ Fetched 15234 characters

Analyzing content with Claude AI...
✓ Analysis complete

Content Summary: Article discusses gateway performance optimization...
Sections to update: gateway-configuration, testing-deployment

Updating: sections/gateway-configuration.md
Updating: sections/testing-deployment.md

✓ Updated 2 section file(s)

============================================================
Ingestion complete!
============================================================
```

## Troubleshooting

### "ANTHROPIC_API_KEY must be set"

Make sure you've created a `.env` file with your API key, or pass it via `--api-key`.

### "Failed to fetch URL content"

- Check that the URL is accessible
- Some websites may block automated requests
- Try accessing the URL in a browser first

### "Content is not relevant to Ignition"

The AI determined the content isn't related to Ignition SCADA. You can:
- Try a different URL
- Manually add the content if you believe it's relevant

## Advanced Usage

### Batch Processing

Process multiple URLs:

```bash
#!/bin/bash
urls=(
    "https://example.com/article1"
    "https://example.com/article2"
    "https://example.com/article3"
)

for url in "${urls[@]}"; do
    echo "Processing: $url"
    python ingest_content.py "$url"
    sleep 2  # Rate limiting
done
```

### Integration with GitHub Actions

You can set up a GitHub Action to process URLs from issues or PR comments. See the example workflow in `.github/workflows/` (if available).

## Contributing

If you improve the automation system, please submit a pull request! Some ideas for enhancements:

- Support for PDF documents
- Video transcript processing
- Multi-language support
- Duplicate detection
- Automated PR creation

## License

This automation tool is part of the Ignition Best Practices repository and is licensed under the MIT License.
