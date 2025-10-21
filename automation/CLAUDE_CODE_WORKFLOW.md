# Using Claude Code for Content Ingestion (FREE!)

**No API key needed! Uses your existing Claude Code subscription.**

This guide shows you how to use your existing Claude Code subscription to ingest content - no additional costs for API tokens!

## Why Use This Approach?

- ✅ **FREE** - Uses your existing Claude Code subscription ($100/month you're already paying)
- ✅ **No API key required** - No additional Anthropic API setup
- ✅ **Interactive** - Review and approve changes as Claude works
- ✅ **Flexible** - Easy to adjust and refine on the fly

## Two Methods Available

### Method 1: Slash Command (Recommended)

This is the easiest way to ingest content with Claude Code.

#### Step 1: Open Claude Code in this repository

```bash
cd /path/to/Ignition-Best-Practices
claude
```

#### Step 2: Use the ingest-url command

In Claude Code, type:
```
/ingest-url
```

#### Step 3: Provide the URL

When Claude asks, paste your URL:
```
https://inductiveautomation.com/blog/your-article-here
```

#### Step 4: Claude will automatically:
- Fetch the content from the URL
- Analyze it for relevance to Ignition
- Determine which sections it applies to
- Extract best practices
- Update the appropriate markdown files
- Show you a summary of changes

#### Step 5: Review and commit

```bash
git diff                    # Review changes
git add sections/
git commit -m "Add content from blog post"
git push
```

### Method 2: Helper Script

We've created a helper script to make this even easier!

```bash
# Run the helper script with a URL
./automation/ingest_with_claude.sh "https://your-url-here.com"

# Or run it without a URL to be prompted
./automation/ingest_with_claude.sh
```

This script will:
- Show you the URL you're processing
- Give you step-by-step instructions
- Copy the URL to your clipboard
- Tell you exactly what to type in Claude Code

## Complete Example Workflow

Let's say you found this blog post: `https://inductiveautomation.com/blog/perspective-performance-tips`

### Using the Helper Script:

```bash
# Step 1: Run the helper
$ ./automation/ingest_with_claude.sh "https://inductiveautomation.com/blog/perspective-performance-tips"

╔════════════════════════════════════════════════════════════╗
║   Ignition Best Practices - Content Ingestion Helper      ║
║   Using Claude Code (No API Key Required!)                ║
╔════════════════════════════════════════════════════════════╗

URL to process: https://inductiveautomation.com/blog/perspective-performance-tips

═══════════════════════════════════════════════════════════
Next Steps:

1. Run Claude Code in this repository:
   claude

2. Use the ingest-url command:
   /ingest-url

3. When Claude asks, provide this URL:
   https://inductiveautomation.com/blog/perspective-performance-tips

[... rest of instructions ...]
```

### Using Claude Code Directly:

```bash
# Step 1: Start Claude Code
$ claude

# Step 2: In Claude Code, type
> /ingest-url

# Step 3: Paste your URL when prompted
> https://inductiveautomation.com/blog/perspective-performance-tips

# Step 4: Claude will process it and update files
# Claude: "I've analyzed the content and added 3 best practices to
#          sections/perspective-views.md. Here's what was added:
#          - Use component pooling for repeating elements
#          - Minimize bindings on container components
#          - Implement lazy loading for large datasets"

# Step 5: Review the changes
$ git diff sections/perspective-views.md

# Step 6: Commit if you're happy
$ git add sections/
$ git commit -m "Add Perspective performance tips from IA blog"
$ git push
```

## What Happens Behind the Scenes?

When you use `/ingest-url`:

1. **Claude fetches the content** using WebFetch tool
2. **Claude analyzes it** to understand what it's about
3. **Claude categorizes it** into appropriate sections
4. **Claude extracts best practices** from the content
5. **Claude updates markdown files** in `sections/`
6. **Claude shows you** what was changed

All of this uses your Claude Code subscription - no API calls, no extra charges!

## Comparison: Claude Code vs API Script

| Feature | Claude Code Method | API Script Method |
|---------|-------------------|-------------------|
| **Cost** | FREE (included) | Pay-per-token |
| **Setup** | None | Requires API key |
| **Interaction** | Interactive | Automated |
| **Flexibility** | High (can adjust on-the-fly) | Medium (predefined) |
| **Best For** | Manual processing, learning | Batch automation, CI/CD |

## Tips for Best Results

1. **Use quality sources** - Blog posts, official documentation, detailed forum posts work best
2. **One at a time** - Process URLs individually for better control
3. **Review carefully** - Always check `git diff` before committing
4. **Provide context** - If Claude misses something, you can guide it: "Also add this as a tip under gateway-configuration"

## Troubleshooting

### "Command not found: claude"

Make sure Claude Code is installed and in your PATH. If you just installed it, you may need to restart your terminal.

### "I don't see the /ingest-url command"

Make sure you're running Claude Code from the repository root directory where the `.claude/commands/` directory exists.

### The content wasn't relevant

If Claude determines content isn't relevant to Ignition, it will let you know. You can:
- Try a different URL
- Manually add the content if you disagree with the assessment

### Want to process multiple URLs?

Just run the slash command multiple times, or create a simple loop:

```bash
# Start Claude Code once
claude

# Then in Claude Code, repeatedly use:
/ingest-url
# (paste URL 1)

/ingest-url
# (paste URL 2)

# etc.
```

## When to Use the API Script Instead

The API script (`ingest_content.py`) is better for:

- **Automation** - Running in CI/CD pipelines or GitHub Actions
- **Batch processing** - Processing many URLs at once
- **Scheduled tasks** - Automatic periodic content checking
- **Headless environments** - Servers without interactive terminals

But for manual, one-off content ingestion, **Claude Code is the way to go** - it's free and uses your existing subscription!

## Questions?

- Check the main [README.md](README.md) for more automation details
- See [QUICKSTART.md](QUICKSTART.md) for the API approach
- Open an issue on GitHub if you run into problems

---

**Remember**: This method uses zero API tokens and leverages your existing Claude Code subscription. Process as many URLs as you want at no additional cost!
