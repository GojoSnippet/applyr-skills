# State and deduplication

Lifecycle:

```text
discovered -> nonprofit_verified -> scored -> researched -> drafted -> reviewed
-> applying -> submission_unverified -> submitted -> follow_up
```

Terminal alternatives are `rejected`, `expired`, `withdrawn`, and `failed`.
`blocked` and `submission_unverified` are recoverable states.

Build `org_key` from authoritative legal identity when possible. Build
`job_key` from organization plus source posting or requisition id; retain a
secondary fingerprint of canonical URL, normalized title, location, and
description content hash.

Check duplicates:

1. while ingesting discovery results;
2. before spending on research or tailoring;
3. while atomically claiming an application run;
4. inside the final submission tool.

A canonical URL with a changed description content hash creates an immutable
new job-description version and reruns scoring. It does not erase the prior
application record or automatically authorize a second application. A repost
with a new requisition is linked to its predecessor for an explicit reapply
decision.

Each `state.json` records job, organization, candidate-evidence, skill, and
artifact versions; current lease; transitions; blockers; and proof references.
Only a stored stable receipt or equivalent confirmation permits `submitted`.
