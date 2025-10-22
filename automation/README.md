# Automated Content Ingestion - Using Claude Code (FREE!)

**Uses your existing Claude Code subscription - no API keys, no extra costs!**

This system allows you to automatically process and incorporate Ignition-related content from URLs (blog posts, articles, documentation) into the best practices repository using your existing Claude Code subscription.

---

## How It Works

This repository includes a **Claude Code Skill** (`.skills/content-ingest/SKILL.md`) that teaches Claude how to ingest content automatically.

### The Skill

The skill enables Claude to:
- Extract and fetch content from URLs
- Analyze relevance to Ignition SCADA
- Categorize into appropriate sections
- Extract best practices
- Update markdown files
- Add external links

---

## Two Ways to Use It

### Method 1: On The Go (Mobile/Anywhere)

**Perfect for when you're reading an article on your phone or away from your computer.**

1. **Capture the URL** - [Create a GitHub issue](../.github/ISSUE_TEMPLATE/ingest-content.md) with the URL
2. **Add label** - Apply the `content-ingestion` label
3. **Process later** - When you're back at your computer with Claude Code:
   ```bash
   cd Ignition-Best-Practices
   claude
   > Process issue #XX - ingest the URL from that issue
   ```

See [GITHUB_ISSUE_WORKFLOW.md](GITHUB_ISSUE_WORKFLOW.md) for details.

### Method 2: Direct Processing (At Your Computer)

**Perfect for immediate processing when you have a URL.**

1. **Open Claude Code:**
   ```bash
   cd Ignition-Best-Practices
   claude
   ```

2. **Simply ask Claude to ingest:**
   ```
   Ingest this URL: https://inductiveautomation.com/blog/your-article
   ```

   Or:
   ```
   Process this article: https://example.com/ignition-tips
   ```

3. **Claude automatically:**
   - Uses the content-ingest skill
   - Fetches and analyzes the content
   - Updates section files
   - Shows you what was added

4. **Review and commit:**
   ```bash
   git diff
   git add sections/
   git commit -m "Add content from article"
   git push
   ```

See [CLAUDE_CODE_WORKFLOW.md](CLAUDE_CODE_WORKFLOW.md) for details.

---

## Complete Example

You find a great article on your phone about Perspective performance:

**Step 1 (On mobile):**
- Create GitHub issue
- Paste URL: `https://inductiveautomation.com/blog/perspective-perf`
- Add `content-ingestion` label
- Done! Continue reading.

**Step 2 (Later at computer):**
```bash
cd Ignition-Best-Practices
claude
> Process issue #5 - ingest that Perspective performance article

# Claude fetches, analyzes, and updates files automatically
# Shows you: "Added 3 best practices to perspective-views.md"

git diff sections/perspective-views.md  # Review
git add sections/
git commit -m "Add Perspective performance tips from issue #5"
git push
```

**Total cost:** $0 (uses your existing Claude Code subscription!)

---

## Helper Script

For convenience, we provide a helper script that gives you step-by-step instructions:

```bash
./automation/ingest_with_claude.sh "https://your-url-here.com"
```

This script:
- Shows you what to type in Claude Code
- Copies the URL to your clipboard
- Provides clear next steps

---

## Repository Sections

Content can be added to these sections:

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

---

## Guides

- **[SIMPLE_GUIDE.md](SIMPLE_GUIDE.md)** - Quick overview
- **[CLAUDE_CODE_WORKFLOW.md](CLAUDE_CODE_WORKFLOW.md)** - Direct processing guide
- **[GITHUB_ISSUE_WORKFLOW.md](GITHUB_ISSUE_WORKFLOW.md)** - Mobile capture workflow

---

## FAQs

### Does this cost money?

**No!** It uses your existing Claude Code subscription. Process as many URLs as you want at no extra cost.

### Do I need to set up API keys?

**No!** No API keys, no secrets, no setup. Just use Claude Code.

### Can I process multiple URLs at once?

Yes! Just ask Claude:
```
Ingest these URLs:
- https://example.com/article1
- https://example.com/article2
```

### What if the content isn't relevant?

Claude will analyze it and let you know if it's not relevant to Ignition SCADA. You can manually add it if you disagree.

### Can I adjust what Claude adds?

Absolutely! Review the changes with `git diff`, then adjust manually if needed before committing.

---

## Troubleshooting

### "Claude doesn't understand what to do"

Make sure:
- You're running Claude Code from the repository root
- The `.skills/content-ingest/` directory exists
- You're on the main branch (or a branch with the skill)

Try being more specific:
```
Use the content-ingest skill to process this URL: https://example.com
```

### "Skill not found"

Pull the latest from main:
```bash
git checkout main
git pull origin main
```

The skill should be in `.skills/content-ingest/SKILL.md`

---

## Summary

**Capture on the go** → Create GitHub issue with URL

**Process when ready** → Use Claude Code with the skill

**Cost** → $0 (uses your existing subscription)

**Setup required** → None!

Simple, free, and uses the tools you already have! 🚀
