# Content Ingestion Skill

**Description:** Automatically ingest Ignition-related content from URLs and incorporate best practices into the repository.

**When to use:** When a user provides a URL to a blog post, article, or documentation about Ignition SCADA that should be added to the best practices repository.

**Triggers:**
- User provides a URL with context like "ingest this" or "add this to the repo"
- GitHub issue with `content-ingestion` label
- @claude mention in an issue containing a URL

---

## Instructions

When this skill is invoked, follow these steps:

### 1. Extract the URL

Identify the URL from the user's request or GitHub issue. The URL should point to Ignition-related content (blog post, documentation, article, etc.).

### 2. Fetch and Analyze Content

Use the WebFetch tool to retrieve the content from the URL. Then analyze it to determine:

- **Relevance**: Is this content relevant to Ignition SCADA platform?
- **Sections**: Which repository sections does this apply to?
  - gateway-configuration
  - perspective-views
  - gateway-scripting
  - tags
  - database-integration
  - testing-deployment
  - source-control
  - reports
  - webdev
  - alarms

- **Best Practices**: What are the key actionable recommendations?
- **External Links**: Should this URL be added to the "Links to More Information" section?

### 3. Update Section Files

For each relevant section:

1. Read the existing section file from `sections/<section-name>.md`
2. Add new best practices under the "## Tips and Recommendations" section
   - Format: `- **Practice Title**\n  - Details if needed`
   - Follow the existing formatting style
   - Don't duplicate existing content

3. Add the source URL under "## Links to More Information" section
   - Format: `- [Descriptive Title](URL)`
   - Only add if the link provides value as a reference

### 4. Create Summary

Provide a clear summary of:
- Which sections were updated
- What best practices were added
- What links were added
- Recommendation to review changes before committing

### 5. If in GitHub Actions Context

If running via GitHub Actions (issue trigger):
- Create a new branch: `auto-ingest/<issue-number>`
- Commit the changes
- Create a pull request
- Comment on the original issue with the summary and PR link

If running interactively:
- Just make the changes and show the summary
- User will review and commit manually

---

## Available Section Files

```
sections/
├── gateway-configuration.md  # Gateway setup and configuration
├── perspective-views.md      # Perspective view development
├── gateway-scripting.md      # Gateway scripting best practices
├── tags.md                   # Tag structure and organization
├── database-integration.md   # Database connectivity and queries
├── testing-deployment.md     # Testing and deployment workflows
├── source-control.md         # Version control practices
├── reports.md                # Report development
├── webdev.md                 # Web Development Module
└── alarms.md                 # Alarm notification pipelines
```

---

## Example Usage

### Interactive (Claude Code CLI):

```
User: Ingest this URL: https://inductiveautomation.com/blog/perspective-performance

Claude: I'll fetch and analyze that content...
[Fetches content]
[Analyzes and determines it's relevant to perspective-views]
[Updates sections/perspective-views.md]

Summary:
✓ Updated sections/perspective-views.md
  - Added: Use component pooling for better performance
  - Added: Minimize bindings on containers
  - Added: Implement lazy loading
✓ Added link to external resources

Review changes with: git diff sections/
```

### Via GitHub Issue:

```
Issue #42: "Ingest: Performance Tips"
Body: https://inductiveautomation.com/blog/perspective-performance
@claude please ingest this

Claude (via GitHub Actions):
[Creates branch: auto-ingest/42]
[Updates files]
[Creates PR #43]
[Comments on issue #42]:

✓ Content ingested successfully!

Updated sections:
- perspective-views.md (3 new best practices)

Pull request: #43
Please review and merge if the changes look good.
```

---

## Error Handling

If content is not relevant to Ignition:
- Politely explain why it's not relevant
- Don't make any changes
- Suggest the user verify the URL

If a section file doesn't exist:
- Note the missing file
- Skip updating that section
- Continue with other sections

If unable to fetch the URL:
- Explain the error (404, timeout, etc.)
- Ask the user to verify the URL
- Suggest alternatives if possible

---

## Quality Guidelines

- **Be conservative**: Only add high-quality, actionable best practices
- **Avoid duplication**: Check existing content before adding
- **Maintain formatting**: Follow the existing markdown style
- **Keep it concise**: Best practices should be brief and clear
- **Verify relevance**: Ensure content is truly about Ignition SCADA

---

## Supporting Tools

- **WebFetch**: Retrieve content from URLs
- **Read**: Read existing section files
- **Edit**: Update section files with new content
- **Bash**: For git operations (branch, commit, PR creation)
- **Grep/Glob**: Search for existing content to avoid duplication
