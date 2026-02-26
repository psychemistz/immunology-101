# B Cells & Antibodies

## Overview

If innate immunity is the firewall, B cells are the **key-value store** of
adaptive immunity. Each B cell produces a unique antibody — a protein that binds
one specific antigen with high affinity. Together, the B cell repertoire can
recognise virtually any molecular shape.

This module covers B cell development, antibody structure, and the mechanisms
that generate antibody diversity.

---

## B Cell Development

B cells develop in the **bone marrow** (hence "B"), where they undergo V(D)J
recombination to generate a unique B cell receptor (BCR). Only cells that pass
quality control (not self-reactive, functional receptor) survive.

| Stage | Event | CS Analogy |
|-------|-------|------------|
| Pro-B cell | Heavy chain gene rearrangement | Generating a random API key |
| Pre-B cell | Light chain rearrangement, pre-BCR checkpoint | Key validation |
| Immature B cell | Self-tolerance testing (negative selection) | Input sanitisation — reject self-matches |
| Mature naive B cell | Exits to periphery, awaits antigen | Deployed service, idle |

---

## Antibody Structure

An antibody (immunoglobulin, Ig) is a Y-shaped protein with two functional
regions:

- **Fab region** (Fragment, antigen-binding): The variable tips that bind
  antigen. Each antibody has two identical binding sites.
  *Analogy: the lookup key in a key-value store.*

- **Fc region** (Fragment, crystallisable): The constant stem that determines
  the antibody class and interacts with immune cells and complement.
  *Analogy: the response payload / metadata.*

### Antibody Classes (Isotypes)

| Isotype | Location | Function | CS Analogy |
|---------|----------|----------|------------|
| **IgM** | Blood (pentamer) | First responder; complement activation | Default HTTP response |
| **IgG** | Blood, tissues | Opsonisation, neutralisation, crosses placenta | Standard API response — most versatile |
| **IgA** | Mucosal surfaces (dimer) | Mucosal immunity | Edge/CDN cache |
| **IgE** | Tissues (bound to mast cells) | Anti-parasite; allergy mediator | Webhook trigger |
| **IgD** | B cell surface | BCR co-receptor; poorly understood | Debug/trace header |

---

## Generating Diversity

The immune system generates ~10¹¹ unique antibody specificities via:

1. **V(D)J recombination** — Combinatorial joining of Variable, Diversity, and
   Joining gene segments.
2. **Junctional diversity** — Random nucleotide additions/deletions at join sites.
3. **Somatic hypermutation (SHM)** — Point mutations in V regions during germinal
   centre reactions, selected for higher affinity.
4. **Class-switch recombination (CSR)** — Switching the Fc region (e.g., IgM → IgG)
   without changing antigen specificity.

*Analogy: V(D)J = combinatorial parameter generation; SHM = hyperparameter
tuning via random search; CSR = changing the output format while keeping the
query logic.*

---

## B Cell Activation & The Germinal Centre

1. Naive B cell encounters antigen matching its BCR.
2. With T cell help (CD4⁺), the B cell enters a **germinal centre** (GC) in the
   lymph node.
3. Inside the GC: rapid proliferation, SHM, and selection for high-affinity
   clones (**affinity maturation**).
4. Output: **plasma cells** (antibody factories) and **memory B cells**.

*Analogy: the GC is a training loop — generate variants (SHM), evaluate fitness
(antigen binding), select the best (clonal selection), deploy (plasma cells),
and cache (memory cells).*

---

## Bioinformatics Relevance

- **BCR-seq / AIRR-seq**: Sequencing B cell receptor repertoires to study
  diversity, clonal expansion, and convergent responses.
- **Antibody engineering**: Computational design of therapeutic antibodies
  using structural prediction (AlphaFold, RoseTTAFold).
- **scRNA-seq + VDJ**: Single-cell platforms (10x Genomics) pair transcriptome
  with BCR sequence, linking cell state to clonotype.
- **Immune deconvolution**: B cell / plasma cell signatures in bulk RNA-seq
  indicate humoral immune activity.

---

## Summary

| Concept | Key Point |
|---------|-----------|
| B cell development | Bone marrow → V(D)J → self-tolerance check → mature |
| Antibody structure | Y-shaped: Fab (binding) + Fc (effector function) |
| Isotypes | IgM (first), IgG (main), IgA (mucosal), IgE (allergy), IgD (surface) |
| Diversity mechanisms | V(D)J, junctional diversity, SHM, CSR |
| Germinal centre | Training loop: mutate, select, output plasma + memory cells |
