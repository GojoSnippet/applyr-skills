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
4. Prefer evidence connected to distributed systems, high-throughput or
   low-latency services, production reliability, data pipelines,
   infrastructure, backend systems in Python/Java/C++/TypeScript, and
   quantifiable performance or scale improvements when it exists — Citadel
   postings consistently emphasize production-grade systems and measurable
   impact over breadth.
5. Surface ownership of a system end to end, debugging under pressure, and
   working with tight technical constraints only when evidenced — Citadel's
   own interview guidance (see `knowledge/company.md` sources) rates concrete
   ownership and outcomes above polished narrative.
6. Do not claim finance-domain experience, trading-systems experience, C++
   proficiency, years of experience, relocation, or work authorization unless
   approved inputs say so.
7. Keep the résumé concise and compile-safe. Compile and inspect the PDF
   before returning it.

Return the source artifact, PDF artifact, and a short change summary tied to
the approved evidence used.
