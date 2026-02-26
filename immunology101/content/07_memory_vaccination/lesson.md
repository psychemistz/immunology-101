# Immunological Memory & Vaccination

## Overview

The adaptive immune system doesn't just fight — it **remembers**. After an
infection is cleared, long-lived memory cells persist for years or decades,
enabling faster, stronger responses on re-encounter. Vaccination exploits
this principle: train the immune system without causing disease.

*Analogy: memory cells are a **cache layer** — precomputed responses ready
for instant retrieval. Vaccines are **pre-trained models** loaded before
the system encounters real threats.*

---

## Primary vs Secondary Immune Response

| Feature | Primary Response | Secondary Response |
|---------|-----------------|-------------------|
| Timing | 7–14 days to peak | 1–3 days to peak |
| Antibody level | Low (mostly IgM) | High (mostly IgG) |
| Affinity | Lower | Higher (affinity-matured) |
| Cell source | Naive B and T cells | Memory B and T cells |
| CS Analogy | Cold start — model training | Cache hit — instant recall |

The speed and magnitude difference is dramatic: secondary responses can be
100–1000× stronger, often clearing a pathogen before symptoms appear.

---

## Memory Cell Populations

### Memory B Cells

- Persist in lymph nodes and spleen for decades.
- Pre-selected for high affinity (products of germinal centre reactions).
- On re-encounter: rapidly differentiate into plasma cells producing
  high-affinity, class-switched antibodies (IgG, IgA).
- Some maintain ongoing somatic hypermutation in germinal centres.

### Memory T Cells

| Subset | Location | Function | CS Analogy |
|--------|----------|----------|------------|
| **T_CM** (central memory) | Lymph nodes, blood | Self-renew; proliferate on recall | Cold standby replica |
| **T_EM** (effector memory) | Tissues, blood | Immediate effector function on re-encounter | Hot standby — instant failover |
| **T_RM** (tissue-resident memory) | Barrier tissues (skin, gut, lung) | First responders at entry sites | Edge cache / CDN node |

### Long-Lived Plasma Cells

- Reside in bone marrow for decades.
- Continuously secrete antibodies without re-stimulation.
- Provide baseline serum antibody levels (serological memory).

---

## Vaccination Strategies

| Type | Mechanism | Example | CS Analogy |
|------|-----------|---------|------------|
| **Live attenuated** | Weakened pathogen replicates mildly | MMR, yellow fever | Sandboxed malware for training |
| **Inactivated** | Killed whole pathogen | Polio (Salk), hepatitis A | Static test fixture |
| **Subunit / protein** | Purified antigen (± adjuvant) | Hepatitis B, HPV | Mock API response |
| **Toxoid** | Inactivated toxin | Tetanus, diphtheria | Defanged exploit sample |
| **mRNA** | mRNA encoding antigen, delivered in LNP | COVID-19 (Pfizer, Moderna) | Source code → runtime builds the antigen |
| **Viral vector** | Harmless virus delivers antigen gene | COVID-19 (AstraZeneca, J&J) | Container image with payload |

### Adjuvants

Adjuvants boost the immune response to a vaccine antigen by activating
innate immunity (via PRRs), enhancing antigen presentation, and promoting
germinal centre reactions.

*Analogy: adjuvants are like feature engineering — they make the training
signal stronger and more informative.*

---

## Correlates of Protection

A **correlate of protection** is a measurable immune parameter (e.g.,
neutralising antibody titre) that predicts whether a vaccinated individual
is protected. Establishing these is a key bioinformatics challenge.

---

## Bioinformatics Relevance

- **Vaccine immunogenomics**: Predicting vaccine responses from HLA type,
  gene expression, and demographic variables.
- **Epitope prediction**: Computational identification of immunodominant
  epitopes for vaccine design (IEDB tools, NetMHCpan).
- **BCR/TCR repertoire analysis**: Tracking clonal expansion and memory
  formation post-vaccination using AIRR-seq.
- **Systems vaccinology**: Integrating transcriptomics, proteomics, and
  serology to predict vaccine efficacy (e.g., HIPC consortium datasets).

---

## Summary

| Concept | Key Point |
|---------|-----------|
| Primary vs secondary | Memory enables faster, stronger, higher-affinity responses |
| Memory B cells | Pre-selected, high-affinity, rapid plasma cell differentiation |
| Memory T cells | T_CM (lymph node), T_EM (blood/tissue), T_RM (barrier tissues) |
| Vaccination | Train immunity without disease — multiple platform strategies |
| Adjuvants | Boost response by activating innate immunity |
| Correlates | Measurable parameters predicting protection |
