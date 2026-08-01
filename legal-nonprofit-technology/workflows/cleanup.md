# Retain durable evidence and clean disposable work

Read `references/workspace-contract.md` and
`references/state-and-deduplication.md`.

1. Confirm the run is terminal or paused with recoverable durable state.
2. Retain immutable intake, exact input versions, research sources, final
   artifacts, review reports, submitted answers, and submission proof.
3. Retain private browser evidence according to the configured history policy;
   never copy it into public cache or redacted operational logs.
4. Remove scratch only after its retention TTL and only when it is not needed
   by an active, paused, failed, or disputed run.
5. Expire public cache entries by type. Revalidation replaces an index pointer
   with a new immutable object; it never mutates content used by an application.
6. Archive completed job workspaces by year and month while preserving registry
   pointers and deduplication keys.

Cleanup must never erase the only application receipt, evidence provenance, or
artifact needed to reproduce what was submitted.
