# Cells of the Immune System

## Overview

Your body runs an operating system — and the immune system is its security
framework. Just as an OS has different processes for different jobs (firewall,
antivirus scanner, intrusion detection), the immune system deploys specialised
cell types, each with a defined role.

This module introduces the major players.

---

## Innate vs Adaptive Immunity

| Feature | Innate Immunity | Adaptive Immunity |
|---------|----------------|-------------------|
| Speed | Minutes–hours | Days–weeks (first encounter) |
| Specificity | Broad patterns (PAMPs) | Highly specific (epitopes) |
| Memory | None | Yes — immunological memory |
| CS analogy | **Firewall / IDS rules** | **Machine-learning classifier** |

**Innate immunity** is the first line of defence. It recognises conserved
molecular patterns on pathogens (PAMPs — pathogen-associated molecular
patterns) via pattern-recognition receptors (PRRs). Think of it as a firewall
with a fixed rule set: fast, but not specific to novel threats.

**Adaptive immunity** takes longer to activate but learns. B cells and T cells
rearrange their receptor genes (V(D)J recombination) to generate enormous
diversity — analogous to training a classifier on labelled data. After
clearance, memory cells persist for rapid recall.

---

## Key Cell Types

### Innate Cells

| Cell | Role | CS Analogy |
|------|------|------------|
| **Neutrophil** | First responder; phagocytosis, NETs | Short-lived worker thread |
| **Macrophage** | Phagocytosis, antigen presentation, cytokines | Long-running daemon + logger |
| **Dendritic cell (DC)** | Antigen capture → presentation to T cells | Router / message broker |
| **Natural killer (NK) cell** | Kills virus-infected & tumour cells (no prior activation) | Heuristic-based anomaly detector |
| **Mast cell** | Releases histamine; allergy & parasite defence | Event emitter |

### Adaptive Cells

| Cell | Role | CS Analogy |
|------|------|------------|
| **B cell** | Produces antibodies (immunoglobulins) | Key-value store (antigen → antibody) |
| **Helper T cell (CD4⁺)** | Orchestrates immune responses via cytokines | Scheduler / orchestrator |
| **Cytotoxic T cell (CD8⁺)** | Kills infected / abnormal cells directly | Kill process by PID |
| **Regulatory T cell (Treg)** | Suppresses excessive responses | Rate limiter |
| **Memory B / T cell** | Long-lived; rapid recall on re-exposure | Cache layer |

---

## Antigen Presentation — The Routing Layer

Cells communicate what they've found via **MHC molecules** (Major
Histocompatibility Complex):

- **MHC class I** — present on *all* nucleated cells. Displays intracellular
  peptides (self or viral). Recognised by CD8⁺ T cells.
  *Analogy: every process reports its loaded modules to the kernel.*

- **MHC class II** — present on professional antigen-presenting cells (APCs):
  dendritic cells, macrophages, B cells. Displays extracellular peptides.
  Recognised by CD4⁺ T cells.
  *Analogy: specialised log aggregators reporting external events.*

---

## Bioinformatics Relevance

- **scRNA-seq cell-type annotation**: You classify immune cells by marker gene
  expression (e.g., CD3 for T cells, CD19 for B cells). Understanding what
  these markers mean is essential.
- **Spatial transcriptomics**: Cell neighbourhoods matter — a macrophage next
  to a tumour cell has different signalling than one in healthy tissue.
- **Ligand–receptor analysis**: Tools like CellChat and NicheNet model cell
  communication. Knowing which cells talk to which (and via what signals)
  is prerequisite knowledge.
- **Immune deconvolution**: Algorithms like CIBERSORTx estimate immune cell
  fractions from bulk RNA-seq. Understanding cell types is step zero.

---

## Summary

| Concept | Key Point |
|---------|-----------|
| Innate immunity | Fast, pattern-based, no memory |
| Adaptive immunity | Slow start, specific, learns and remembers |
| Antigen presentation | MHC I (all cells → CD8⁺), MHC II (APCs → CD4⁺) |
| Immune cells | Each type has a defined role, like OS processes |
