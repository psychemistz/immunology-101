# Infection & Immune Evasion

## Overview

Pathogens and the immune system are locked in an evolutionary **arms race**.
While the immune system has developed sophisticated detection and killing
mechanisms, pathogens have evolved equally clever evasion strategies —
analogous to **exploit techniques and obfuscation** in cybersecurity.

This module covers how different pathogen classes interact with immunity
and the strategies they use to survive.

---

## Pathogen Classes & Immune Responses

| Pathogen Type | Examples | Primary Defence | CS Analogy |
|---------------|---------|-----------------|------------|
| **Extracellular bacteria** | *Staphylococcus*, *Streptococcus* | Antibodies, complement, neutrophils | Blocking known malicious IPs |
| **Intracellular bacteria** | *Mycobacterium*, *Listeria* | Th1 → macrophage activation | Detecting rootkits in running processes |
| **Viruses** | Influenza, HIV, SARS-CoV-2 | CTLs, interferons, antibodies | Antivirus + sandbox execution |
| **Fungi** | *Candida*, *Aspergillus* | Th17 → neutrophils, dectin-1 | Specialised malware scanner |
| **Parasites (helminths)** | Tapeworms, schistosomes | Th2 → IgE, eosinophils, mast cells | Custom defence module |
| **Protozoa** | *Plasmodium* (malaria) | Mixed Th1/Th2, antibodies | Multi-layered defence |

---

## Viral Evasion Strategies

Viruses are masters of immune evasion:

| Strategy | Mechanism | Example | CS Analogy |
|----------|-----------|---------|------------|
| **Antigenic variation** | Mutate surface proteins | Influenza (antigenic drift/shift) | Polymorphic malware |
| **MHC I downregulation** | Block peptide presentation | Herpes viruses (CMV) | Disabling logging |
| **Interferon antagonism** | Block IFN signalling | SARS-CoV-2 (NSP proteins) | Disabling the firewall |
| **Latency** | Hide in host genome, no protein expression | HIV, EBV, HSV | Rootkit — dormant until triggered |
| **Molecular mimicry** | Express host-like molecules | EBV (IL-10 homologue) | Spoofing trusted credentials |
| **Decoy receptors** | Secrete soluble cytokine receptors | Poxviruses | Intercepting alert messages |

---

## Bacterial Evasion Strategies

| Strategy | Mechanism | Example |
|----------|-----------|---------|
| **Capsule** | Prevents phagocytosis and complement | *Streptococcus pneumoniae* |
| **Intracellular survival** | Escape phagolysosome | *Mycobacterium tuberculosis* |
| **Biofilm formation** | Physical barrier to immune cells | *Pseudomonas aeruginosa* |
| **Toxin secretion** | Kill immune cells or subvert signalling | *Staphylococcus aureus* (leukocidins) |
| **Antigenic variation** | Phase variation of surface antigens | *Neisseria* species |
| **Superantigen production** | Non-specific T cell activation → cytokine storm | *Staphylococcus* (TSST-1) |

---

## Parasite Evasion

Large parasites (helminths) face unique challenges — they cannot hide inside
cells. Their strategies include:

- **Tegument shedding**: Shed surface coat with bound antibodies.
- **Immune modulation**: Skew toward Th2/Treg responses, dampening Th1.
- **Molecular disguise**: Coat with host molecules.
- **Long lifespan**: Outlast immune responses (some helminths live years).

---

## Superinfection & Immune Suppression

Some pathogens actively suppress the immune system:

- **HIV**: Destroys CD4⁺ T cells → progressive immunodeficiency (AIDS).
- **Measles**: Causes "immune amnesia" — destroys memory B and T cells.
- **Tuberculosis**: Prevents phagolysosome fusion in macrophages.

*Analogy: these pathogens don't just evade detection — they attack the
security infrastructure itself (like compromising the SIEM).*

---

## Bioinformatics Relevance

- **Pathogen genomics**: Whole-genome sequencing tracks viral evolution,
  transmission chains, and resistance mutations.
- **Host-pathogen interaction networks**: Databases (HPIDB, VirHostNet) map
  protein-protein interactions between pathogens and host immune proteins.
- **Differential expression**: Comparing infected vs uninfected transcriptomes
  reveals host response signatures and pathogen evasion effects.
- **Phylogenetics**: Tracking antigenic drift in influenza and SARS-CoV-2
  informs vaccine strain selection.

---

## Summary

| Concept | Key Point |
|---------|-----------|
| Pathogen diversity | Bacteria, viruses, fungi, parasites each face different immune arms |
| Viral evasion | Antigenic variation, MHC downregulation, IFN antagonism, latency |
| Bacterial evasion | Capsules, intracellular survival, biofilms, toxins |
| Parasite evasion | Immune modulation, tegument shedding, molecular disguise |
| Immune suppression | HIV (CD4 loss), measles (immune amnesia), TB (phagosome escape) |
