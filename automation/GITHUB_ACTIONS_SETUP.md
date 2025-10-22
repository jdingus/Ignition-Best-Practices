# GitHub Actions Setup Guide

## Important: Issues Found & Fixed

If you tried to use the GitHub Actions workflow and it failed, here's what was wrong and how to fix it:

### Issue #1: Incorrect Label Syntax ✅ FIXED

**Problem:**
```yaml
if: (github.event.issue.labels[*].name contains 'content-ingestion')
```

**Fixed to:**
```yaml
if: contains(github.event.issue.labels.*.name, 'content-ingestion')
```

### Issue #2: Skill Not on Main Branch ⚠️ NEEDS ATTENTION

**Problem:** The `.skills/content-ingest/` directory is currently on the feature branch `claude/automate-info-ingestion-011CULgTt2NszXWA2eLUPXw9`, but the workflow checks out the default branch (main).

**Solution:** You need to merge this branch to main first!

```bash
# After testing and approving the code:
git checkout main
git merge claude/automate-info-ingestion-011CULgTt2NszXWA2eLUPXw9
git push origin main
```

### Issue #3: API Key Not Set ⚠️ SETUP REQUIRED

**Problem:** The workflow requires `ANTHROPIC_API_KEY` in your repository secrets.

**Solution:**

1. Get your Anthropic API key from https://console.anthropic.com/
2. Go to your GitHub repo: **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"**
4. Name: `ANTHROPIC_API_KEY`
5. Value: Paste your API key
6. Click **"Add secret"**

---

## Complete Setup Checklist

Before the GitHub Actions workflow will work, you need:

### ✅ Step 1: Merge to Main

```bash
# Make sure the skill is on your main branch
git checkout main
git merge claude/automate-info-ingestion-011CULgTt2NszXWA2eLUPXw9
git push
```

### ✅ Step 2: Add API Key to Secrets

1. Visit: `https://github.com/YOUR-USERNAME/Ignition-Best-Practices/settings/secrets/actions`
2. Add `ANTHROPIC_API_KEY` with your key from https://console.anthropic.com/

### ✅ Step 3: Enable GitHub Actions

1. Go to your repo → **Settings** → **Actions** → **General**
2. Under "Actions permissions", ensure actions are enabled
3. Under "Workflow permissions", select:
   - ✅ Read and write permissions
   - ✅ Allow GitHub Actions to create and approve pull requests

### ✅ Step 4: Test It!

Create a test issue:
1. Go to Issues → New Issue
2. Use the "Ingest Content" template
3. Paste a URL (test with: https://inductiveautomation.com/blog)
4. Add label: `content-ingestion`
5. Submit

Or comment on any issue:
```
@claude please test the workflow
```

---

## Troubleshooting

### Workflow Doesn't Trigger

**Check:**
- Is the workflow file on the main branch?
- Did you push the `.github/workflows/claude-ingest.yml` file?
- Are GitHub Actions enabled in Settings?

**Debug:**
Go to the "Actions" tab in your repo to see workflow runs and errors.

### "Secret ANTHROPIC_API_KEY not found"

**Solution:** Add the API key to repository secrets (see Step 2 above)

### "Skill not found" or Claude doesn't know how to ingest

**Solution:** The `.skills/` directory isn't on the branch being checked out. Merge to main first (see Step 1 above).

### Workflow Runs But Doesn't Work

**Check the logs:**
1. Go to "Actions" tab
2. Click the failed run
3. Expand the "Run Claude Code" step
4. Look for error messages

Common issues:
- API key invalid or expired
- Permissions not set correctly
- Skill file missing or malformed

---

## Current Status

Based on issue #3 that failed, here's what likely happened:

1. ❌ **Label syntax was wrong** → Fixed in latest commit
2. ❌ **Skill not on main** → Need to merge branch to main
3. ❌ **API key not set** → Need to add to secrets

## Next Steps

1. **Review and merge this PR** to get the skill onto main
2. **Add ANTHROPIC_API_KEY** to repository secrets
3. **Enable workflow permissions** in settings
4. **Retry issue #3** or create a new test issue

---

## Alternative: Use Manual Workflow (No API Key!)

If you don't want to set up the automated workflow with API keys, you can still use the **FREE manual method**:

```bash
# When you see an issue with a URL:
claude
> Process issue #3 using the content-ingest skill
```

This uses your existing Claude Code subscription at no extra cost!

See [GITHUB_ISSUE_WORKFLOW.md](GITHUB_ISSUE_WORKFLOW.md) for details.

---

## Summary

The workflow **will work** once you:
1. ✅ Merge this branch to main (get the skill on main)
2. ✅ Add `ANTHROPIC_API_KEY` to secrets
3. ✅ Enable workflow permissions

Then it will automatically process issues with the `content-ingestion` label or `@claude` mentions!
