# Cancer Coach

Five educational skills for AI assistants: prepare questions, organize records, follow through on care tasks, and discuss priorities with a qualified cancer care team. These skills do not diagnose, choose treatments, interpret scans independently, change medicines, prescribe tests or monitoring schedules, or provide emergency care. AI can make mistakes; verify important summaries and details with the team.

Content updated **2026-10-15**. Source checks are an editorial review, not clinical validation or clinician review. The pack incorporates practical lessons from [JJ Maxwell's account](https://jjmaxwell4.com/writing/things-to-know-when-you-get-cancer/) and [Hacker News](https://news.ycombinator.com/item?id=50093568), clearly separated from medical evidence. See the [evidence and source notes](cc-strategist/references/EVIDENCE-AND-SOURCE-NOTES.md).

## Skills

| Skill | Useful for |
| --- | --- |
| [cc-strategist](cc-strategist/SKILL.md) | Start with a goal; prepare a short care agenda and route by need |
| [cc-assess](cc-assess/SKILL.md) | Understand report terms and ask about testing, staging, tumor biomarkers and inherited risk |
| [cc-treat](cc-treat/SKILL.md) | Prepare shared decision questions about clinician-provided options, evidence, benefits, harms and burden |
| [cc-navigate](cc-navigate/SKILL.md) | Prepare second opinions, trial leads, referrals, cost questions and records requests |
| [cc-monitor](cc-monitor/SKILL.md) | Record the team's follow-up plan, symptoms, missing results and verified visit summaries |

There is no mandatory sequence, comprehensive intake, universal testing ladder, treatment-combination formula or scan schedule. A one-page summary and one next step may be enough. Ask for support; outcomes are not a measure of personal effort.

## Use and privacy

Start with a small request:

```text
Use cc-strategist. Help me prepare three questions for my next appointment.
I want to discuss recovery and what the next steps mean for daily life.
```

`/cc-teach` is an optional context conversation interpreted by the AI host, not a command guaranteed in every product. Skip any question. General guidance needs no records upload. For someone else's information, obtain their permission or appropriate authority.

Share only relevant redacted excerpts. Your AI provider's privacy, retention, training, memory and tool settings apply; do not assume medical confidentiality or HIPAA compliance. The skills instruct the assistant not to automatically persist context, upload records, contact third parties or transmit health information. Any such action needs a separate explicit request and review of destination/content. Removing names does not reliably anonymize genomic data.

For severe symptoms, use local emergency services or the team's urgent action plan immediately. **During chemotherapy, 38°C / 100.4°F or higher requires immediate oncology contact and urgent assessment**, without waiting for persistence. If the team cannot be reached promptly, seek emergency care and explain chemotherapy and fever. Follow stricter/lower team thresholds. [CDC fever guidance](https://www.cdc.gov/cancer-preventing-infections/patients/fever.html), checked 2026-10-15. These skills do not monitor or respond to emergencies.

## Install

The published skills repository is [cancer-coach/skills](https://github.com/cancer-coach/skills):

```bash
npx skills add cancer-coach/skills
```

This command uses a third-party installer; review its requirements and your host's instructions. It is shown for users and is not run by this project. Host compatibility and slash-command support vary. For manual installation, copy the five `cc-*` folders from this repository's root into the skill directory supported by your host. Preserve each folder's `references/`. Do not store health records in a source repository.

## Checks

```bash
python3 scripts/check-content.py
```

This dependency-free check validates packaging and local links. It does not establish medical safety; safety changes also need independent scenario review. Do not commit personal health information, generated patient records, or evaluation data from real people.

## Website and release coordination

The [landing page](https://cancer.v1be.codes/) is maintained separately in the private `ckorhonen/cancer-coach` repository on `ckorhonen/cancer-coach-site`. It is not part of this skills-only package. The five root skill folders here mirror that branch's `skills/` directory; keep the copies synchronized when preparing releases. Publication needs the session's release authority and the applicable project checks.

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
