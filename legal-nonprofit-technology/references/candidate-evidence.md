# Candidate evidence contract

The resume is an index into a larger history, not the only allowed source.
Evidence may come from candidate-authored code, commits, tests, architecture and
project documents, career documents, and candidate-supplied explanations.

Each atomic record contains:

```yaml
id: stable-content-derived-id
capability: concise demonstrated capability
claim: publishable wording when permitted
evidence_refs: [source-path-or-artifact-and-span]
attribution: authored | coauthored | described | contextual
publication_state: publishable | private_context | needs_confirmation | prohibited
confidence_basis: direct_artifact | repeated_artifacts | candidate_statement | context_only
allowed_abstraction: optional redacted wording
source_version: immutable hash
```

## Evidence strength

- Candidate-authored implementation plus tests or design rationale can support
  a demonstrated technical capability.
- Commit attribution strengthens authorship but does not by itself prove solo
  ownership or production impact.
- A dependency, lockfile, import, tutorial, generated file, or template proves
  exposure only. Inspect substantive authored use before claiming experience.
- Public employer material supplies context, never personal ownership.
- Metrics, dates, employers, titles, business outcomes, team size, production
  deployment, and regulated-domain claims require direct evidence.

## Publication states

- `publishable`: may be used within the permitted abstraction.
- `private_context`: may improve matching but must not appear in an application.
- `needs_confirmation`: hold from publication until direct evidence or a clear
  candidate statement resolves it.
- `prohibited`: never use or reveal.

Secrets and proprietary identifiers are prohibited. Confidential work may
support a generalized capability only when `allowed_abstraction` is explicit
and reveals no protected detail. Preserve evidence ids beside every tailored
clause so reviews can verify rather than guess.
