# Workspace and cache contract

Runtime root: `/Users/sai/Developer/work/nonprofit-job-search`.

```text
candidate/                 private evidence graph and source versions
registry/                  employer, job, application, and receipt indexes
organizations/<org-key>/   reusable public organization dossier
jobs/<job-key>/intake/     immutable job snapshot and identifiers
jobs/<job-key>/research/   job-specific research and evidence matrix
jobs/<job-key>/drafts/     job-specific resume, letter, and answers
jobs/<job-key>/review/     automated review reports
jobs/<job-key>/final/      submission-ready artifacts only
jobs/<job-key>/proof/      submitted values and confirmation evidence
jobs/<job-key>/state.json  state plus exact input versions
cache/public/              reusable content-addressed public inputs only
scratch/<run-id>/          disposable intermediates with retention TTL
archive/<year>/<month>/    completed job packages
logs/                      redacted operational logs
```

## Isolation

Mount one job workspace read-write into an application run. Other jobs are not
mounted. Mount `candidate/` and `organizations/<org-key>/` read-only. Never use
another job's resume, cover letter, answer, keyword list, evidence matrix, or
research conclusion as an input.

## Shared cache

Cache public reusable inputs only: source results, job pages, organization
research, legal-status records, and platform documentation. Every key includes
canonical identity, content hash, retrieval time, extractor version, and skill
version. A changed document creates a new object.

Job-specific prose and tailored artifacts must never enter shared cache.
Candidate evidence stays in private versioned storage, not public cache. Job
state records exact candidate, organization, job-description, and skill hashes.

## Retention

Scratch has a configurable retention TTL long enough to diagnose failures. It
is never the only home of a final artifact or receipt. Durable job packages
retain provenance, final files, review reports, and proof. Logs contain ids,
hashes, events, and redacted summaries—never secrets, raw private documents, or
full application answers.
