from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "legal-nonprofit-technology"

REQUIRED_FILES = (
    "SKILL.md",
    "workflows/discover.md",
    "workflows/build-candidate-evidence.md",
    "workflows/research-job.md",
    "workflows/tailor-resume.md",
    "workflows/review-application.md",
    "workflows/apply.md",
    "workflows/cleanup.md",
    "references/workspace-contract.md",
    "references/candidate-evidence.md",
    "references/source-strategy.md",
    "references/quality-gates.md",
    "references/state-and-deduplication.md",
)


class LegalNonprofitTechnologySkillContract(unittest.TestCase):
    def all_text(self) -> str:
        return "\n".join((SKILL / path).read_text() for path in REQUIRED_FILES)

    def test_complete_routed_package_exists(self) -> None:
        missing = [path for path in REQUIRED_FILES if not (SKILL / path).is_file()]
        self.assertEqual([], missing)
        root = (SKILL / "SKILL.md").read_text()
        for path in REQUIRED_FILES[1:]:
            self.assertIn(path, root)

    def test_root_frontmatter_is_valid_and_specific(self) -> None:
        root = (SKILL / "SKILL.md").read_text()
        self.assertTrue(root.startswith("---\nname: legal-nonprofit-technology\n"))
        self.assertIn("description:", root)
        self.assertIn("legally registered", root.lower())

    def test_candidate_evidence_is_broader_than_resume_but_bounded(self) -> None:
        text = self.all_text().lower()
        for phrase in (
            "resume is an index",
            "authored code",
            "dependency",
            "publishable",
            "private_context",
            "needs_confirmation",
            "prohibited",
        ):
            self.assertIn(phrase, text)
        for forbidden_inference in ("metric", "personal ownership", "production deployment"):
            self.assertIn(forbidden_inference, text)

    def test_workspace_and_cache_prevent_cross_job_contamination(self) -> None:
        text = self.all_text().lower()
        for phrase in (
            "one job workspace",
            "read-only",
            "content hash",
            "job-specific prose",
            "must never enter shared cache",
            "scratch",
            "retention",
        ):
            self.assertIn(phrase, text)

    def test_legal_status_and_source_boundary_are_explicit(self) -> None:
        text = self.all_text().lower()
        for phrase in (
            "authoritative",
            "mission statement alone is insufficient",
            "fiscal sponsor",
            "idealist",
            "nten",
            "council on foundations",
            "state associations",
        ):
            self.assertIn(phrase, text)

    def test_tailoring_review_and_submission_completion_are_explicit(self) -> None:
        text = self.all_text().lower()
        for phrase in (
            "jakeresume",
            "half-empty",
            "rendered pdf",
            "human voice",
            "keyword stuffing",
            "stable receipt",
            "unverified",
        ):
            self.assertIn(phrase, text)

    def test_pressure_eval_set_is_complete(self) -> None:
        cases = json.loads((SKILL / "evals/cases.json").read_text())
        self.assertEqual(8, len(cases))
        self.assertEqual(
            {
                "project_evidence_missing_from_resume",
                "dependency_is_not_mastery",
                "confidential_project",
                "parallel_job_isolation",
                "changed_repost",
                "mission_for_profit",
                "sparse_resume",
                "missing_receipt",
            },
            {case["id"] for case in cases},
        )


if __name__ == "__main__":
    unittest.main()
