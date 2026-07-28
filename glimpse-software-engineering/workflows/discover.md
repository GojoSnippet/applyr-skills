# Discover Glimpse engineering roles

Read `knowledge/roles.md`, then inspect the configured Glimpse careers page.

Return only current postings that:

- belong to Glimpse at `tryglimpse.com`;
- are Software Engineer or Senior Software Engineer roles;
- meet the configured location and `discover_from` constraints;
- have a canonical Glimpse/Ashby job URL.

Use the shared job database before recording a posting. Classify each observed
role once:

- `match`: title, company, date, and configured constraints fit;
- `review`: a potentially relevant engineering title needs judgment;
- `no_match`: wrong function, employer, seniority, location, or date.

Queue only new `match` records. Never hand off a job that is already queued,
claimed, applying, submitted, failed, or skipped. Finish with the counts and the
canonical URLs observed in this scan.
