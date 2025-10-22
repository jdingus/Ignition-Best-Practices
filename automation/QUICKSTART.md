# Quick Start Guide

Get up and running with automated content ingestion in 5 minutes!

## Prerequisites

- Python 3.7 or higher
- Anthropic API key ([Get one here](https://console.anthropic.com/))

## Setup (One-Time)

### Step 1: Install Dependencies

```bash
cd automation
pip install -r requirements.txt
```

### Step 2: Configure API Key

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Anthropic API key
# You can use any text editor:
nano .env
# or
vim .env
# or
code .env
```

Your `.env` file should look like:
```
ANTHROPIC_API_KEY=sk-ant-api03-xxxxxxxxxxxxx
```

## Usage

### Example 1: Preview Content (Dry Run)

Test the system without making any changes:

```bash
python ingest_content.py --dry-run "https://inductiveautomation.com/blog/your-article"
```

This will:
- Fetch the content
- Analyze it with AI
- Show you what would be added
- **NOT** modify any files

### Example 2: Ingest Content

Once you're happy with the preview, run it for real:

```bash
python ingest_content.py "https://inductiveautomation.com/blog/your-article"
```

### Example 3: Review and Commit

After ingestion, review the changes:

```bash
# See what changed
git diff

# If you're happy with the changes, commit them
git add sections/
git commit -m "Add best practices from IA blog post"
git push
```

## Complete Workflow Example

Here's a complete workflow for ingesting a blog post about troubleshooting CPU resources:

```bash
# 1. Navigate to automation directory
cd automation

# 2. Preview the ingestion (dry run)
python ingest_content.py --dry-run \
    "https://inductiveautomation.com/blog/troubleshooting-ignition-cpu"

# Output shows:
# ✓ Fetched 12543 characters
# ✓ Analysis complete
# Content Summary: Article discusses CPU performance optimization...
# Sections to update: gateway-configuration, testing-deployment
# Dry run: Would update 2 section file(s)

# 3. Looks good! Run it for real
python ingest_content.py \
    "https://inductiveautomation.com/blog/troubleshooting-ignition-cpu"

# 4. Review changes
cd ..
git diff sections/

# 5. Commit if satisfied
git add sections/
git commit -m "Add CPU troubleshooting best practices from IA blog"
git push
```

## Tips

- **Always use `--dry-run` first** to preview changes
- **Review with `git diff`** before committing
- **One URL at a time** for better control
- **Check the analysis** to ensure content is categorized correctly

## Troubleshooting

### Error: "ANTHROPIC_API_KEY must be set"

Make sure you created the `.env` file with your API key:

```bash
# Check if .env exists
ls -la .env

# If not, create it
cp .env.example .env
# Then edit and add your key
```

### Error: "Failed to fetch URL content"

- Verify the URL is accessible in a browser
- Check your internet connection
- Some sites may block automated requests

### Content Not Relevant

If the AI says "Content is not relevant to Ignition", the article might not be about Ignition SCADA. Try a different URL or manually add the content.

## Next Steps

- Read the full [README.md](README.md) for advanced usage
- Try processing multiple URLs with [example_batch.sh](example_batch.sh)
- Contribute improvements to the automation system!

## Getting Help

- Check the full documentation: [README.md](README.md)
- Review example scripts in the `automation/` directory
- Open an issue on GitHub if you encounter problems
