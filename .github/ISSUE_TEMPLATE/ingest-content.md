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

### Manual Processing (FREE - No API key needed!)
A maintainer will process this issue using Claude Code:
```bash
claude
> Process issue #XX using the content-ingest skill
```
**Cost:** $0 (uses existing Claude Code subscription)

### Automated Processing (If configured)
If the repo has automation set up, Claude will:
1. Automatically fetch and analyze the URL
2. Update the appropriate section files
3. Create a pull request with changes
4. Comment here with a summary

To trigger automation, mention `@claude` in a comment below!

---

## 📖 Learn More

- [GitHub Issue Workflow Guide](../automation/GITHUB_ISSUE_WORKFLOW.md)
- [Claude Code FREE Workflow](../automation/CLAUDE_CODE_WORKFLOW.md)
- [All Automation Options](../automation/README.md)
