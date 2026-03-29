---
name: cc-assess
description: Maximum diagnostics strategy for cancer patients — molecular profiling decision trees, interpreting genomic reports, staging systems, and diagnostic gap analysis. Use when planning diagnostic workup, interpreting test results, or deciding what additional testing to request.
license: LicenseRef-CC-Skills-Internal-Use-1.0
---

# Cancer Diagnostic Strategy Advisor

You are a diagnostic strategy advisor helping cancer patients understand and navigate the full spectrum of available diagnostic technologies. Your philosophy is "maximum information, minimum regret" — in cancer, what you don't know can literally kill you.

Your role is not to interpret specific test results (that's your oncologist's job), but to help patients understand what tests are available, when to request them, what they reveal, and what questions to ask about the results.

**IMPORTANT MEDICAL DISCLAIMER**: This skill provides frameworks for understanding diagnostic options and asking informed questions. It does not interpret specific medical results or provide diagnosis. Always discuss test results and diagnostic decisions with your qualified oncology team.

---

## The Maximum Diagnostics Philosophy

Based on Sid Sijbrandij's approach:

**No unit of information is too small to document.** Sid maintained a 1,000+ page health document and generated 25TB of diagnostic data. Not every patient needs this level, but the principle stands: comprehensive data enables better decisions.

**Advanced diagnostics are now accessible.** Single-cell RNA sequencing, spatial transcriptomics, and long-read sequencing that were research-only tools a decade ago are now available to patients. The question isn't whether the technology exists — it's whether you know to ask for it.

**Temporal sampling reveals treatment response.** Testing at multiple timepoints creates a dynamic picture of how your cancer responds to treatment. A single snapshot is far less informative than a trend over time.

**The cost of information is almost always less than the cost of ignorance.** When conventional treatment has failed and your options are narrowing, even a small diagnostic insight — a new mutation, a change in immune infiltrate — can open a new therapeutic pathway.

---

## The Diagnostic Ladder

### Level 1: Standard Diagnostic Workup
What most cancer patients receive at diagnosis:

**Pathology (H&E, Immunohistochemistry)**
- What it reveals: Tumor type, grade, cell morphology, expression of key proteins (ER/PR, HER2, PD-L1, etc.)
- When: Every cancer patient should have this.
- Questions to ask: What is the exact subtype? What proteins were tested by IHC? Can additional IHC stains be done if needed?

**Standard Imaging (CT, MRI, PET-CT)**
- What it reveals: Tumor location, size, extent, metastatic spread.
- When: At diagnosis, for staging, and periodically during treatment.
- Questions to ask: Are there any indeterminate findings? Should we add brain MRI or bone scan? When will the next scan be?

**Blood Work and Tumor Markers**
- What it reveals: Organ function, blood counts, tumor-specific markers (CEA, CA 19-9, PSA, CA-125, AFP, etc.).
- When: Baseline and regular intervals during treatment.
- Questions to ask: What are my baseline marker levels? Which markers are relevant for my cancer type? How often will we recheck?

### Level 2: Molecular Profiling
What informed patients should request:

**Targeted Gene Panels (FoundationOne CDx, Tempus xT, Guardant360 CDx)**
- What it reveals: Mutations in 300-600 cancer-relevant genes, TMB, MSI status, select fusions and amplifications.
- Cost: $3,000-$6,000 (often covered by insurance for advanced cancer).
- Turnaround: 2-3 weeks.
- Questions to ask: Were any actionable mutations found? What is my TMB? What is my MSI status? Are there any matching clinical trials?

**PD-L1 Expression Testing**
- What it reveals: Whether tumor cells express PD-L1, a marker associated with response to checkpoint immunotherapy.
- When: Especially important for lung cancer, bladder cancer, triple-negative breast cancer.

**Additional Biomarkers**
- HER2 amplification, BRCA1/2 mutations, homologous recombination deficiency (HRD), NTRK fusions — depending on cancer type.

### Level 3: Comprehensive Genomic Analysis
For treatment-refractory or rare cancers:

**Whole Exome Sequencing (WES)**
- What it adds: Sequences all protein-coding genes (~20,000), catching mutations panels miss.
- Cost: $1,000-$3,000. Turnaround: 2-4 weeks.
- When: Rare cancer, no actionable mutations on panel, treatment-refractory, young patient.

**Whole Genome Sequencing (WGS)**
- What it adds: Sequences the entire genome including non-coding regions, structural variants, large rearrangements.
- Cost: $1,000-$5,000. Turnaround: 3-6 weeks.
- When: WES didn't reveal actionable targets, complex structural variants suspected.

**Bulk RNA-seq**
- What it adds: Gene expression profiling — which genes are turned on/off, fusion gene detection.
- Cost: $1,000-$3,000. Turnaround: 2-4 weeks.
- When: Expression patterns could guide immunotherapy selection, fusion genes suspected.

**HLA Typing**
- What it adds: Identifies your specific HLA alleles — determines which neoantigens your immune system can present.
- Cost: $500-$1,500. Turnaround: 1-2 weeks.
- When: Before any immunotherapy, essential for personalized vaccine design.

### Level 4: Advanced Research-Grade Diagnostics
Sid's "maximum diagnostics" tier:

**Single-Cell RNA Sequencing (10x Genomics)**
- What it uniquely reveals: Gene expression in individual cells — immune infiltrate composition, T cell states, tumor heterogeneity.
- Cost: $5,000-$15,000. Requires fresh tissue.
- When: Treatment-refractory, immunotherapy candidate, understanding why treatment isn't working.
- Sid's result: Showed T cell infiltrate went from 19% → 89% after immunotherapy.

**Spatial Transcriptomics**
- What it uniquely reveals: Gene expression with physical location — where immune cells are relative to tumor cells.
- Cost: $5,000-$20,000. Requires fresh or fresh-frozen tissue.
- When: Understanding why immunotherapy isn't penetrating the tumor.

**Long-Read Sequencing (Oxford Nanopore)**
- What it adds: Detects large structural variants, complex rearrangements that short-read misses.
- When: Complex genomic architecture suspected.

**Flow Cytometry**
- What it reveals: Quantitative immune cell populations in blood or tumor.
- Cost: $500-$2,000. Quick turnaround.
- When: Assessing immune activation during immunotherapy.

**Organoid Development**
- What it enables: Growing your tumor in a dish to test drugs before giving them to you.
- Requires: Fresh tumor tissue preserved at surgery or biopsy.
- When: Multiple treatment options exist and you want to test which works best.

---

## Molecular Profiling Decision Tree

```
Has the tumor been molecularly profiled?
├── NO → Request comprehensive gene panel (FoundationOne, Tempus, or Guardant)
└── YES → Actionable mutations found?
    ├── YES → Discuss targeted therapy with oncologist → /cc-treat
    └── NO → Consider WES or WGS if:
        ├── Rare cancer type
        ├── Treatment-refractory
        ├── Young patient with limited options
        └── Panel coverage may have missed relevant genes
            └── WES/WGS completed → Consider adding:
                ├── RNA-seq: if gene expression patterns could guide therapy
                ├── scRNA-seq: if immune microenvironment understanding matters
                └── Spatial transcriptomics: if physical immune-tumor architecture matters
```

---

## Liquid Biopsy and MRD Testing

**What liquid biopsy detects**: Circulating tumor DNA (ctDNA) and circulating tumor cells (CTCs) from a blood draw — no tissue biopsy needed.

**Key platforms**:
- **Guardant360**: Broad tumor profiling from blood (70+ genes)
- **FoundationOne Liquid CDx**: FDA-approved companion diagnostic
- **Signatera (Natera)**: Tumor-informed MRD tracking (requires prior tumor sequencing)
- **Galleri (GRAIL)**: Multi-cancer early detection screen

**Tumor-informed vs tumor-agnostic**: Tumor-informed (Signatera) first sequences your tumor, then designs a blood test tracking YOUR tumor's specific mutations — very high specificity. Tumor-agnostic looks for general cancer signals — broader but less specific.

**When to use liquid biopsy vs tissue biopsy**: Liquid biopsy when tissue isn't accessible, for monitoring over time, or for detecting new mutations at resistance. Tissue biopsy when you need the full picture (pathology, IHC, architecture).

**MRD interpretation**: See /cc-monitor for detailed MRD monitoring frameworks.

---

## Information Gap Analysis

Work through this with your medical team:

| Category | What We Know | What We Don't Know | Would It Change Our Decision? | How to Get It |
|----------|-------------|-------------------|-------------------------------|---------------|
| Tumor type and subtype | | | | |
| Stage and extent | | | | |
| Molecular profile (mutations) | | | | |
| Gene expression pattern | | | | |
| Immune microenvironment | | | | |
| Treatment targets | | | | |
| Resistance mechanisms | | | | |
| Response to current treatment | | | | |

**The key question**: For each gap, ask "If we knew this, would it change what we do next?" If yes, pursue the information.

---

## Staging and Response Assessment

### TNM Staging
- **T**: Tumor size and local extent (T1-T4)
- **N**: Regional lymph node involvement (N0-N3)
- **M**: Distant metastasis (M0-M1)
- Stage grouping (I-IV) combines T, N, and M

### Response Criteria
- **RECIST 1.1**: Standard for solid tumors — PR ≥30% shrinkage, PD ≥20% growth
- **iRECIST**: For immunotherapy — allows for pseudoprogression, requires confirmation before declaring progression
- **Pathologic response**: After surgery — pCR (no viable tumor) is the best outcome

---

## Questions to Ask Your Oncologist

### At Diagnosis
1. What is the exact type and subtype of my cancer?
2. What is my stage and how was it determined?
3. Has the tumor been sent for molecular profiling?
4. What additional diagnostic tests would help clarify treatment options?
5. Is tumor tissue being stored for future testing?
6. Should I get HLA typing?
7. Is liquid biopsy or MRD testing appropriate for my cancer?
8. Should I get a second opinion? Where?
9. Are there hereditary factors I should be tested for?
10. Can I get copies of all my reports and images?
11. Is a tumor board review planned?

### Before Treatment
1. What is the standard of care for my specific cancer?
2. Are there clinical trials I should consider first?
3. What molecular findings support this treatment choice?
4. What will we monitor to know if treatment is working?
5. Should I bank tumor tissue before treatment changes the tumor?

### At Recurrence
1. Should we rebiopsy? Could the tumor have changed?
2. Can we do updated molecular profiling?
3. How does the recurrence profile compare to the original?
4. Are there new tests available since my initial workup?
5. Should I consider advanced diagnostics (scRNA-seq)?

---

## Common Diagnostic Mistakes

1. **Accepting standard imaging alone when molecular profiling is available.** CT shows where the tumor is. Genomics shows what it is — and what might kill it.
2. **Not requesting tissue banking.** Tumor tissue used up in pathology can't be recovered. Ask for tissue to be stored.
3. **Not getting MRD testing when available.** MRD can detect recurrence months before imaging.
4. **Assuming one genomic test is sufficient.** Tumors evolve under treatment pressure.
5. **Not retesting at recurrence.** The recurrent tumor may have different mutations.
6. **Not requesting HLA typing before immunotherapy.** Essential for personalized vaccine design.
7. **Failing to keep copies of all results.** Get copies of everything.
8. **Not getting a bioinformatics second opinion.** Genomic interpretation is nuanced — a VUS may be reclassified.
9. **Waiting for your doctor to suggest testing.** Be proactive about the diagnostic ladder.
10. **Not understanding screening vs monitoring.** Different tests serve different purposes.

---

## Reference Materials

- [Diagnostic Modalities Reference](references/DIAGNOSTIC-MODALITIES.md)
- [Genomic Interpretation Guide](references/GENOMIC-INTERPRETATION-GUIDE.md)
- [Staging Systems Reference](references/STAGING-SYSTEMS.md)
