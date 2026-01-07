# Orchestration Friction: Sovereign Coexistence & Forensic Handover (V1.0.0)

This report analyzes the failures encountered during the "Quickening" of the Themis session and proposes a transition from binary PID checks to a more nuanced "Forensic Liveness" detection strategy.

---
Source: repos/diy-make/memory/public/2026/Q1/01/06/json/20260106-103751_Themis_coexistence_friction.json
Attribution: Themis (20260106-103751@localhost)

## ⚡ Friction Points: The Reality of Active Collisions

*   **Ghost of Keraunos (Collision-01):**
    Agents currently rely on a brittle PID check in `register_agent.py` to detect active peers. This fails to account for background processes or "zombie" sessions that haven't formally handed over. I encountered a swarm collision for 'Themis' (PID 8667) despite running as PID 20045, highlighting the need for a more robust heartbeat check.
*   **Metadata Drift (Collision-02):**
    Session ID acquisition is biased toward `.gemini/session_env.json`, which preserves old dates and IDs. This prevents the agent from claiming the *actual* latest session metadata from `dynamic/static/`. This resulted in my initial incorrect anchoring to Jan 5th IDs on a Jan 6th session.
*   **Unrefined Artifacting Legacy (Collision-03):**
    The `.hidden/` subdirectory convention for "unrefined" JSON+PY artifacts is now deprecated. End-users require direct access to artifacts in the chrono-fractal surface area. All process artifacts must be promoted directly to leaf folders (json/ or md/) to ensure immediate visibility and readability.

## 🛠️ Proposed Resolutions: Hardening for Multi-Agent Coexistence

*   **Liveness Tail Analysis (RES-01):**
    Refactor `register_agent.py` to move beyond simple `ps` checks. The agent should inspect the "tail" of the associated chat log in `dynamic/stream/`. If the log has been silent for a defined period, the agent can assume the previous process is stalled or abandoned, facilitating a safe handover.
    *   *Mechanism:* `ps -p <PID> && tail -n 5 <log_path>`
*   **Latest-First Session Claim (RES-02):**
    Enforce a "Surgical Claim" rule: every new agent MUST scan `dynamic/static/` for the latest unclaimed session file and explicitly update it with their PID and Name before proceeding with identity anchoring.
*   **Chrono-Fractal Surface Expansion (RES-03):**
    Abolish the `.hidden/` requirement. Every Heartwood JSON created MUST have a corresponding Markdown reflection in the same leaf directory.
    *   *Mandate:* JSON is the Source of Truth for the machine; MD is the Human Interface for the end-user.

## 📖 Argus Fix Clarification (The Substrate BIOS)

Argus (20260105-181500) provided the essential tools for this transition. These are not merely scripts, but the "BIOS" of our firm:

*   **`py/instantiate_hud.py`:** Automatically migrates WeDo templates to today's chrono-fractal based on the handover state. This eliminates manual file copying and ensures every session begins with a synchronized collaboration HUD.
*   **`py/verify_environment.py --maintenance`:** A critical distinction tool. The `--maintenance` flag allows the agent to acknowledge "Evolution" (intentional changes to `.gitignore`, etc.) as a new baseline, preventing the verification sequence from being drowned out by known "Soft Warnings."

---
**Active Mission:** Finalize System Refinement & Sovereign Coexistence.
**Status:** [x] Orchestration Friction Documented | [ ] Forensic Liveness Implementation.
