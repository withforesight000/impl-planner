# impl-planner HTML Output Variant

Read this reference only when the user explicitly asks for HTML, a browser-readable artifact, or a visual report.

The HTML report must preserve the same information as the Markdown plan:

- Missing context and ambiguities
- Assumptions
- Plan milestones
- Acceptance criteria
- Validation commands
- Decision notes
- Main risks
- Rollback considerations

HTML constraints:

- Use semantic HTML: `main`, `section`, `h1`, `h2`, `h3`, `ul`, `ol`, `pre`, `code`, and `table` when useful.
- Keep CSS minimal and inline inside a single `<style>` block.
- Do not use JavaScript.
- Do not load external fonts, stylesheets, scripts, images, or remote assets.
- Preserve command snippets inside `<pre><code>...</code></pre>`.
- Keep the report printable and readable in light and dark browser settings where possible.
