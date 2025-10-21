---
name: Ingest Content
about: Submit a URL to be processed and added to the best practices
title: 'Ingest: [Brief description]'
labels: content-ingestion
assignees: ''
---

## URL to Ingest

<!-- Paste the URL to the blog post, article, or documentation below -->



## Type of Content

<!-- Check all that apply -->
- [ ] Blog post
- [ ] Documentation
- [ ] Forum post
- [ ] Video/Tutorial
- [ ] Case study
- [ ] Other: _____

## Suggested Sections

<!-- Which sections do you think this content applies to? (Optional - AI will determine this) -->
- [ ] Gateway Configuration
- [ ] Perspective Views
- [ ] Gateway Scripting
- [ ] Tags
- [ ] Database Integration
- [ ] Testing & Deployment
- [ ] Source Control
- [ ] Reports
- [ ] Web Development Module
- [ ] Alarm Notification Pipelines

## Additional Context

<!-- Any notes about why this content is valuable or what specific best practices it contains -->



---

## For Maintainers

To process this URL using Claude Code:

```bash
# Option 1: Use the slash command
/ingest-url

# Then paste the URL when prompted

# Option 2: Use the interactive script
./automation/ingest_with_claude.sh "<URL>"
```
