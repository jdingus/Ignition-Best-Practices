# GitHub Issue Workflow - Ingest On The Go!

**Ingest content from anywhere, anytime - just create a GitHub issue with a URL!**

This workflow allows you to trigger content ingestion by simply creating a GitHub issue or commenting on one. Perfect for when you're on mobile, away from your computer, or just want a hands-free experience.

---

## 🎯 Two Methods Available

### Method 1: Manual (FREE - No API Key Needed!)

**Best for:** You're a maintainer with Claude Code access

1. Create a GitHub issue with the URL
2. Later, when at your computer, process it with Claude Code
3. Zero API costs!

### Method 2: Automated (Requires API Key Setup)

**Best for:** Fully automated workflow, anyone can submit

1. Create a GitHub issue with the URL and `@claude` mention
2. GitHub Actions + Claude Code automatically processes it
3. Creates a PR with the changes
4. Requires ANTHROPIC_API_KEY in repo secrets

---

## Method 1: Manual Workflow (Recommended - FREE!)

### Step 1: Create an Issue (From Anywhere!)

On your phone, tablet, or any browser, create a new issue:

**Title:** `Ingest: [Brief description]`

**Body:**
```
https://inductiveautomation.com/blog/your-article-here

## Context
This article discusses perspective performance optimization tips.
```

**Label:** Add the `content-ingestion` label

### Step 2: Process When Ready (At Your Computer)

When you're back at your computer with Claude Code:

```bash
# Open the repo in Claude Code
cd Ignition-Best-Practices
claude

# Tell Claude to process the issue
> Process issue #42 - ingest the URL

# Or use the skill directly
> Use the content-ingest skill for https://example.com/article
```

Claude will:
- Fetch the content from the URL
- Analyze and categorize it
- Update the appropriate section files
- Show you what was added
- You can then commit and close the issue

### Step 3: Close the Issue

After reviewing and committing:
```bash
git add sections/
git commit -m "Add content from issue #42"
git push
```

Then close the issue on GitHub with a comment summarizing what was added.

---

## Method 2: Automated Workflow (Requires Setup)

### One-Time Setup

#### 1. Get Anthropic API Key

1. Go to https://console.anthropic.com/
2. Create an API key
3. Copy it

#### 2. Add to GitHub Secrets

1. Go to your repo: Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `ANTHROPIC_API_KEY`
4. Value: Paste your API key
5. Click "Add secret"

#### 3. Enable GitHub Actions

The workflow file `.github/workflows/claude-ingest.yml` is already set up!

### Using the Automated Workflow

#### Option A: Create Issue with Label

1. Create a new issue
2. Add the `content-ingestion` label
3. Paste the URL in the body
4. Submit

GitHub Actions will:
- Detect the label
- Run Claude Code
- Process the URL
- Create a PR with changes
- Comment on your issue with a summary

#### Option B: Mention @claude in Comments

On any existing issue:
```
@claude please ingest https://example.com/article
```

Claude will respond automatically!

---

## Complete Example Workflows

### Example 1: On Mobile

You're reading an article on your phone about Ignition alarm best practices:

```
1. Open GitHub app or mobile browser
2. Navigate to your repo
3. Click "Issues" → "New Issue"
4. Title: "Ingest: Alarm Best Practices from IA Blog"
5. Body: https://inductiveautomation.com/blog/alarm-best-practices
6. Label: content-ingestion
7. Submit

[Later at your computer with Claude Code]
8. claude
9. > Process issue #45
10. Review changes
11. Commit and close issue
```

### Example 2: Fully Automated (with API key)

```
1. [On your phone] Create issue with URL
2. [Automatically] GitHub Actions triggers
3. [Automatically] Claude processes the URL
4. [Automatically] PR #46 created
5. [You] Review PR #46
6. [You] Merge if good
7. [Automatically] Issue #45 closed
```

### Example 3: Quick Comment

On an existing discussion:

```
User: "This article has great tips on tag organization"
      https://example.com/tag-structure

You: "@claude please ingest this article"

[If automated] Claude creates PR automatically
[If manual] You process it later with Claude Code
```

---

## Issue Template

We've created an issue template at `.github/ISSUE_TEMPLATE/ingest-content.md` that makes this even easier!

Just click "New Issue" → "Ingest Content" and fill in the form.

---

## Cost Comparison

| Method | Setup | Per-Use Cost | Best For |
|--------|-------|--------------|----------|
| **Manual** | 0 min | **$0** ✅ | Maintainers with Claude Code |
| **Automated** | 10 min | $0.01-0.05 | Anyone can submit, auto-process |

---

## Skill Integration

The `.skills/content-ingest/SKILL.md` teaches Claude how to:
- Extract URLs from issues
- Fetch and analyze content
- Update section files properly
- Create PRs (if in GitHub Actions)
- Comment on issues with summaries

This skill works in both manual and automated workflows!

---

## Troubleshooting

### Manual Workflow

**Q: Claude doesn't seem to understand what to do**

A: Be specific:
```
Process GitHub issue #42 using the content-ingest skill.
The issue contains a URL to fetch and add to the repository.
```

**Q: Can I process multiple issues at once?**

A: Yes! Just ask:
```
Process issues #41, #42, and #43 - they all have URLs to ingest
```

### Automated Workflow

**Q: GitHub Actions didn't trigger**

A: Check:
- Is the `content-ingestion` label applied?
- Did you mention `@claude` in the comment?
- Is `ANTHROPIC_API_KEY` set in repository secrets?
- Are GitHub Actions enabled for your repo?

**Q: Action failed**

A: Check the Actions log:
1. Go to "Actions" tab in GitHub
2. Click the failed run
3. Check the error message
4. Common issues:
   - Missing API key
   - Invalid URL
   - Content not relevant to Ignition

**Q: I want to disable automation temporarily**

Rename the workflow file:
```bash
mv .github/workflows/claude-ingest.yml .github/workflows/claude-ingest.yml.disabled
```

---

## Tips for Best Results

### Writing Good Issues

✅ **Good:**
```
Title: Ingest: Perspective Performance Tips
Body: https://inductiveautomation.com/blog/perspective-perf

This article covers component pooling and lazy loading strategies.
```

❌ **Bad:**
```
Title: Article
Body: check this out https://example.com
```

### Providing Context

Help Claude understand the content:
```
https://example.com/article

This discusses gateway CPU troubleshooting and should go in:
- gateway-configuration
- testing-deployment
```

### Multiple URLs

Create separate issues for each URL for better tracking:
```
Issue #50: Ingest URL 1
Issue #51: Ingest URL 2
Issue #52: Ingest URL 3
```

---

## Advanced Usage

### Bulk Ingestion via Issues

Create multiple issues at once:
```bash
# Create issues programmatically
gh issue create --title "Ingest: Article 1" --body "URL1" --label content-ingestion
gh issue create --title "Ingest: Article 2" --body "URL2" --label content-ingestion
gh issue create --title "Ingest: Article 3" --body "URL3" --label content-ingestion

# Then process them all with Claude Code:
claude
> Process all open issues with the content-ingestion label
```

### Email to Issue

Use GitHub's email integration to create issues by email:
```
To: repo+owner/Ignition-Best-Practices@reply.github.com
Subject: Ingest: New Article

https://example.com/article
```

### Bookmarklet

Create a browser bookmarklet to instantly create issues:
```javascript
javascript:(function(){window.open('https://github.com/YOUR-USERNAME/Ignition-Best-Practices/issues/new?labels=content-ingestion&body='+encodeURIComponent(window.location.href));})();
```

---

## What Gets Created

When you ingest content via GitHub issues:

1. **Manual workflow:**
   - Updates section files directly
   - You commit manually
   - You close the issue with a summary

2. **Automated workflow:**
   - New branch: `auto-ingest/<issue-number>`
   - Updated section files
   - Pull request: #XX
   - Comment on issue with summary
   - Issue closed when PR merged

---

## Next Steps

1. **Try it now:** Create a test issue with a URL
2. **Add the label:** Apply `content-ingestion` label
3. **Process it:**
   - Manual: Use Claude Code when ready
   - Automated: Set up API key and watch it work!

4. **Bookmark this page:** For quick reference on the go

---

## Summary

You can now ingest content from **anywhere**:

📱 **On mobile?** Create an issue, process later
💻 **At computer?** Use Claude Code directly
🤖 **Want automation?** Set up API key for hands-free

All methods use the same `content-ingest` skill and produce the same great results!
