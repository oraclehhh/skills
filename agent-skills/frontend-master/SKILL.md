---
name: frontend-master
description: Frontend UI/UX work with Gemini CLI in --yolo mode. Use when (1) modifying visual/styling elements in frontend files (.tsx, .jsx, .vue, .svelte, .css), (2) implementing UI components, (3) adjusting layout, colors, spacing, typography, or animations, (4) creating responsive designs, (5) any frontend task involving how things LOOK rather than how they WORK, or (6) image-based frontend tasks (screenshots, mockups, Figma exports) where visual context drives the implementation.
---

# Frontend Master Skill

Frontend UI/UX implementation workflow using Gemini CLI in `--yolo` mode.
For image-based tasks, Gemini analyzes the image first, then implements based on that analysis.

## Routing Rules

### USE this skill
- Visual properties: colors, backgrounds, borders, shadows
- Layout: flexbox, grid, margins, padding, positioning
- Typography: font sizes, weights, line heights
- Animation: transitions, keyframes, hover states
- Responsive design: breakpoints, media queries
- Component styling: Tailwind, CSS-in-JS, styled-components
- Image-based frontend: generate/modify components from screenshots, mockups, design exports

### DO NOT use this skill
- Pure logic: API calls, state management, event handlers
- Type definitions, utility functions, business logic
- Logic optimization or non-frontend image tasks → use `logic-master`

---

## Workflow

```
Task received
     │
     ▼
┌──────────┐     ┌─────────────────┐     ┌──────────────┐     ┌────────────┐
│  Image   │ Yes │ Phase 1:        │     │ Phase 2:     │     │  Verify    │
│  input   ├────►│ Gemini image    ├────►│ Gemini       ├────►│  lsp_diag  │
│  exists? │     │ analysis (@ref) │     │ --yolo impl  │     │  nostics   │
└────┬─────┘     └─────────────────┘     └──────┬───────┘     └────────────┘
     │ No                                       ▲
     └──────────────────────────────────────────┘
```

### Step 1: Detect image input
Check if the task includes image files (`.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.svg`, `.pdf`).

### Step 2: Branch execution

**Image exists → 2-phase pipeline (Phase 1 → Phase 2)**
**No image → Direct execution (Phase 2 only)**

### Step 3: Verify results
Run `lsp_diagnostics` to check for type/build errors and fix them.

---

## Phase 1: Gemini Image Analysis

Reference image paths with `@` to extract UI structure. Save results to a temp file.

```bash
ANALYSIS_PROMPT=$(cat <<'PROMPT'
@<image-path>
Analyze this UI image and organize in the following format:
1. LAYOUT: Overall layout structure (flex/grid, direction, alignment)
2. COMPONENTS: UI component list and hierarchy
3. COLORS: Color palette (hex codes)
4. TYPOGRAPHY: Font sizes, weights, line heights
5. SPACING: Margins, padding, gap values (px/rem estimates)
6. INTERACTIONS: Buttons, links, hover states and interactive elements
7. RESPONSIVE: Responsive design considerations
PROMPT
)

gemini --yolo -p "$ANALYSIS_PROMPT" > /tmp/ui-analysis.md
```

### Analysis Prompt Variants

| Scenario | Prompt focus |
|----------|-------------|
| Simple component | `@<img>` + map to Tailwind classes |
| Complex layout | `@<img>` + detailed hierarchy, grid system, spacing |
| Before/After comparison | `@<before> @<after>` + diff changes in CSS/Tailwind |
| Responsive comparison | `@<desktop> @<mobile>` + breakpoint differences |
| Design system extraction | `@<img>` + map to color/typo/spacing tokens |
| Error screenshot | `@<img>` + identify rendering issues and CSS fixes |

### Single Component Analysis

```bash
ANALYSIS_PROMPT=$(cat <<'PROMPT'
@<image-path>
Focus only on the [component-name] section. Analyze and map to Tailwind CSS classes.
PROMPT
)
gemini --yolo -p "$ANALYSIS_PROMPT" > /tmp/ui-analysis.md
```

### Multi-Image Analysis

```bash
ANALYSIS_PROMPT=$(cat <<'PROMPT'
@<desktop.png> @<mobile.png>
Compare and analyze both images:
1. Desktop layout structure
2. Mobile layout structure
3. Responsive transition points
4. Common and differing elements
5. Tailwind breakpoint mapping
PROMPT
)
gemini --yolo -p "$ANALYSIS_PROMPT" > /tmp/ui-analysis.md
```

---

## Phase 2: Gemini --yolo Implementation

### With image analysis results

Inject analysis into the implementation prompt.

```bash
ANALYSIS=$(cat /tmp/ui-analysis.md)

gemini --yolo -p "Implement based on the following UI analysis:

--- UI ANALYSIS ---
${ANALYSIS}
--- END ANALYSIS ---

Implementation requirements:
- Follow existing CSS framework/patterns in the project
- Use semantic HTML structure
- Include responsive design
- Consider accessibility (a11y)

Target file: <target-file-path>" \
  --include-directories <relevant-dirs>
```

### Direct execution (no image)

```bash
# With file context
cat <frontend-file> | gemini --yolo -p "<instruction>"

# With directory context
gemini --yolo -p "<instruction>" --include-directories <dirs>

# With full project context
gemini --yolo -p "<instruction>" --all-files
```

### Required Flags

| Flag | Purpose |
|------|---------|
| `--yolo` | **MANDATORY** - Auto-approve all changes |
| `--prompt` / `-p` | Specify the task |
| `--include-directories` | Add specific folder context |
| `--all-files` / `-a` | Include full project context |

---

## Examples

### Component Styling

```bash
# Update button styles
cat src/components/Button.tsx | gemini --yolo -p "Change button color to blue-500, add hover:scale-105 transition"

# Responsive navbar
gemini --yolo -p "Make the navbar responsive with hamburger menu on mobile" --include-directories src/components
```

### Layout Changes

```bash
# Convert to grid layout
cat src/pages/Dashboard.tsx | gemini --yolo -p "Convert this layout to CSS Grid with 3 columns"
```

### Animation

```bash
# Modal fade-in
cat src/components/Modal.tsx | gemini --yolo -p "Add fade-in animation when modal opens"
```

### Full Project Changes

```bash
# Dark mode
gemini --yolo -p "Update all components to use dark mode color palette" --all-files
```

### Image-Based Full Pipeline

```bash
# Phase 1: Analyze mockup
ANALYSIS_PROMPT=$(cat <<'PROMPT'
@designs/card-component.png
Analyze this card component:
1. Layout structure (flex/grid)
2. Size, color, spacing of each element
3. Tailwind CSS class mapping
4. Estimated hover/interaction states
PROMPT
)
gemini --yolo -p "$ANALYSIS_PROMPT" > /tmp/ui-analysis.md

# Phase 2: Implement
ANALYSIS=$(cat /tmp/ui-analysis.md)
gemini --yolo -p "Implement a React component based on the following analysis:

--- UI ANALYSIS ---
${ANALYSIS}
--- END ANALYSIS ---

- Create at src/components/Card.tsx
- Use Tailwind CSS
- Include TypeScript props interface
- Follow existing component patterns" \
  --include-directories src/components
```

---

## Subagent Delegation Templates

### Standard Frontend Task

```
1. TASK: Update component styling via Gemini CLI
2. EXPECTED OUTCOME: Visually updated component
3. REQUIRED TOOLS: Bash (gemini CLI), Read, lsp_diagnostics
4. MUST DO:
   - Use --yolo flag
   - Verify with lsp_diagnostics after execution
   - Follow existing CSS framework patterns
5. MUST NOT DO:
   - Modify logic or event handlers
   - Remove existing functionality
6. CONTEXT: [file paths, design requirements, existing patterns]
```

### Image-Based Frontend Task

```
1. TASK: Generate/modify component from image reference
2. EXPECTED OUTCOME: Component matching the visual reference
3. REQUIRED TOOLS: Bash (gemini CLI), Read, Edit, lsp_diagnostics
4. MUST DO:
   - Phase 1: Run Gemini with @-image prompt → save to /tmp/ui-analysis.md
   - Phase 2: Inject analysis into gemini --yolo prompt
   - Verify with lsp_diagnostics
   - Clean up temp files after completion
5. MUST NOT DO:
   - Skip image analysis phase
   - Modify business logic
6. CONTEXT: [image path, target file, existing patterns]
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Command hangs | Ensure `--yolo` flag is present |
| No changes made | Check file context with `--include-directories` |
| Unexpected changes | Add more specific constraints in prompt |
| Build errors | Run `lsp_diagnostics` and fix type issues |
| Image not recognized | Use absolute path, verify file exists |
| Analysis too vague | Add specific extraction targets in prompt |
| Gemini ignores analysis | Wrap in `--- UI ANALYSIS ---` delimiters |
| Temp file conflict | Use unique names: `/tmp/ui-analysis-{component}.md` |

## Security

- `--yolo` auto-approves ALL changes. Use only in version-controlled directories.
- Image files referenced by `@` paths are processed in Gemini CLI context. Verify path access policy before running.
