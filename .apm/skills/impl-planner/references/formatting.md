# impl-planner Formatting Constraints

Read this reference when formatting constraints are unclear or the output needs tables, code blocks, or unusually compact structure.

- Use Markdown headings and bullet lists.
- Tables are allowed when they make comparisons, option tradeoffs, or file lists easier to scan.
- The affected-files, validation-commands, and main-risks subsections require the core contract's respective two-column tables when entries exist; other subsections retain their existing flexible format.
- Keep the core contract's required headings, order, and milestone fields for every plan, including small changes. Make small plans concise through shorter content, not omitted headings.
- Keep assumptions within the existing ambiguity subsections, not a separate heading. Apply the core contract's five/ten-item limits and its explicit handling of material overflow.
- Close all code blocks.
- Prefer concise, implementation-ready bullets over long prose.
- Use the core contract's fixed parenthetical status explanation on the status line. Use short prose or bullets for decision sources, assumptions, and any plan-specific follow-up; do not require fixed tables or repeat shared context in each milestone.
- Keep evidence, requirement, acceptance, and validation IDs readable where traceability is needed.
- Use `## Plan.md`, `### Milestone`, and `####` milestone subsections so plans have a consistent hierarchy.
- Do not tell the implementer to start coding or proceed with execution.
