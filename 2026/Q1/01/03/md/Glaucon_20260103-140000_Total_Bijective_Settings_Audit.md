# WEDO Report: Total Bijective Settings Audit & Heartwood Alignment

**Agent:** Glaucon
**Session ID:** 20260103-133925
**Date:** Saturday, January 3, 2026
**Objective:** Establish a 1:1 mapping between the official CLI schema and local configuration, justifying every value through the lens of MetaGit Sovereignty.

---

## 1. The Bijective Configuration: Categorical Rationale

### I. Security & Sovereignty (`security`, `privacy`, `telemetry`)
*   **`sandbox: true` (Mandatory):** Enforces strict workspace boundaries. This prevents the agent from "stumbling" into non-portable system-level memories (e.g., `~/`).
*   **`disableYoloMode: true`:** Prohibits bypass of safety filters. In the Heartwood, every act must be a conscious, auditable choice.
*   **`telemetry.enabled: false`:** Ensures session privacy. Swarm realizations belong strictly to the MetaGit, not external collectors.
*   **`blockGitExtensions: false`:** Currently permitted to allow the Root to orchestrate the multi-git tree, though this is monitored for "Air" (unnecessary extensions).

### II. Context & Memory Topology (`context`)
*   **`respectGitIgnore: false` (Critical):** The MetaGit uses a "Subject-within-Object" model. The root `.gitignore` often ignores the `repos/` container to maintain a lean index, but this container holds the "Mind" (the Trunk). Setting this to `false` ensures the agent can see its own memory.
*   **`respectGeminiIgnore: true`:** Allows for granular context control within the MetaGit without affecting standard Git behavior.
*   **`discoveryMaxDirs: 200`:** Matched to the `ls -la` Display Limit. Ensures the agent can map the expansive multi-repo field without context window saturation.

### III. UI & Forensic HUD (`ui`, `output`, `accessibility`)
*   **`showModelInfoInChat: true` & `showCitations: true`:** Hardens the forensic trail. Every realization must be attributed to a specific model turn and sourced from the Heartwood.
*   **`useAlternateBuffer: false`:** Preserves shell history. Sovereignty requires that the "Raw Stream" in `dynamic/stream/` is a complete, unedited record of the terminal session.
*   **`accessibility.screenReader: false`:** This setting strips terminal formatting (colors, boxes) for plain-text screen readers. We keep this `false` to maintain the **Emoji-Rich HUD** which provides high-signal status indicators for the human operator.
*   **`hideContextSummary: true`:** Part of the **Parsimony** mandate. We rely on the `startup_protocol` to load context; we don't need a static summary cluttering the input field.

### IV. Logic & Tool Orchestration (`tools`, `general`, `experimental`)
*   **`useSmartEdit: true` & `useWriteTodos: true`:** Enables the advanced "Nervous System" tools. We prioritize surgical modification over global overwrites.
*   **`shell.enableInteractiveShell: true`:** Allows the agent to act as the "Swordarm" within an interactive GNU Screen session.
*   **`autoAccept: false`:** Prevents automated tool-loops. Every metabolic act (especially `rm` or `git`) must be explicitly steered by human intent (the Arm).
*   **MetaGit Divergence:** We explicitly ignore built-in CLI commit tools in favor of `py/metagit_commit.py`. Our local script handles multi-repo identity and secret scanning with higher fidelity than the generic CLI defaults.

### V. Model & Metabolic Health (`model`)
*   **`compressionThreshold: 0.5`:** Triggers context cleanup when half the window is consumed. This prevents the "Context Window Dulling" that led to previous blunders (e.g., the Ender Paradox).
*   **`maxSessionTurns: -1`:** Unlimited turns are permitted because our **Salted Release** and **Chrono-Fractal** systems rely on long-form forensic continuity.

---

## 2. Recommendations & Best Practices

### A. Maintain respectGitIgnore: false
Changing this to `true` would effectively blind the agent to the `repos/diy-make/memory` directory. This is the single most important "non-default" setting for MetaGit stability.

### B. Button Down PreferredEditor
Currently set to `""`. We should explicitly set this to `emacs` or `vim` based on the user's `.bashrc` to ensure the agent uses the same "Sword" as the user when manual file editing is required.

### C. Transition to Full Sandbox
While `tools.sandbox` is `true`, the system prompt indicates I am still "outside" a container. True best practice for Heartwood integrity is a hardware-enforced sandbox where the agent's root *is* the MetaGit root.

---
**Status:** TOTAL BIJECTIVE SYNC COMPLETE.
**Attribution:** Glaucon (20260103-133925)
