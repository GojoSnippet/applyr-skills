---
capabilities:
  - browser
---

# Tailor the canonical résumé

Read `knowledge/roles.md`, `knowledge/company.md`, `knowledge/engineering.md`,
the canonical résumé, approved profile, and company-private candidate files.
Use the exact job description of the target Owner.com posting as the target.

Produce a focused, truthful `.tex` revision:

1. Preserve employers, titles, dates, education, technologies, metrics, and
   achievements exactly unless approved evidence supports a change.
2. Select and reorder the strongest evidence for this role.
3. Reword only to clarify ownership, technical depth, scale, reliability, and
   business impact already present in the sources.
4. Owner.com reads for "TypeScript everywhere" product engineering with
   end-to-end ownership at consumer-traffic scale, and describes itself as
   AI-native — software that acts agentically for restaurant owners. When
   the corpus supports them, foreground in roughly this order:
   - TypeScript/Node.js/React/Next.js production work;
   - agentic/LLM platform engineering (agent runtimes, LLM gateways or
     integrations, evaluation harnesses, computer-use agents) — this is
     their product direction, so corpus-backed agent-infrastructure work is
     the differentiator, not filler;
   - distributed-systems reliability and throughput at scale (queues,
     event streams, exactly-once processing, p99 latency, crash-safety),
     phrased as ownership of production outcomes;
   - founding-engineer / 0→1 / solo-shipped evidence — their culture prizes
     "Build as an Owner" and staffs heavily from ex-founders;
   - AWS and document-store (MongoDB-family) experience;
   - commerce-shaped systems (ordering, booking, payments, double-booking
     prevention, loyalty/lifecycle) — only where genuinely evidenced.
5. Variant fit: for a Backend posting, lead with backend/distributed-systems
   and platform evidence; for a Full-Stack posting, bring corpus-backed
   React/Next.js/frontend work up beside it. Never convert a backend fact
   into a frontend claim or vice versa.
6. Mirror their language honestly: quantified outcomes, speed-with-quality,
   conception-to-ship ownership, product impact for the end customer. Keep
   every number exactly as the corpus states it.
7. Landmines — do not:
   - claim restaurant, hospitality, or SMB-domain experience, Vue, Ruby, or
     any technology absent from approved inputs;
   - present configurability/customization-platform work as a selling point —
     Owner's product philosophy explicitly rejects customization; frame such
     evidence as standardization, reliability, or scale instead;
   - claim years of experience, seniority, location, or authorization beyond
     approved inputs;
   - assert Owner's interview process, comp, internal stack details, or any
     community-sourced claim as fact anywhere in the résumé;
   - reference LinkedIn anywhere.
8. Keep the résumé concise and compile-safe. Compile and inspect the PDF
   before returning it.

Return the source artifact, PDF artifact, and a short change summary tied to
the approved evidence used.
