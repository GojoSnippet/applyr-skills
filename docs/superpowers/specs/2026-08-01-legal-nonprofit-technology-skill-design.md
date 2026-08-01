# Legal Nonprofit Technology Application Skill

**Status:** approved with candidate-evidence amendment, 2026-08-01

## 1. Outcome

Create one reusable skill for finding and applying to technology roles at
legally registered US nonprofits, NGOs, foundations, nonprofit universities,
research institutes, and nonprofit hospital systems. Optimize for interview
probability, not application count. Process every role that passes the quality
gates; use concurrency and portal-rate limits only for correctness and safety.

The skill complements Applyr's durable runtime. Applyr continues to own leases,
duplicate prevention, browser isolation, submission idempotency, private
artifacts, and event history. The skill owns vertical strategy, evidence
construction, job research, tailoring, review, and workspace hygiene.

## 2. Candidate evidence model

The source resume is an index, not the boundary of the candidate's knowledge.
Build a private, versioned candidate evidence graph from:

- resume and existing career documents;
- repositories, code, architecture, tests, commit history, and project docs;
- employment and project context supplied by the candidate;
- prior application answers that the candidate supplied or corrected;
- public information about former employers, used only as context and never as
  proof that the candidate personally performed a task.

An agent may infer a demonstrated capability from authored work. It may not
infer an employer, title, date, metric, business result, production deployment,
team size, personal ownership, or regulated-domain experience without direct
evidence. Dependency files and repository boilerplate prove project exposure,
not personal mastery. Every proposed claim records its evidence references and
one of these publication states:

- `publishable`: safe to use in applications;
- `private_context`: useful for reasoning but not safe to disclose;
- `needs_confirmation`: plausible but insufficiently supported;
- `prohibited`: never use.

New evidence may be added incrementally. The user does not need to enumerate a
lifetime of work before the system becomes useful.

## 3. Workspace and isolation

Use `/Users/sai/Developer/work/nonprofit-job-search` as the runtime workspace.

```text
candidate/                     private, versioned evidence graph and source files
registry/                      canonical employers, jobs, applications, receipts
organizations/<org-key>/       legal proof and reusable public organization dossier
jobs/<job-key>/intake/         immutable job snapshot and identifiers
jobs/<job-key>/research/       role-specific research and evidence matrix
jobs/<job-key>/drafts/         job-specific resume, letter, and answer drafts
jobs/<job-key>/review/         truth, ATS, voice, consistency, and render reports
jobs/<job-key>/final/          submission-ready artifacts only
jobs/<job-key>/proof/          confirmation page, receipt, and submitted answers
jobs/<job-key>/state.json      durable workflow state and input versions
cache/public/                  reusable content-addressed public inputs only
scratch/<run-id>/              disposable intermediate files with retention TTL
archive/<year>/<month>/        completed job packages
logs/                          redacted operational logs
```

One job workspace is mounted read-write into a job run. Other job workspaces
are not mounted. Candidate evidence and organization dossiers are mounted
read-only. Job-specific prose, rankings, keyword lists, and tailored artifacts
must never enter shared cache.

## 4. Cache contract

Cache only public, reusable inputs: source result pages, job-page snapshots,
organization research, legal-status evidence, and ATS/platform documentation.
Keys include canonical URL or organization identity, content hash, retrieval
date, extractor version, and skill version. A changed job description creates
a new immutable version.

Candidate evidence uses a private version hash rather than the public cache.
Each job state records the exact candidate, job-description, organization, and
skill versions used. Cached material has type-specific freshness limits and is
revalidated before submission when it can affect eligibility or legal status.

Scratch is retained briefly for debugging, then removed by TTL. Final artifacts,
review reports, evidence provenance, and submission proof are durable. Raw page
captures follow the private-history retention policy and never enter logs.

## 5. Employer and job boundary

An employer passes only when its legal nonprofit status is supported by an
authoritative record or by reliable official evidence for entities that do not
map cleanly to a US 501(c) record. A mission statement alone is insufficient.
For fiscal-sponsorship arrangements, record both the project and legal sponsor.

Primary discovery sources include Idealist, Fast Forward Tech Nonprofit, NTEN,
National Council of Nonprofits and state associations, Council on Foundations,
Work for Good, National Nonprofits, NPO.net, and direct organization career/ATS
pages. Broader social-impact sources may supply leads only; the employer still
must pass legal verification.

## 6. Job strategy

Score jobs on mandatory eligibility, demonstrated capability, role trajectory,
location/remote fit, compensation when available, mission interest, recency,
and tailoring leverage. Reject jobs with failed hard requirements. Research and
apply to every remaining role whose expected value justifies the work.

There is no daily application quota and no artificial minimum. Parallelize
research and drafting when isolated, but serialize applications for the same
employer and preserve Applyr's duplicate, budget, and browser-capacity controls.

## 7. Tailoring and automatic review

Tailoring may substantially reorganize and rewrite the resume when supported by
the candidate evidence graph. It must preserve factual identity and avoid
keyword stuffing or synthetic corporate language. The default output uses the
JakeResume layout and must be a visually complete one- or two-page document;
half-empty pages, clipped text, tiny type, and unexplained removal of strong
evidence fail review.

Every final package must pass:

1. evidence/provenance review;
2. must-have and important-keyword coverage review;
3. job-level and cross-artifact consistency review;
4. human-voice and specificity review;
5. rendered PDF layout and text-extraction review;
6. form-answer and attachment review immediately before submission.

Do not claim a magic ATS percentage. Report matched requirements, missing
requirements, risky claims, and layout defects directly.

## 8. Durable lifecycle

The lifecycle is `discovered -> verified -> scored -> researched -> drafted ->
reviewed -> applying -> submitted -> follow_up`, with explicit rejected,
blocked, withdrawn, and expired terminal states. Duplicate checks occur before
research, before claiming an application run, and inside the final submission
tool. A submission is complete only when proof or a stable receipt is stored.

## 9. Skill package

Create `legal-nonprofit-technology/` with a concise root `SKILL.md`, focused
workflows for discovery, evidence building, research, tailoring, review,
application, and cleanup, and references for the workspace contract, candidate
evidence schema, source strategy, and quality gates. Organization knowledge is
runtime data, not copied into the public skill.

## 10. Acceptance cases

The skill must correctly handle:

- a strong project capability absent from the source resume;
- a dependency that must not be misrepresented as expert experience;
- confidential work that may inform matching but may not be published;
- two simultaneous jobs without cross-contamination;
- a reposted role and a changed job description;
- a mission-driven for-profit that must be rejected;
- a sparse tailored resume that must fail render review;
- an application without a confirmation receipt that must remain unverified.
