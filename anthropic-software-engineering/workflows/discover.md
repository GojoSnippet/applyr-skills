# Discover Anthropic engineering roles

Read `knowledge/roles.md`, then inspect the configured Anthropic careers
board at `https://job-boards.greenhouse.io/anthropic` (or its underlying
Greenhouse job-board API/feed, if one can be read without a browser).

Return only current postings that:

- belong to Anthropic on `job-boards.greenhouse.io/anthropic` exactly;
- are software/research-engineering roles (see `knowledge/roles.md` for the
  allowed title patterns) — not research-scientist, policy, comms, legal, or
  business-operations postings that share the same board;
- meet the configured location and `discover_from` constraints — most
  postings list multiple offices (e.g. "San Francisco, CA | New York City,
  NY | Seattle, WA") or are explicitly Remote-Friendly; treat any listed
  location as satisfying the configured constraint if the posting is
  otherwise eligible;
- have a canonical Anthropic (Greenhouse) job URL.

Scan incrementally. Compare each posting's listed date against the stored
high-water mark (`discover_from`) for this board and skip postings published
before it. Before recording any posting that passes the date filter, check it
against the shared durable job database by canonical URL/job ID: a posting
that already exists there in any status is a duplicate and must not be
re-queued or re-classified, regardless of its date. After the scan, advance
the stored high-water mark to the newest posting date observed.

Classify each observed role once:

- `match`: title, company, date, and configured constraints fit an
  engineering role from `knowledge/roles.md`'s allowed patterns;
- `review`: a title needs judgment — e.g. a "Research Engineer, X" posting
  where X reads more research-scientist than engineering, or an "Anthropic
  Fellows Program" posting (a fellowship/mentorship track, not a standard
  engineering hire — route to review rather than auto-matching or
  auto-rejecting);
- `no_match`: wrong function (research scientist, policy, go-to-market,
  legal, recruiting, and similar), employer, seniority, location, or date.

No bot-check was observed on this board at verification time. If one ever
blocks reading the listing, stop and report the source as unreadable — never
attempt to solve or bypass it.
