---
name: Ingest Content
about: Submit a URL to be processed and added to the best practices - works from anywhere!
title: 'Ingest: [Brief description]'
labels: content-ingestion
assignees: ''
---

## URL to Ingest

<!-- Paste the URL to the blog post, article, or documentation below -->



## Context (Optional)

<!--
Any notes about why this content is valuable or what it covers.
This helps Claude understand and categorize the content better.
-->



---

## 🤖 What Happens Next?

### Automatic Processing (Claude Code Pro)

If you have Claude Code Pro with GitHub Actions enabled, simply:

**Option 1: Add the label**
- This issue has the `content-ingestion` label
- GitHub Actions will automatically process it!

**Option 2: Mention @claude**
- Comment: `@claude please ingest this URL`
- GitHub Actions will automatically process it!

Claude will:
1. Fetch and analyze the URL
2. Update the appropriate section files
3. Create a pull request with changes
4. Comment here with a summary

**Cost:** $0 - Uses your Claude Code Pro subscription!

### Manual Processing (Alternative)

You can also process this manually with Claude Code:

```bash
claude
> Process issue #XX - ingest the URL
```

---

## 📖 Learn More

- [Automation Guide](../automation/README.md)
- [GitHub Issue Workflow](../automation/GITHUB_ISSUE_WORKFLOW.md)
- [Claude Code Workflow](../automation/CLAUDE_CODE_WORKFLOW.md)
