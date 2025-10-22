---
name: Ingest Content
about: Submit a URL to be processed and added to the best practices (from anywhere - mobile, desktop, etc!)
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

### ⚙️ Automated Processing Status

**Current Status:** Automation requires setup (see below)

**If automation is configured**, commenting `@claude` will:
1. Automatically fetch and analyze the URL
2. Update the appropriate section files
3. Create a pull request with changes
4. Comment here with a summary

**Setup Required:** See [GitHub Actions Setup Guide](../automation/GITHUB_ACTIONS_SETUP.md) for:
- Merging skill to main branch
- Adding ANTHROPIC_API_KEY to secrets
- Enabling workflow permissions

### Manual Processing (FREE - Always Works!)
A maintainer can process this issue using Claude Code:
```bash
claude
> Process issue #XX using the content-ingest skill
```
**Cost:** $0 (uses existing Claude Code subscription)
**Works immediately:** No setup required!

---

## 📖 Learn More

- [GitHub Issue Workflow Guide](../automation/GITHUB_ISSUE_WORKFLOW.md)
- [Claude Code FREE Workflow](../automation/CLAUDE_CODE_WORKFLOW.md)
- [All Automation Options](../automation/README.md)
