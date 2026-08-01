# Discover and qualify roles

Read `references/source-strategy.md`, `references/workspace-contract.md`, and
`references/state-and-deduplication.md`.

1. Search the configured source tiers and direct organization career pages.
2. Normalize employer, title, location, compensation, source posting id,
   canonical URL, posted time, description, and application URL.
3. Resolve the organization identity. Verify legal nonprofit status before
   advancing the role; retain the authoritative evidence, retrieval date, and
   fiscal sponsor when applicable.
4. Snapshot the exact job description. Compute a content hash; never overwrite
   an older snapshot when the content changed.
5. Reconcile the durable registry using source id, canonical URL, organization,
   requisition id, and normalized title/location fingerprints.
6. Apply hard eligibility gates: US location or accepted remote arrangement,
   work authorization, sponsorship requirement, required credentials, and
   clearly mandatory experience.
7. Score surviving roles on demonstrated capability, trajectory, recency,
   location, compensation, mission interest, and tailoring leverage.
8. Queue every worthwhile role. Do not manufacture a target count and do not
   reject a strong role merely because a daily quota was reached.

Cache only public source inputs under the workspace contract. Discovery output
must never include job-specific prose from another application.
