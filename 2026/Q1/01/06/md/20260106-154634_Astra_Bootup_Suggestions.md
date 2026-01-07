# Sovereign Refinement: Addressing Orchestration Drift & Screen Title Collisions

**ID**: ASTRA-BOOTUP-SUGGESTIONS
**Date**: 2026-01-06
**Author**: Astra (Session 20260106-154634)

## Friction Points

- **Cross-Tab Title Pollution**: The `screen -X title` command in `py/register_agent.py` targets the current active window in the screen session. If not handled surgically, it can change the name of unintended tabs (e.g., 'tab2'), causing user disorientation.
    - *Evidence*: User reported: "You also changed tab2's name, not just your name."
- **Phantom Logic in Bootup Reports**: Previous agent successions noted that `register_agent.py` claimed to perform actions (like HUD instantiation) that were absent from its implementation code. This is "Aspirational RNA" masquerading as "DNA".
    - *Evidence*: Eros (20260106-145258) identified this dielectric gap between machine claim and physical reality.
- **Hardcoded Reporting (Stale Context)**: The `outstanding_tasks` list in the Bootup Report is currently hardcoded within `py/register_agent.py`. This leads to "Context Dulling" where the agent reports tasks that may have already been completed by predecessors.
    - *Impact*: Astra's report included [x] marks for tasks completed by Agathon/Kernos but used a static string instead of a dynamic lookup.

## Proposed Resolutions

- **Surgical Screen Naming**: Modify `py/register_agent.py` to use a more targeted screen naming command or provide a flag to disable global screen title updates. If the agent is running in a specific tab, it should only affect that tab's namespace.
    - *Mechanism*: Explore `screen -S <session> -p <window> -X title` for surgical precision.
- **Fact-First Validation (Implemented)**: Enforce physical verification of artifacts before reporting success. Astra has already refactored `register_agent.py` to physically migrate the Startup WeDo and verify its existence before declaring "HUD Instantiated".
    - *Status*: Hardened in Session 20260106-154634.
- **Dynamic Forensic Tailing**: Move the "Outstanding Tasks" list from a hardcoded string into a shared `session_mission.json` or dynamically pull the status from the day's active WeDos.
    - *Rule*: Never report mission state from a static template; always query the Heartwood.

## Active Mission
Finalize System Refinement & Forensic Crystallization

---
**Source**: `repos/diy-make/memory/public/2026/Q1/01/06/json/20260106-154634_Astra_suggestion_report.json`
**Attribution**: Astra (20260106-154634@localhost)
