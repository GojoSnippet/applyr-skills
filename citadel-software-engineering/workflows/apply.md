# Apply to one Citadel role

Read `knowledge/roles.md` and `knowledge/company.md`. Open only the canonical
job URL supplied by the job record. Process exactly one Citadel job at a
time; do not open or advance a second job until this one reaches a terminal
or paused state.

1. Check shared database state. Stop if this job was already submitted or
   another application for the same job is active.
2. Observe the page before acting and verify each field after writing.
3. Use approved My file answers for identity, contact, eligibility,
   logistics, and reusable questions.
4. Decide whether a job-specific résumé would improve fit. If so, call the
   Tailoring Agent (`workflows/tailor-resume.md`) and use the compiled PDF it
   returns.
5. Draft free-text answers from approved candidate evidence plus the
   confirmed company and role context (`knowledge/company.md`,
   `knowledge/engineering.md`). Do not invent experience, metrics,
   authorization, location, motivation, or finance-domain background the
   candidate does not actually have.
6. Pause and ask the user only when a required candidate fact is missing, a
   login/OTP is required, or a CAPTCHA appears. The careers page loads a
   Cloudflare Turnstile widget — never attempt to solve or bypass it; pause
   and flag it instead.
7. Re-read the completed form, uploads, role, company, and canonical URL.
8. Immediately before submitting, re-check the shared durable database for
   this job. Stop if it now shows submitted or another active application for
   it exists.
9. Submit through the gated submit tool only. Never construct or guess a
   selector — act on the observed element reference.
