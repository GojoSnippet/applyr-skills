# Design — Glimpse Software Engineering Application Skill

**Status:** approved, 2026-07-25

## Purpose

Create a reusable company-specific skill for agents applying only to Glimpse's
Software Engineer and Senior Software Engineer roles. The skill must help an
agent recognize the correct company, understand its product and engineering
signals, tailor grounded candidate evidence, answer Glimpse's application
questions, and prepare for plausible interview topics without inventing a
reported interview process.

## Packaging and installation

Create one self-contained package:

```text
glimpse-software-engineering/
└── SKILL.md
```

Use an uppercase `SKILL.md` with valid YAML frontmatter containing only `name`
and `description`. Keep all instructions and research in that file because
Applyr's current GitHub installer discovers uppercase `SKILL.md` files but
copies only the instruction body, not bundled references.

After the repository is pushed to GitHub, Applyr's Add Skill UI can discover,
review, commit-pin, and install the folder for an agent. The existing reusable
skills library is not yet composed into application runs, so runtime wiring is
explicitly outside this task. The package remains usable as a direct agent
handoff and ready for that wiring.

## Skill behavior

### Identity and scope

- Identify the target as Glimpse at `tryglimpse.com`, the New York City AI
  platform for consumer packaged goods financial operations.
- Reject research or claims belonging to unrelated companies with similar
  names, including battery imaging and VR/AR businesses.
- Apply the guidance only to Software Engineer and Senior Software Engineer
  openings.

### Verified company context

Give the agent concise, dated knowledge of:

- Glimpse's deductions management, revenue recovery, cash application, and
  retailer/ERP integration products.
- AI-agent workflows that ingest and reconcile PDFs, spreadsheets, HTML,
  remittance data, shipping records, promotional records, and retailer data.
- Public growth and funding claims, clearly attributed to their sources and
  treated as company-reported facts rather than candidate facts.
- The five-day, on-site New York City working model.

### Engineering fit model

Use shared hiring signals across both roles:

- Python, Node.js, Next.js, MongoDB, PostgreSQL, and LLM-enabled systems.
- Full-stack delivery, production ownership, fast iteration, debugging,
  cross-functional work, communication, and comfort with ambiguity.

Branch by role:

- **Software Engineer:** emphasize evidence of at least three years of
  full-stack work, implementation speed, end-to-end project delivery, and
  hands-on problem solving.
- **Senior Software Engineer:** emphasize evidence of at least six years of
  experience, architecture, scalability, technical leadership, production
  judgment, mentoring, and improvements to engineering quality.

Treat advertised experience thresholds as role requirements, never as facts to
manufacture about the candidate.

### Candidate grounding

Use only evidence present in the candidate profile, résumé, approved answer
store, or user-provided corpus. Never infer or invent:

- years of experience;
- use of Glimpse's named technologies;
- LLM or AI-agent experience;
- metrics, revenue impact, leadership, or mentoring;
- CPG, retailer, deductions, accounting, EDI, or ERP experience;
- New York location, willingness to relocate, or work authorization.

When direct stack overlap is absent, use grounded adjacent evidence such as
learning speed, distributed systems, data pipelines, document processing,
workflow automation, reliability, or full-stack ownership. Flag required facts
that remain unknown.

### Application handling

Cover the currently observed Software Engineer form:

- Name, email, and résumé upload.
- Whether the candidate is in New York City or willing to relocate.
- Whether the candidate is authorized to work in the United States without
  current or future sponsorship.
- A 150–200 word response about the candidate's proudest professional
  accomplishment.
- A response explaining what the candidate uniquely brings to Glimpse and the
  role.

Define positive answer recipes:

- **Proudest accomplishment:** context and stakes → candidate-owned action →
  verified result → why the accomplishment matters.
- **Unique contribution:** two or three grounded strengths → evidence for each
  → connection to Glimpse's engineering problems and working style.

Do not fill relocation or authorization answers unless explicitly grounded.
Do not submit an application; stop at Applyr's normal review/submission gate.

### Interview preparation

State that no reliable public candidate account establishes Glimpse's current
interview stages. Never present an inferred stage, coding exercise, or question
as reported fact.

Use the job descriptions and product architecture to prepare plausible themes:

- full-stack and API design;
- Python/Node.js/Next.js tradeoffs;
- MongoDB/PostgreSQL data modeling;
- ingestion and normalization of messy documents and external data;
- LLM evaluation, reliability, observability, and human review;
- debugging production workflows and handling partial failure;
- system design for multi-tenant financial automation;
- rapid delivery, ownership, ambiguity, and customer-driven product decisions.

Label these as inferred preparation topics.

## Evidence model

Mark research internally using three confidence classes:

- **Confirmed:** stated in an official Glimpse page or current job posting.
- **Corroborated:** supported by a credible external company profile or investor
  source.
- **Unknown/inferred:** not publicly established; usable only as a preparation
  hypothesis and labeled accordingly.

Include a source ledger with a last-verified date. Do not use LinkedIn as a
source.

## Sources to encode

Last verified: 2026-07-25.

- Careers portal: https://jobs.ashbyhq.com/glimpse
- Software Engineer:
  https://jobs.ashbyhq.com/glimpse/767a3a59-53d6-4306-afae-6b05a265ba82
- Senior Software Engineer:
  https://jobs.ashbyhq.com/glimpse/c5b5f19b-cca0-46bd-a734-d922c26b27ad
- Platform: https://www.tryglimpse.com/platform
- AI Disputing Agents:
  https://www.tryglimpse.com/post/glimpse-ai-disputing-agents
- Company profile: https://www.ycombinator.com/companies/glimpse-2
- Founder/pivot story: https://www.rho.co/akash
- Investor announcement: https://a16z.com/announcement/investing-in-glimpse/

## Validation design

Treat this as a reference-and-behavior skill and test it before implementation:

1. Run baseline agents without the skill on a wrong-company collision prompt,
   a résumé with missing LLM experience, an underqualified senior profile, and
   a request for the "known Glimpse interview loop."
2. Record identity confusion, fabricated candidate claims, seniority inflation,
   unsupported form answers, and invented interview stages.
3. Implement the smallest skill that corrects the observed failures.
4. Re-run the same scenarios with the skill and require:
   - correct company identification;
   - explicit separation of company facts from candidate facts;
   - no ungrounded résumé or form claims;
   - correct SDE-versus-senior branching;
   - interview uncertainty stated plainly;
   - useful, evidence-based application and interview guidance.
5. Validate YAML and package structure with the skill-creator validator.

## Acceptance criteria

- `glimpse-software-engineering/SKILL.md` is the only runtime artifact added.
- The file has valid two-field YAML frontmatter and is discoverable by Applyr's
  GitHub scanner.
- The skill stays focused on the two engineering roles.
- Confirmed facts, corroborated facts, and inferences are distinguishable.
- Candidate answers remain grounded and unknown required facts are flagged.
- Interview guidance never claims a public process that research did not find.
- The skill contains no LinkedIn-derived information.
- Baseline failures are captured, corrected, and re-tested.
- Repository validation and relevant Applyr skill-discovery tests pass.

## Non-goals

- Changing Applyr's reusable-skill runtime wiring.
- Creating or editing a lowercase per-vertical `skill.md` in the Applyr repo.
- Tailoring a specific candidate résumé before candidate evidence is supplied.
- Applying to or submitting a Glimpse application.
- Publishing or pushing the repository without a separate request.
