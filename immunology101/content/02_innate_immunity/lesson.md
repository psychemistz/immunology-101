# Innate Immunity: First Line of Defence

## Overview

If the immune system is your body's security framework, innate immunity is the
**firewall** — a set of hard-coded rules that block common threats instantly,
without needing prior exposure. It provides broad, rapid protection while the
adaptive system spins up.

This module dives deeper into the mechanisms, receptors, and effector responses
of innate immunity.

---

## Physical & Chemical Barriers

Before immune cells even engage, the body has passive defences:

| Barrier | Mechanism | CS Analogy |
|---------|-----------|------------|
| Skin (epithelium) | Physical wall, antimicrobial peptides | Network perimeter / DMZ |
| Mucous membranes | Traps pathogens, contains lysozyme | Input sanitisation layer |
| Stomach acid (pH ~2) | Destroys ingested microbes | Data validation filter |
| Commensal microbiota | Competitive exclusion of pathogens | Trusted process whitelist |

---

## Pattern Recognition Receptors (PRRs)

Innate immunity detects threats via **pattern recognition receptors** that bind
conserved microbial structures (**PAMPs** — pathogen-associated molecular
patterns) and damage signals (**DAMPs**).

| PRR Family | Location | Ligand Examples | CS Analogy |
|------------|----------|-----------------|------------|
| **Toll-like receptors (TLRs)** | Cell surface / endosomes | LPS (TLR4), dsRNA (TLR3) | Regex pattern matcher |
| **NOD-like receptors (NLRs)** | Cytoplasm | Peptidoglycan, flagellin | Inline code scanner |
| **RIG-I-like receptors (RLRs)** | Cytoplasm | Viral RNA | Signature-based antivirus |
| **C-type lectin receptors** | Cell surface | Fungal β-glucan | File-type detector |

**Key principle**: PRRs match *patterns*, not specific antigens — like a firewall
rule that blocks all traffic from suspicious port ranges rather than a single IP.

---

## Effector Mechanisms

Once a threat is detected, innate immunity deploys multiple responses:

### Phagocytosis

Neutrophils and macrophages engulf and destroy pathogens in phagolysosomes.
*Analogy: garbage collector reclaiming memory from terminated processes.*

### Complement System

A cascade of ~30 plasma proteins that:
- **Opsonise** pathogens (tag for phagocytosis) — like adding metadata tags
- **Recruit** immune cells via anaphylatoxins (C3a, C5a) — like alert notifications
- **Lyse** pathogens via the membrane attack complex (MAC) — like a kill signal

### Inflammation

The hallmarks — redness, heat, swelling, pain — result from vasodilation and
immune cell recruitment. Cytokines (TNF-α, IL-1, IL-6) coordinate this.
*Analogy: incident response — log alerts, page on-call, escalate priority.*

### Interferons (Type I)

IFN-α and IFN-β are released by virus-infected cells, warning neighbours to
upregulate antiviral defences.
*Analogy: a broadcast message telling all nodes to enable strict firewall mode.*

---

## The Inflammasome

NLR proteins (especially NLRP3) assemble into **inflammasomes** — multiprotein
complexes that activate caspase-1, which processes pro-IL-1β and pro-IL-18 into
their active forms. Dysregulated inflammasome activity is linked to
autoinflammatory diseases.

*Analogy: a circuit breaker that triggers an emergency shutdown protocol.*

---

## Bioinformatics Relevance

- **Bulk/scRNA-seq**: Innate immune activation signatures (e.g., interferon-
  stimulated genes — ISGs) are key in infection and tumour studies.
- **Pathway enrichment**: GO terms like "innate immune response" and
  "inflammatory response" frequently appear in differential expression analyses.
- **PRR variant analysis**: TLR polymorphisms (e.g., TLR4 Asp299Gly) are studied
  in GWAS for infection susceptibility.
- **Spatial transcriptomics**: Mapping innate cell infiltration patterns reveals
  tissue-level immune architecture.

---

## Summary

| Concept | Key Point |
|---------|-----------|
| Barriers | Skin, mucosa, acid, microbiota — passive first line |
| PRRs | Recognise PAMPs/DAMPs via pattern matching (TLRs, NLRs, RLRs) |
| Phagocytosis | Engulf and destroy — the garbage collector |
| Complement | Opsonise, recruit, lyse — a protein cascade |
| Inflammation | Coordinated recruitment via cytokines — incident response |
| Interferons | Antiviral broadcast signal |
