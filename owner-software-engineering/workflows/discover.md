# Discover Owner.com engineering roles

Read `knowledge/roles.md`, then inspect the configured Owner.com careers page
at `https://jobs.ashbyhq.com/Owner` (or its underlying job-board feed).

Return only current postings that:

- belong to Owner.com at `owner.com`, hosted on `jobs.ashbyhq.com/Owner`
  exactly;
- are Software Engineer or Senior Software Engineer roles;
- meet the configured location and `discover_from` constraints;
- have a canonical Owner/Ashby job URL.

Scan incrementally. Compare each posting's `published_at` against the stored
high-water mark (`discover_from`) for this board and skip postings published
before it. Before recording any posting that passes the date filter, check it
against the shared durable job database by canonical URL/job ID: a posting
that already exists there in any status is a duplicate and must not be
re-queued or re-classified, regardless of its `published_at`. After the scan,
advance the stored high-water mark to the newest `published_at` observed.

Classify each observed role once:

- `match`: title, company, date, and configured constraints fit;
- `review`: a potentially relevant engineering title needs judgment;
- `no_match`: wrong function, employer, seniority, location, or date.

Queue only new `match` records that passed both the `published_at` filter and
the durable duplicate check. Never hand off a job that is already queued,
claimed, applying, submitted, failed, or skipped. Hand only newly queued jobs
downstream. Finish with the counts and the canonical URLs observed in this
scan.
