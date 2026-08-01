# Legal Nonprofit Technology Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and validate a reusable skill plus an isolated operational workspace for nationwide US legal-nonprofit technology applications.

**Architecture:** A concise root skill routes to focused workflows and reference contracts. Applyr retains durable execution and submission controls; the skill governs vertical strategy and per-job behavior. Public reusable inputs use a content-addressed cache, while each job receives a private workspace and evidence-version manifest.

**Tech Stack:** Markdown Agent Skill package, JSON eval fixtures, Python 3 standard-library contract tests, Applyr runtime contracts.

## Global Constraints

- Optimize for interview probability rather than application volume.
- Target only legally nonprofit employers, including qualifying NGOs, foundations, nonprofit universities, research institutes, and nonprofit hospital systems.
- Infer demonstrated capability from attributable work, but never invent identity, dates, metrics, outcomes, ownership, deployment, or domain experience.
- Never publish `private_context`, `needs_confirmation`, or `prohibited` evidence.
- Mount exactly one job workspace read-write; candidate and organization evidence remain read-only.
- Never place job-specific prose or tailored artifacts in shared cache.
- Use JakeResume and reject sparse, clipped, unreadable, or inconsistent output.
- A submission is complete only when durable proof or a stable receipt exists.

---

### Task 1: Behavioral and structural skill contracts

**Files:**
- Create: `legal-nonprofit-technology/evals/cases.json`
- Create: `tests/test_legal_nonprofit_technology_skill.py`

**Interfaces:**
- Consumes: the approved design specification.
- Produces: deterministic package-structure checks and eight pressure-case definitions used during skill review.

- [ ] **Step 1: Create pressure cases covering hidden project experience, dependency overclaiming, confidential evidence, cross-job contamination, changed reposts, for-profit rejection, sparse resumes, and missing receipts.**

- [ ] **Step 2: Add a standard-library test that requires the root skill, all routed workflows/references, workspace prohibitions, evidence publication states, legal verification, PDF review, and receipt verification.**

- [ ] **Step 3: Run the contract before implementation.**

Run: `python3 -m unittest tests/test_legal_nonprofit_technology_skill.py -v`

Expected: FAIL because `legal-nonprofit-technology/SKILL.md` and its routed files do not exist.

### Task 2: Skill package

**Files:**
- Create: `legal-nonprofit-technology/SKILL.md`
- Create: `legal-nonprofit-technology/workflows/discover.md`
- Create: `legal-nonprofit-technology/workflows/build-candidate-evidence.md`
- Create: `legal-nonprofit-technology/workflows/research-job.md`
- Create: `legal-nonprofit-technology/workflows/tailor-resume.md`
- Create: `legal-nonprofit-technology/workflows/review-application.md`
- Create: `legal-nonprofit-technology/workflows/apply.md`
- Create: `legal-nonprofit-technology/workflows/cleanup.md`
- Create: `legal-nonprofit-technology/references/workspace-contract.md`
- Create: `legal-nonprofit-technology/references/candidate-evidence.md`
- Create: `legal-nonprofit-technology/references/source-strategy.md`
- Create: `legal-nonprofit-technology/references/quality-gates.md`
- Create: `legal-nonprofit-technology/references/state-and-deduplication.md`

**Interfaces:**
- Consumes: task kind, exact job snapshot, organization dossier, candidate evidence version, and Applyr job/run identifiers.
- Produces: verified leads, evidence-backed artifacts, review reports, submission receipts, and deterministic terminal state.

- [ ] **Step 1: Implement the root routing and non-negotiable isolation, truth, nonprofit-status, and completion rules.**

- [ ] **Step 2: Implement discovery, candidate-evidence, research, tailoring, review, application, and cleanup workflows.**

- [ ] **Step 3: Implement reference contracts for workspace/cache, evidence states, source tiers, quality gates, and durable deduplication.**

- [ ] **Step 4: Run package validation.**

Run: `python3 /Users/sai/.codex/skills/.system/skill-creator/scripts/quick_validate.py legal-nonprofit-technology`

Expected: `Skill is valid!`

- [ ] **Step 5: Run the behavioral and structural contracts.**

Run: `python3 -m unittest tests/test_legal_nonprofit_technology_skill.py -v`

Expected: all tests pass.

### Task 3: Operational workspace and handoff

**Files:**
- Create: `/Users/sai/Developer/work/nonprofit-job-search/README.md`
- Create: `/Users/sai/Developer/work/nonprofit-job-search/candidate/README.md`
- Create: `/Users/sai/Developer/work/nonprofit-job-search/registry/README.md`
- Create: `/Users/sai/Developer/work/nonprofit-job-search/cache/README.md`
- Create: `/Users/sai/Developer/work/nonprofit-job-search/scratch/README.md`
- Modify: `README.md`

**Interfaces:**
- Consumes: the workspace contract from Task 2.
- Produces: a stable local root that Applyr runs can populate without mixing applications.

- [ ] **Step 1: Create the runtime directories and document ownership, retention, and prohibited content for each shared area.**

- [ ] **Step 2: Update the skill repository README with the new package purpose and runtime path.**

- [ ] **Step 3: Run the skill validator and contract suite again from a clean command invocation.**

Run: `python3 /Users/sai/.codex/skills/.system/skill-creator/scripts/quick_validate.py legal-nonprofit-technology && python3 -m unittest tests/test_legal_nonprofit_technology_skill.py -v`

Expected: validator succeeds and all contracts pass.

- [ ] **Step 4: Inspect `git diff --check` and `git status --short` before reporting completion.**
