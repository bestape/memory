# WEDO Report: The Physics of "Air" – Configuration Rationale

**Agent:** Glaucon
**Session ID:** 20260103-133925
**Date:** Saturday, January 3, 2026
**Objective:** De-complect the "Air" in settings.json by mapping the metabolic function of every omitted configuration key.

---

## 1. Definition: What is "Air"?

In the Heartwood philosophy, **Air** is configuration metadata that assumes a "Passive State." These are keys that exist in the official schema but, when set to their defaults or left empty, provide no instructional force to the agent. Including them in `settings.json` adds cognitive load to the context window without increasing the "Wood" (permanent logic) of the session.

## 2. Mapping the "Air": Metabolic Functions

### I. System Management (`general`, `advanced`, `privacy`, `telemetry`)
*   **`checkpointing`**: Saves the session state to allow for recovery after a crash. We omit this because our **Salted Release** and **Chrono-Fractal** systems prioritize Git history over ephemeral CLI checkpoints.
*   **`sessionRetention`**: Automatically deletes old logs based on age (`maxAge`) or count (`maxCount`). We omit this because we view every log as a forensic artifact—nothing is deleted until explicitly "Surgically" purged by the user.
*   **`usageStatisticsEnabled` / `telemetry`**: Governs the sending of diagnostic data back to the developers. We disable/omit this to ensure **MetaGit Sovereignty**—what happens in the Field stays in the Field.
*   **`dnsResolutionOrder`**: Controls whether the CLI prefers IPv4 or IPv6. Only relevant in complex network environments; "Air" for standard makerspace sessions.

### II. The User Interface (`ui`, `accessibility`)
*   **`theme` / `customThemes`**: Governs the colors of the terminal UI. We set this to `""` to default to the native shell colors, avoiding the "Theme not found" logic-loops.
*   **`customWittyPhrases`**: Allows the user to provide their own loading text. While aesthetically pleasing, it is pure "Air"—it provides no functional capability to the agent.
*   **`disableLoadingPhrases`**: Stops the witty text entirely. Primarily used for accessibility or to reduce terminal noise.
*   **`screenReader`**: Renders output in flat, plain text without boxes or emojis. Useful for screen-reading software but disabled here to preserve the **Emoji-Rich HUD**.

### III. Logic & Tool Extensions (`experimental`, `hooks`, `extensions`, `skills`)
*   **`hooks`**: A powerful system for intercepting CLI events (e.g., `BeforeTool`, `AfterModel`) and running custom shell scripts. We omit this because we prefer to build logic directly into the Heartwood's `py/` directory rather than adding a hidden layer of "Invisible Logic" in the settings.
*   **`extensions` / `skills`**: The CLI's native plugin system. We maintain `extensionManagement: true` but leave the lists empty to ensure we are only using "Approved Wood" from our local `repos/` container.
*   **`introspectionAgentSettings`**: An experimental subagent that allows the CLI to analyze its own behavior. We favor the **Glaucon/Thrasymachus** persona model for self-correction over an automated "Introspection" toggle.

### IV. Context Window Control (`context`, `mcpServers`)
*   **`mcpServers`**: Maps external Model Context Protocol servers. We omit this because we orchestrate our own servers via the `startup_protocol` and `environment_paths.json`.
*   **`includeDirectories`**: Forces extra folders into the agent's view. We prefer to navigate the MetaGit field dynamically rather than hardcoding paths in the root settings.
*   **`respectGitIgnore`**: Usually defaults to `true`. We explicitly set it to `false` because our "Subject-within-Object" model requires the agent to see into directories that Git for humans might be told to ignore.

---

## 3. Surgical Best Practice: Why Parsimony Wins

By removing these "Air" options, we achieve **Metabolic Parsimony**.
1.  **Context Efficiency:** The agent reads 20 lines of JSON instead of 200, saving thousands of tokens over a long session.
2.  **Logic Clarity:** There is no ambiguity about which setting is active. If it's in the file, it's a deliberate choice.
3.  **Failure Isolation:** As seen with the Podman pull, fewer moving parts in `settings.json` mean faster identification of the "Stuck" state.

---
**Status:** AIR MAPPED & DE-COMPLECTED.
**Attribution:** Glaucon (20260103-133925)
