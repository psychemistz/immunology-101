# Immune Tolerance & Autoimmunity

## Overview

The immune system must distinguish **self** from **non-self** — and it must
do so with near-zero false positives. When this discrimination fails,
the result is **autoimmunity**: the immune system attacks healthy tissue.

Think of tolerance as **input validation** at multiple layers — catching
bad classifications before they cause damage.

---

## Central Tolerance

Central tolerance occurs during lymphocyte development in the **thymus**
(T cells) and **bone marrow** (B cells). Self-reactive cells are eliminated
before they ever reach the periphery.

| Mechanism | Location | Target | CS Analogy |
|-----------|----------|--------|------------|
| **Negative selection (T cells)** | Thymus medulla | T cells binding self-MHC/peptide too strongly | Compile-time type check |
| **AIRE expression** | Thymic epithelium | Displays tissue-specific antigens for deletion testing | Exhaustive test suite |
| **Receptor editing (B cells)** | Bone marrow | Self-reactive B cells rearrange light chain | Retry with new parameters |
| **Clonal deletion (B cells)** | Bone marrow | Strongly self-reactive B cells undergo apoptosis | Fatal error — process killed |

**AIRE** (Autoimmune Regulator) is a transcription factor that forces thymic
cells to express proteins normally found only in specific organs (e.g., insulin,
myelin). This allows testing against a comprehensive self-antigen library.
AIRE mutations cause multi-organ autoimmunity (APS-1).

---

## Peripheral Tolerance

Some self-reactive cells escape central tolerance. Peripheral mechanisms act
as runtime checks:

| Mechanism | How It Works | CS Analogy |
|-----------|-------------|------------|
| **Anergy** | T cell gets Signal 1 without Signal 2 → unresponsive | Auth failure → account locked |
| **Regulatory T cells (Tregs)** | Actively suppress self-reactive cells via IL-10, TGF-β | Rate limiter / moderator |
| **Immune-privileged sites** | Brain, eyes, testes — physical barriers limit immune access | Air-gapped network |
| **Activation-induced cell death** | Repeated stimulation → Fas/FasL apoptosis | Circuit breaker — too many retries |
| **Peripheral deletion** | Chronic antigen without inflammation → apoptosis | Garbage collection of idle processes |

---

## When Tolerance Fails: Autoimmune Disease

| Disease | Target | Mechanism | Type |
|---------|--------|-----------|------|
| **Type 1 diabetes** | Pancreatic β cells | CD8⁺ T cells destroy insulin-producing cells | Organ-specific |
| **Rheumatoid arthritis** | Joint synovium | TNF-α/IL-6-driven inflammation | Organ-specific |
| **Systemic lupus (SLE)** | DNA, nuclear antigens | Autoantibodies form immune complexes | Systemic |
| **Multiple sclerosis** | Myelin sheaths | T cells attack CNS myelin | Organ-specific |
| **Graves' disease** | TSH receptor | Stimulatory autoantibodies | Organ-specific |

### Contributing Factors

- **Genetic susceptibility**: HLA alleles (e.g., HLA-DR4 in RA, HLA-DR3 in SLE)
- **Molecular mimicry**: Pathogen epitopes resemble self-antigens
- **Bystander activation**: Inflammation damages tissue, exposing hidden self-antigens
- **Defective Tregs**: Reduced suppressive function

*Analogy: autoimmunity = false positive at scale. The classifier (immune system)
was trained well but fails on edge cases due to noisy labels (mimicry) or
overfitting (genetic predisposition).*

---

## Bioinformatics Relevance

- **HLA association studies**: GWAS identify HLA risk alleles for autoimmune
  diseases (e.g., HLA-B27 and ankylosing spondylitis).
- **Autoantibody profiling**: Protein arrays detect autoantibody signatures
  for diagnosis and subtyping.
- **scRNA-seq in autoimmunity**: Characterising pathogenic vs protective immune
  cell populations in affected tissues.
- **Treg signatures**: Gene expression signatures distinguish functional Tregs
  (FOXP3, IL2RA, CTLA4) from other CD4⁺ cells.

---

## Summary

| Concept | Key Point |
|---------|-----------|
| Central tolerance | Deletion/editing of self-reactive cells during development |
| AIRE | Thymic expression of tissue-specific antigens — exhaustive test suite |
| Peripheral tolerance | Anergy, Tregs, immune privilege, AICD |
| Autoimmunity | Tolerance failure — false positives attack self |
| Risk factors | HLA genetics, molecular mimicry, defective Tregs |
