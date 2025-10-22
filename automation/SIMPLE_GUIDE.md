# Content Ingestion - Simple Guide

**One skill, two ways to use it. All FREE with your existing Claude Code subscription!**

---

## How It Works

This repo has a **Claude Code Skill** at `.skills/content-ingest/SKILL.md` that teaches Claude how to automatically:
- Fetch content from URLs
- Analyze relevance to Ignition SCADA
- Extract best practices
- Update markdown files
- Add external links

---

## The Two Ways

### 1. GitHub Issues (📱 Mobile-Friendly)

**Perfect for:** Capturing URLs on the go

**How:**
1. Create a GitHub issue with a URL
2. Add the `content-ingestion` label
3. Later, process with Claude Code:
   ```
   claude
   > Process issue #XX - ingest the URL
   ```

**Files used:** `.skills/content-ingest/SKILL.md`

[Full guide →](GITHUB_ISSUE_WORKFLOW.md)

---

### 2. Claude Code Direct (💻 At Your Computer)

**Perfect for:** Immediate processing

**How:**
1. Run `claude` in the repo
2. Say: `Ingest this URL: https://example.com`
3. Claude uses the skill automatically

**Files used:** `.skills/content-ingest/SKILL.md`

[Full guide →](CLAUDE_CODE_WORKFLOW.md)

---

## Quick Decision Guide

**On your phone?** → GitHub Issues (Method 1)

**At your computer?** → Direct (Method 2)

---

## Cost

**$0** - Uses your existing Claude Code subscription

**No API keys** - No setup required

**Unlimited** - Process as many URLs as you want

---

## Summary

- **1 Skill** (`.skills/content-ingest/SKILL.md`) - Used by both methods
- **2 Ways to use it** - Mobile or desktop
- **No API keys** - Just your Claude Code subscription
- **No conflicts** - Simple and clean!

Choose the method that works for your situation. They both produce the same great results!
