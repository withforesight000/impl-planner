# impl-planner HTML Output Variant

Read this reference only when the user explicitly asks for HTML, a browser-readable artifact, or a visual report.

The HTML report must preserve the same information as the Markdown plan:

- Purpose and background
- Repository understanding and evidence labels
- Missing context and ambiguities
- Assumptions
- Plan status
- Plan milestones
- Requirements covered and implementation approach
- Affected files / modules and out of scope
- Acceptance criteria
- Validation commands
- Decision notes
- Main risks
- Rollback considerations

HTML constraints:

- Use semantic HTML: `main`, `section`, `h1`, `h2`, `h3`, `h4`, `ul`, `ol`, `pre`, `code`, and `table` when useful.
- Keep CSS minimal and inline inside a single `<style>` block.
- Do not use JavaScript.
- Do not load external fonts, stylesheets, scripts, images, or remote assets.
- Preserve command snippets inside `<pre><code>...</code></pre>`.
- Preserve `[Observed]`, `[Inferred]`, `[Proposed]`, `[Unknown]`, and validation-provenance labels as text.
- Keep the report printable and readable in light and dark browser settings where possible.
