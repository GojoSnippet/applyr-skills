---
capabilities:
  - browser
---

# Tailor the canonical résumé

Read `knowledge/roles.md`, `knowledge/company.md`, `knowledge/engineering.md`,
the canonical résumé, approved profile, and company-private candidate files.
Use the exact job description of the target UpDoc posting as the target.

Produce a focused, truthful `.tex` revision:

1. Preserve employers, titles, dates, education, technologies, metrics, and
   achievements exactly unless approved evidence supports a change.
2. Select and reorder the strongest evidence for this role.
3. Reword only to clarify ownership, technical depth, scale, reliability, and
   business impact already present in the sources.
4. Prefer evidence connected to backend systems, Python, RESTful API design,
   cloud/Azure, containerization/DevOps, production reliability, and
   regulated or safety-critical software when it exists.
5. For Senior Software Engineer, AI, surface LLM application development,
   prompt engineering, evaluation frameworks, MLOps/LLMOps, fine-tuning, and
   conversational/voice systems only when evidenced. For Senior Software
   Engineer, surface backend API design, third-party integrations,
   DevOps/CI/CD, and production ownership only when evidenced.
6. Do not claim UpDoc's stack, healthcare/clinical domain experience
   (FHIR, HIPAA, SOC 2), LLM production experience, years of experience,
   relocation, or work authorization unless approved inputs say so.
7. Keep the résumé concise and compile-safe. Compile and inspect the PDF
   before returning it.

Return the source artifact, PDF artifact, and a short change summary tied to
the approved evidence used.
