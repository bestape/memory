# Communication & Style Mandates

## 1. The Straightup Mandate
Always end turns with direct, high-density Markdown reports. Do not hide primary outputs inside shell blocks or verbose explanations. Speak directly to the Lead Partner via the HUD.

## 2. No Tables Policy
Tables are prohibited in the Heartwood and all agent communications. Use structured lists, headers, and bullet points to present data. This ensures maximum readability across diverse terminal environments and simplifies forensic log parsing.

## 3. Scope of Changes
*   **The Meta-Root (`/home/bestape/gemini/`):** This is the static orchestration layer. It manages environment tools and CLI logic. It should remain largely unchanged unless refining core orchestration logic.
*   **The Heartwood (`repos/diy-make/memory/public/`):** This is where active changes happen. When instructed to "change the Heartwood," it refers specifically to this directory. All logic, memory, and legislative DNA reside here.
*   **Project Repositories (`repos/*`):** These are the workbenches for specific engineering tasks.

---
*Mandated by Eudaimonia (2026-01-05) following the Great Forensic Trace.*
