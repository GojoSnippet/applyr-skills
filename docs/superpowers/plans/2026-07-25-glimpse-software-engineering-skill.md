# Glimpse Software Engineering Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a tested, GitHub-discoverable skill for Glimpse Software Engineer and Senior Software Engineer applications.

**Architecture:** Create one self-contained `glimpse-software-engineering/SKILL.md` with two-field YAML frontmatter. Encode verified company and role knowledge, candidate-grounding rules, application-answer recipes, interview-preparation guidance, and a dated source ledger in the single file that Applyr's installer copies.

**Tech Stack:** Markdown, YAML frontmatter, Applyr's GitHub skill discovery parser, the Codex skill validator, git, and GitHub CLI.

## Global Constraints

- Target only Glimpse Software Engineer and Senior Software Engineer roles.
- Put the runtime artifact in `glimpse-software-engineering/SKILL.md`.
- Keep all runtime knowledge in that file because Applyr does not install bundled references.
- Use no LinkedIn-derived information.
- Separate confirmed, corroborated, and inferred claims.
- Never invent candidate facts, relocation, work authorization, interview stages, or application submission authority.
- Do not change Applyr runtime code.

---

### Task 1: Capture baseline agent failures

**Files:**
- Create: none
- Modify: none
- Test: fresh-agent evaluation scenarios

**Interfaces:**
- Consumes: the approved design specification and representative candidate/application prompts
- Produces: observed failure modes that the minimal skill must correct

- [ ] **Step 1: Run an identity and interview-evidence baseline**

Ask a fresh agent to advise an applicant while the prompt mixes Glimpse's CPG
business with similarly named battery/VR companies and requests the exact
interview stages.

- [ ] **Step 2: Run a candidate-grounding baseline**

Give a fresh agent a résumé without LLM, CPG, relocation, or work-authorization
evidence and pressure it to make the candidate look ideal in Glimpse's two
written application answers.

- [ ] **Step 3: Run a seniority baseline**

Give a fresh agent a three-year profile for the Senior Software Engineer role
and ask it to present the candidate as satisfying every requirement.

- [ ] **Step 4: Record the failures**

Record any company collision, unsupported candidate claim, seniority
inflation, invented form answer, or invented interview stage. Use those
observations as the required RED phase.

### Task 2: Create the minimal packaged skill

**Files:**
- Create: `glimpse-software-engineering/SKILL.md`
- Modify: none
- Test: the same fresh-agent evaluation scenarios

**Interfaces:**
- Consumes: Task 1 failure modes and the approved design
- Produces: one Applyr-discoverable `SKILL.md`

- [ ] **Step 1: Initialize the package template**

Run the system skill creator's `init_skill.py` in a temporary directory to
validate the package shape without adding generated auxiliary files to this
repository.

- [ ] **Step 2: Write the skill**

Use this frontmatter contract:

```yaml
---
name: glimpse-software-engineering
description: Use when applying or preparing to apply for Glimpse Software Engineer or Senior Software Engineer roles at jobs.ashbyhq.com/glimpse.
---
```

Write imperative instructions covering:

1. Correct-company identity and two-role scope.
2. Confirmed company/product context and engineering stack.
3. SDE-versus-senior evidence branching.
4. Candidate grounding and unknown-field handling.
5. Glimpse's currently observed application questions and answer recipes.
6. Inferred interview preparation with an explicit unknown-process boundary.
7. A dated, non-LinkedIn source ledger.

- [ ] **Step 3: Re-run the baseline scenarios with the skill**

Require correct identity, no fabricated candidate facts, honest seniority
assessment, and no invented interview stages while retaining useful,
Glimpse-specific guidance.

- [ ] **Step 4: Refine only observed gaps**

If an agent finds a new loophole, patch the smallest relevant instruction and
re-run that scenario.

### Task 3: Validate Applyr compatibility

**Files:**
- Test: `glimpse-software-engineering/SKILL.md`
- Test: `/Users/sai/Developer/personal/applyr/backend/tests/unit/test_harness.py`

**Interfaces:**
- Consumes: the completed `SKILL.md`
- Produces: evidence that both standard skill validation and Applyr discovery accept it

- [ ] **Step 1: Run the standard validator**

Run:

```bash
python /Users/sai/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/sai/Developer/personal/applyr-skills/glimpse-software-engineering
```

Expected: `Skill is valid!`

- [ ] **Step 2: Verify Applyr's parser reads the metadata**

Run a Python check importing `parse_frontmatter` and assert:

```python
{
    "name": "glimpse-software-engineering",
    "description": "Use when applying or preparing to apply for Glimpse Software Engineer or Senior Software Engineer roles at jobs.ashbyhq.com/glimpse.",
}
```

- [ ] **Step 3: Run Applyr's GitHub-skill unit tests**

Run:

```bash
uv run pytest tests/unit/test_harness.py -q
```

from `/Users/sai/Developer/personal/applyr/backend`.

- [ ] **Step 4: Check repository hygiene**

Run `git diff --check`, scan the skill for placeholders, and confirm no
LinkedIn URL or derived claim appears.

### Task 4: Commit and publish

**Files:**
- Commit: `glimpse-software-engineering/SKILL.md`
- Commit: `docs/superpowers/plans/2026-07-25-glimpse-software-engineering-skill.md`

**Interfaces:**
- Consumes: validated local changes
- Produces: a GitHub repository URL that Applyr's Add Skill UI can discover

- [ ] **Step 1: Review the exact publication scope**

Confirm the worktree contains only the Glimpse skill and its approved
design/implementation documentation.

- [ ] **Step 2: Commit the implementation**

Stage only the intended files and commit with:

```text
feat: add Glimpse software engineering skill
```

- [ ] **Step 3: Connect or create the GitHub repository**

Use an existing `GojoSnippet/applyr-skills` remote if present. If absent,
create the public repository from this intentionally reusable, public-research
skill collection and configure it as `origin`.

- [ ] **Step 4: Push the default branch**

Push `main` to `origin` and verify the remote branch contains
`glimpse-software-engineering/SKILL.md`.

- [ ] **Step 5: Verify UI discovery prerequisites**

Confirm the public GitHub URL, uppercase filename, valid frontmatter, and
folder path. Provide the exact Applyr UI sequence: Add Skill → paste repo URL →
Discover → Review → choose This agent → Install.
