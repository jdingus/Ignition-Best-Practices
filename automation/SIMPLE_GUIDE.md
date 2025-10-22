# Content Ingestion - Simple Guide

**Three ways to add content to the repo. All use the same `.skills/content-ingest/SKILL.md` - no conflicts!**

---

## The Three Methods

### 1. GitHub Issues (📱 Mobile-Friendly)

**Perfect for:** On the go, mobile, capturing links quickly

**How it works:**
1. Create a GitHub issue with a URL
2. Add the `content-ingestion` label
3. Later, process with Claude Code

**No conflicts because:** Issues are just a way to capture URLs for later processing

**Files used:** `.skills/content-ingest/SKILL.md`

[Full guide →](GITHUB_ISSUE_WORKFLOW.md)

---

### 2. Claude Code Interactive (💻 At Your Computer)

**Perfect for:** Immediate processing, full control

**How it works:**
1. Run `claude` in the repo
2. Say: `Ingest this URL: https://example.com`
3. Claude uses the skill automatically

**No conflicts because:** Direct interaction with Claude, uses the same skill

**Files used:** `.skills/content-ingest/SKILL.md`

[Full guide →](CLAUDE_CODE_WORKFLOW.md)

---

### 3. API Script (🤖 Automation)

**Perfect for:** Batch processing, CI/CD, scheduled jobs

**How it works:**
1. Set up API key (one-time)
2. Run: `python ingest_content.py "https://example.com"`
3. Automated processing

**No conflicts because:** Completely separate Python script, doesn't use Claude Code

**Files used:** `automation/ingest_content.py` (standalone)

[Full guide →](README.md#api-script-setup-optional)

---

## How They Work Together

```
Method 1 (GitHub Issues)  ──┐
                            ├──> Uses .skills/content-ingest/SKILL.md
Method 2 (Claude Code)    ──┘

Method 3 (API Script)     ───> Uses standalone Python script
```

**No redundancy:**
- Methods 1 & 2 share the same skill (efficient!)
- Method 3 is completely separate (for automation)
- All three update the same section files
- Choose the method that fits your situation

---

## Quick Decision Guide

**On your phone?** → GitHub Issues (Method 1)

**At your computer with Claude Code?** → Interactive (Method 2)

**Need automation/batching?** → API Script (Method 3)

---

## What We Removed (Simplified!)

❌ **Removed:** Redundant slash command (`.claude/commands/ingest-url.md`)

✅ **Kept:** The skill (`.skills/content-ingest/SKILL.md`) - more powerful and flexible

**Why?** The skill is model-invoked (Claude knows when to use it automatically), while the slash command required typing `/ingest-url` every time. The skill is just better!

---

## Summary

- **1 Skill** (`.skills/content-ingest/SKILL.md`) - Used by Methods 1 & 2
- **1 Python Script** (`ingest_content.py`) - Used by Method 3
- **No conflicts** - Each method has its purpose
- **No redundancy** - We removed the duplicate slash command

Choose the method that works for your situation. They all produce the same great results!
