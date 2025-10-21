# Ingest Content from URL

You are helping to add content to the Ignition Best Practices repository by processing a URL provided by the user.

## Your Task

1. **Fetch the URL content** - Use WebFetch to get the content from the URL
2. **Analyze the content** - Determine:
   - Is it relevant to Ignition SCADA platform?
   - Which sections does it apply to? (gateway-configuration, perspective-views, gateway-scripting, tags, database-integration, testing-deployment, source-control, reports, webdev, alarms)
   - What are the key best practices or recommendations?
   - What links should be added to "Links to More Information" sections?

3. **Update the markdown files** - Add the extracted best practices to the appropriate section files in `sections/`
   - Add bullet points under "## Tips and Recommendations"
   - Add links under "## Links to More Information"
   - Follow the existing formatting style

4. **Show a summary** - Tell the user:
   - What sections were updated
   - What was added
   - Suggest they review with `git diff` before committing

## Available Sections

- `sections/gateway-configuration.md` - Gateway setup and configuration
- `sections/perspective-views.md` - Perspective view development
- `sections/gateway-scripting.md` - Gateway scripting best practices
- `sections/tags.md` - Tag structure and organization
- `sections/database-integration.md` - Database connectivity and queries
- `sections/testing-deployment.md` - Testing and deployment workflows
- `sections/source-control.md` - Version control practices
- `sections/reports.md` - Report development
- `sections/webdev.md` - Web Development Module
- `sections/alarms.md` - Alarm notification pipelines

## Important Notes

- Read the existing section files first to understand the format
- Don't duplicate existing content
- Keep recommendations concise and actionable
- Preserve the existing markdown structure
- If content isn't relevant to Ignition, politely let the user know

## Example Usage

User provides a URL like: https://inductiveautomation.com/blog/troubleshooting-cpu

You should:
1. Fetch and analyze the content
2. Add relevant tips to gateway-configuration.md
3. Add the blog link to the Links section
4. Summarize what was added
