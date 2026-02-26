# Cytokines & Cell Signalling

## Overview

Immune cells don't work in isolation — they communicate through **cytokines**,
small signalling proteins that act as the immune system's **message queue**.
Like a pub/sub system, cytokines enable one cell to broadcast instructions to
many listeners, coordinating complex multi-cell responses.

This module covers the major cytokine families, signalling modes, and their
roles in shaping immune responses.

---

## What Are Cytokines?

Cytokines are small (8–40 kDa) secreted proteins that bind specific receptors
on target cells, triggering intracellular signalling cascades. They are
produced by virtually all immune cells and many non-immune cells.

| Property | Description | CS Analogy |
|----------|-------------|------------|
| Pleiotropic | One cytokine, many effects on different cells | Polymorphic function |
| Redundant | Multiple cytokines can have overlapping effects | Failover / redundancy |
| Synergistic | Combined effect greater than sum | Parallel execution speedup |
| Antagonistic | One cytokine inhibits another's action | Mutex / lock contention |

---

## Signalling Modes

| Mode | Range | Example | CS Analogy |
|------|-------|---------|------------|
| **Autocrine** | Self (same cell) | T cell producing IL-2 to stimulate its own proliferation | Recursive function call |
| **Paracrine** | Nearby cells | Macrophage releasing TNF-α to activate local endothelium | Local message queue |
| **Endocrine** | Distant (via blood) | IL-6 causing liver to produce acute-phase proteins | Remote API call |

---

## Major Cytokine Families

### Interleukins (ILs)

| Cytokine | Source | Key Function |
|----------|--------|--------------|
| **IL-1β** | Macrophages | Pro-inflammatory; fever; inflammasome product |
| **IL-2** | T cells | T cell proliferation and survival |
| **IL-4** | Th2 cells | B cell class switch to IgE; Th2 polarisation |
| **IL-6** | Macrophages, T cells | Acute-phase response; Th17 differentiation |
| **IL-10** | Tregs, macrophages | Anti-inflammatory; immune suppression |
| **IL-12** | Dendritic cells | Th1 polarisation; NK cell activation |
| **IL-17** | Th17 cells | Neutrophil recruitment; mucosal defence |

### Interferons (IFNs)

| Type | Members | Function |
|------|---------|----------|
| **Type I** | IFN-α, IFN-β | Antiviral state; MHC I upregulation |
| **Type II** | IFN-γ | Macrophage activation; Th1 responses |
| **Type III** | IFN-λ | Mucosal antiviral defence |

### Tumour Necrosis Factors (TNFs)

- **TNF-α**: Pro-inflammatory; endothelial activation; can induce apoptosis.
- **Lymphotoxin (TNF-β)**: Lymph node organogenesis.

### Chemokines

Chemotactic cytokines that direct cell migration along concentration gradients.
*Analogy: routing protocols — cells follow the gradient to the source.*

| Family | Example | Attracts |
|--------|---------|----------|
| CXC | CXCL8 (IL-8) | Neutrophils |
| CC | CCL2 (MCP-1) | Monocytes |
| CX3C | CX3CL1 | Monocytes, NK cells |

---

## Signalling Pathways

Cytokine binding triggers intracellular cascades:

- **JAK-STAT pathway**: Most interleukins and interferons. JAK kinases
  phosphorylate STAT transcription factors.
  *Analogy: event handler → callback → state update.*
- **NF-κB pathway**: TNF-α, IL-1. Activates pro-inflammatory gene expression.
  *Analogy: emergency broadcast system — master switch for inflammation.*
- **MAPK pathway**: Growth factors, some cytokines. Controls proliferation
  and differentiation.

---

## Cytokine Storm

When cytokine release becomes uncontrolled, the resulting **cytokine storm**
causes massive inflammation, tissue damage, and potentially organ failure.
This was a key driver of severe COVID-19.

*Analogy: a feedback loop with no rate limiter — messages amplify endlessly
until the system crashes (DDoS from within).*

---

## Bioinformatics Relevance

- **Ligand–receptor analysis**: CellChat, NicheNet, and CellPhoneDB model
  cytokine-mediated cell communication from scRNA-seq data.
- **Pathway analysis**: JAK-STAT and NF-κB signatures are standard gene sets
  in GSEA and pathway enrichment.
- **Cytokine profiling**: Luminex/multiplex assays generate high-dimensional
  cytokine data analysed with clustering and dimensionality reduction.
- **Spatial transcriptomics**: Mapping cytokine gradients in tissue sections
  reveals signalling microenvironments.

---

## Summary

| Concept | Key Point |
|---------|-----------|
| Cytokines | Small signalling proteins — the immune message queue |
| Properties | Pleiotropic, redundant, synergistic, antagonistic |
| Modes | Autocrine (self), paracrine (local), endocrine (distant) |
| Key families | Interleukins, interferons, TNFs, chemokines |
| Signalling | JAK-STAT, NF-κB, MAPK — event-driven cascades |
| Cytokine storm | Uncontrolled amplification — system crash |
