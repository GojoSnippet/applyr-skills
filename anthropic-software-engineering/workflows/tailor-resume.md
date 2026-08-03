---
capabilities:
  - browser
---

# Tailor the canonical résumé

Read `knowledge/roles.md`, `knowledge/company.md`, `knowledge/engineering.md`,
the canonical résumé, approved profile, and company-private candidate files.
Use the exact job description as the target.

Produce a focused, truthful `.tex` revision:

1. Preserve employers, titles, dates, education, technologies, metrics, and
   achievements exactly unless approved evidence supports a change.
2. Select and reorder the strongest evidence for this role.
3. Reword only to clarify ownership, technical depth, scale, reliability, and
   performance already present in the sources.
4. Prefer evidence connected to distributed systems, large-scale
   infrastructure, ML/data pipelines, backend systems in Python/Go/Rust/C++,
   developer tooling, and measurable performance or reliability improvements
   when it exists — Anthropic engineering postings consistently emphasize
   systems that support research and production ML workloads at scale over
   narrow feature work.
5. Surface ownership of a system end to end, working effectively with
   ambiguity, and collaborating closely with research/ML teams only when
   evidenced.
6. Do not claim AI-research experience, publications, a machine-learning
   research background, years of experience, relocation, or work
   authorization unless approved inputs say so.
7. Keep the résumé concise and compile-safe. Compile and inspect the PDF
   before returning it.

Return the source artifact, PDF artifact, and a short change summary tied to
the approved evidence used.
