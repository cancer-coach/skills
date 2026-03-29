# cancer-coach

A comprehensive cancer patient empowerment skills framework for AI coding assistants. Built for Claude Code, Cursor, Gemini CLI, Codex CLI, and any tool that supports the skills standard.

**Assess → Treat → Navigate → Monitor.** Four production-quality skills covering every phase of a patient's cancer journey, plus a master orchestrator to tie them together.

---

## Why This Exists

Cancer patients who exhaust standard care options are often told nothing more can be done. But an emerging approach — pioneered by patients like Sid Sijbrandij — shows that combining maximum diagnostics, parallel treatments, AI-assisted decision-making, and aggressive regulatory navigation can produce outcomes that conventional medicine didn't predict.

These skills give your AI assistant genuine patient advocacy expertise. Not surface-level health tips — detailed, evidence-informed frameworks for understanding your options, asking better questions, and navigating a complex system alongside your medical team.

**Important:** These skills do not provide medical advice. They provide frameworks for patient empowerment and education. Always work with qualified healthcare professionals.

---

## Skills Overview

| Skill | Phase | What It Does |
|-------|-------|-------------|
| [`cc-assess`](skills/cc-assess/SKILL.md) | Assess | Maximum diagnostics philosophy, molecular profiling decision trees, interpreting genomic reports, staging systems |
| [`cc-treat`](skills/cc-treat/SKILL.md) | Treat | Parallel therapy frameworks, treatment modality reference, toxicity overlap analysis, standard-of-care vs experimental decisions |
| [`cc-navigate`](skills/cc-navigate/SKILL.md) | Navigate | Expanded access pathways, clinical trial search, team assembly, insurance navigation, tissue and data rights |
| [`cc-monitor`](skills/cc-monitor/SKILL.md) | Monitor | MRD testing, imaging cadence, biomarker tracking, response assessment criteria, data organization |
| [`cc-strategist`](skills/cc-strategist/SKILL.md) | All phases | Master orchestrator — founder-mode coaching, journey routing, cross-phase coordination, cancer-type playbooks |

### The Patient Journey

```
ASSESS          TREAT           NAVIGATE        MONITOR
────────        ────────        ────────        ────────
Diagnostics     Therapy         Access &        Response
Staging         Architecture    Regulatory      Assessment
Molecular       Parallel        Team Build      MRD Testing
Profiling       Planning        Trials          Adaptation
                Personalized    Insurance       Data
                Medicine        Rights          Organization
```

Each phase builds on the previous. Monitoring loops back to Assessment when signals warrant re-evaluation.

---

## Installation

### Via npx skills (recommended)

```bash
npx skills add cancer-coach/skills
```

Auto-detects your AI harness and installs to the correct directory.

### Manual installation

Download and extract the skills directory to your project root:

```
your-project/
├── .claude/skills/        # Claude Code
│   └── cc-assess/
│   └── cc-treat/
│   └── cc-navigate/
│   └── cc-monitor/
│   └── cc-strategist/
├── .cursor/skills/        # Cursor
├── .gemini/skills/        # Gemini CLI
├── .codex/skills/         # Codex CLI
└── .agents/skills/        # VS Code Copilot / OpenClaw
```

### Update

```bash
npx skills update
```

---

## Usage

### Start with the orchestrator

For a new diagnosis or when you're not sure where to start:

```
Use the cc-strategist skill. I was recently diagnosed with
stage III osteosarcoma. Help me understand my options and
build a plan for taking an active role in my treatment.
```

### Capture your context first (highly recommended)

```
Use the cc-strategist skill and run /cc-teach
```

This captures your diagnosis, stage, treatments tried, medical team, and goals so all skills give personalized guidance rather than generic frameworks.

### Use phase skills directly

```
Use the cc-assess skill to help me understand what diagnostic
tests I should be requesting beyond standard imaging. My oncologist
ordered a CT scan but I want to know about genomic profiling options.

Use the cc-treat skill to help me evaluate whether parallel
treatment approaches might be appropriate for my situation.
My cancer has recurred after standard chemotherapy.

Use the cc-navigate skill to help me find clinical trials for
recurrent osteosarcoma and understand the expanded access pathway
for experimental immunotherapies.

Use the cc-monitor skill to help me set up a monitoring protocol.
I want to track MRD, imaging, and biomarkers systematically
between treatment cycles.
```

---

## Philosophy

These skills are built on four principles drawn from Sid Sijbrandij's approach to cancer:

**1. Maximum diagnostics**

Every piece of information about your cancer is potentially actionable. Don't settle for the minimum diagnostic workup when advanced molecular profiling, genomic sequencing, and liquid biopsies might reveal treatment targets or monitoring signals that standard tests miss.

**2. Parallel over sequential**

When standard care has failed and time is limited, testing multiple therapeutic hypotheses simultaneously — with non-overlapping toxicity profiles — can compress months of sequential trial-and-error into weeks of informed iteration.

**3. Founder mode on your cancer**

You are not a passive recipient of medical care. You are the architect of your treatment strategy. Your medical team provides expertise; you provide direction, coordination, and the determination to explore every option.

**4. Radical data transparency**

Your medical data belongs to you. Organizing it, understanding it, and sharing it with your full medical team — and potentially with the research community — creates better decisions and advances science for future patients.

---

## What's Covered

### cc-assess
- Diagnostic ladder (standard → molecular → advanced)
- Molecular profiling decision tree (panel vs. WES vs. WGS)
- When to request RNA-seq, scRNA-seq, spatial transcriptomics
- Liquid biopsy and MRD testing options
- Interpreting genomic reports and actionable mutations
- Staging systems (TNM, RECIST, iRECIST)
- Information gap analysis framework
- Questions to ask your oncologist about diagnostics

### cc-treat
- Treatment modality reference (chemo, immunotherapy, targeted, radiation, surgery, cell therapy, vaccines)
- Parallel therapy framework and toxicity overlap matrix
- Standard-of-care vs. experimental decision framework
- Personalized medicine approaches (neoantigen vaccines, CAR-T, TCR-T, radioligand therapy)
- Organoid and functional drug testing
- Treatment evidence ladder
- Treatment plan template for discussing with your team

### cc-navigate
- Expanded access pathways (compassionate use, Right to Try, single-patient IND)
- Clinical trial navigation (ClinicalTrials.gov search strategy, eligibility, site selection)
- Team assembly framework (who you need, when, how to evaluate)
- Insurance navigation and appeals
- Tissue access and medical data rights
- Second opinion strategy
- Questions to ask trial coordinators

### cc-monitor
- MRD testing framework and cadence
- Imaging monitoring schedules by phase
- Biomarker tracking and trend analysis
- Response assessment criteria (RECIST 1.1, iRECIST, metabolic, pathologic)
- Signal vs. noise framework (when to act, when to watch)
- Adaptation trigger matrix
- Personal health data organization
- Data sharing and open science approach

### cc-strategist
- Patient journey lifecycle and routing
- `/cc-teach` command: context capture interview
- Journey mode selector (newly diagnosed / active treatment / monitoring / recurrence)
- Cross-phase workflow guides
- Cancer type playbooks
- Founder mode checklist
- Team assembly guidance
- Common strategic mistakes

---

## Website

The repository includes a static landing page in [`site/`](site/).

### Local preview

```bash
python3 -m http.server 4173 --directory site
```

Then open `http://localhost:4173`.

### Cloudflare deployment

```bash
npx wrangler dev
npx wrangler deploy
```

---

## License

This repository is available under the `CC Skills Internal Use License v1.0`.

In plain English:

- You may use and adapt the skills internally for your own cancer treatment
  journey or that of your family members.
- You may share Output with your healthcare providers.
- You may not use the skills to provide services to third parties.
- You may not copy, repackage, redistribute, white-label, or resell the skills.

This is a source-available license, not an open source license. For the full
terms, see [LICENSE](LICENSE).
