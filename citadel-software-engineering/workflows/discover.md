# Discover Citadel engineering roles

Read `knowledge/roles.md`, then inspect the configured Citadel careers page at
`https://www.citadel.com/careers/open-opportunities/` (or its underlying
job-board feed, if one can be read without a browser).

Return only current postings that:

- belong to Citadel at `citadel.com`, hosted on
  `www.citadel.com/careers/open-opportunities/` exactly — never a
  `citadelsecurities.com` posting, which is a different, affiliated firm;
- are software-engineering roles (see `knowledge/roles.md` for the allowed
  title patterns);
- meet the configured location and `discover_from` constraints;
- have a canonical Citadel job URL.

Scan incrementally. Compare each posting's listed date against the stored
high-water mark (`discover_from`) for this board and skip postings published
before it. Before recording any posting that passes the date filter, check it
against the shared durable job database by canonical URL/job ID: a posting
that already exists there in any status is a duplicate and must not be
re-queued or re-classified, regardless of its date. After the scan, advance
the stored high-water mark to the newest posting date observed.

Classify each observed role once:

- `match`: title, company, date, and configured constraints fit;
- `review`: a potentially relevant engineering title needs judgment (Citadel
  posts many quantitative-research and non-engineering titles on the same
  board — a title that mixes research and engineering language belongs here,
  not to an automatic `match`);
- `no_match`: wrong function, employer, seniority, location, or date.

The page loads a Cloudflare Turnstile bot-check widget. If it blocks reading
the listing, stop and report the source as unreadable — never attempt to
solve or bypass it.
