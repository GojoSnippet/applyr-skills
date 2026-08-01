# Complete one application

Read `references/workspace-contract.md`, `references/candidate-evidence.md`,
`references/quality-gates.md`, and `references/state-and-deduplication.md`.

1. Atomically claim the exact job and verify the run owns its lease and one job
   workspace. Check that no submitted or active duplicate exists.
2. Open the authoritative company application page. Respect platform terms,
   authentication boundaries, and runtime automation settings.
3. Observe before acting. Fill from the reviewed package and current candidate
   evidence; read back each write where supported.
4. Answer humanly, directly, and specifically. Use only publishable evidence.
   Do not disguise unknowns with plausible prose.
5. Treat voluntary demographic responses as the candidate's stored choice,
   never as an inference. Pause if a required personal choice is absent.
6. Upload artifacts from this job's `final/` directory only. Rerun readiness
   review if the live form differs materially from the saved snapshot.
7. Call the final submission tool only after all quality gates pass and the
   runtime's lease, domain, duplicate, budget, and platform controls permit it.
8. Capture the resulting confirmation page, message, application id, or stable
   receipt. If no proof is observed, keep state `submission_unverified`, inspect
   portal history or email when authorized, and never blindly click submit
   again.
9. Save submitted answers and artifacts under `proof/`, transition durable
   state, release the lease, and schedule follow-up when appropriate.

CAPTCHA, unavailable authentication, contradictory required facts, or a portal
that prohibits the configured automation are real blockers; record them rather
than routing around them.
