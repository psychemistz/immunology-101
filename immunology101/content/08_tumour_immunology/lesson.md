# Tumour Immunology

## Overview

The immune system constantly surveys for abnormal cells, including cancer cells.
Tumours, however, evolve strategies to evade immune detection — a process
strikingly similar to **adversarial attacks** on machine learning models.

This module covers immune surveillance of tumours, evasion mechanisms, and
modern immunotherapies that aim to restore anti-tumour immunity.

---

## Cancer Immunosurveillance

The immune system can recognise and eliminate nascent tumour cells through:

- **Tumour-associated antigens (TAAs)**: Overexpressed normal proteins
  (e.g., HER2, EGFR).
- **Tumour-specific antigens / neoantigens**: Mutated proteins unique to the
  tumour, presented on MHC class I. *These are the most specific targets.*
- **Stress ligands**: NKG2D ligands (MICA/MICB) on stressed/transformed cells,
  recognised by NK cells.

| Effector | Mechanism | CS Analogy |
|----------|-----------|------------|
| CD8⁺ CTLs | Recognise neoantigens on MHC I | Signature-based detection |
| NK cells | Kill cells lacking MHC I ("missing self") | Anomaly detection — missing expected header |
| Macrophages (M1) | Phagocytosis, pro-inflammatory cytokines | Garbage collector |
| γδ T cells | Recognise stress ligands without MHC restriction | Heuristic scanner |

---

## The Three Es: Elimination, Equilibrium, Escape

| Phase | Description | CS Analogy |
|-------|-------------|------------|
| **Elimination** | Immune system destroys nascent tumour cells | Malware detected and quarantined |
| **Equilibrium** | Tumour persists but is controlled by immune pressure | Arms race — ongoing detection vs evasion |
| **Escape** | Tumour evolves to evade immunity; clinical cancer | Adversarial attack succeeds |

---

## Tumour Immune Evasion Mechanisms

| Mechanism | How It Works | CS Analogy |
|-----------|-------------|------------|
| **MHC I downregulation** | Hide neoantigens from CD8⁺ T cells | Stripping metadata / response headers |
| **PD-L1 expression** | Engage PD-1 checkpoint → T cell exhaustion | Rate limiting the attacker |
| **Treg recruitment** | Suppress anti-tumour T cells in the microenvironment | Deploying a rogue moderator |
| **Immunosuppressive cytokines** | TGF-β, IL-10 dampen immune responses | Jamming the communication channel |
| **Metabolic competition** | Tumour consumes nutrients, starving T cells | Resource starvation attack |
| **Neoantigen loss** | Immune editing removes immunogenic mutations | Adversarial retraining — remove flagged features |

---

## Immunotherapy

### Immune Checkpoint Inhibitors

Checkpoint inhibitors block inhibitory receptors, releasing the "brakes" on
T cells:

| Target | Drug Examples | Mechanism |
|--------|-------------|-----------|
| **PD-1** | Pembrolizumab, nivolumab | Unblock exhausted T cells |
| **PD-L1** | Atezolizumab, durvalumab | Prevent tumour from engaging PD-1 |
| **CTLA-4** | Ipilimumab | Enhance T cell priming and activation |

### Other Immunotherapies

| Approach | Mechanism | CS Analogy |
|----------|-----------|------------|
| **CAR-T cells** | Engineered T cells with synthetic antigen receptor | Custom-built exploit targeting specific vulnerability |
| **Bispecific antibodies** | Bridge T cells to tumour cells | API adapter / middleware |
| **Cancer vaccines** | Prime immune response against tumour antigens | Threat intelligence update |
| **Adoptive cell therapy** | Expand tumour-infiltrating lymphocytes (TILs) ex vivo | Scaling up the security team |

---

## Tumour Microenvironment (TME)

The TME is a complex ecosystem of tumour cells, immune cells, stromal cells,
and vasculature. Its composition predicts response to immunotherapy:

- **Hot tumours**: High T cell infiltration → likely to respond to checkpoint inhibitors.
- **Cold tumours**: Low T cell infiltration → need combination strategies.

---

## Bioinformatics Relevance

- **Neoantigen prediction**: Pipelines (pVACtools) combine somatic mutation
  calls with HLA typing and MHC binding prediction.
- **TME deconvolution**: CIBERSORTx, TIMER, and MCP-counter estimate immune
  cell fractions from bulk RNA-seq.
- **Spatial transcriptomics**: Mapping immune cell proximity to tumour cells
  reveals functional immune niches.
- **Biomarker discovery**: Tumour mutational burden (TMB), MSI status, and
  PD-L1 expression predict checkpoint inhibitor response.

---

## Summary

| Concept | Key Point |
|---------|-----------|
| Immunosurveillance | Immune system detects tumours via neoantigens and stress signals |
| Three Es | Elimination → equilibrium → escape |
| Evasion | MHC loss, PD-L1, Tregs, immunosuppressive cytokines |
| Checkpoint inhibitors | Release brakes on T cells (anti-PD-1, anti-CTLA-4) |
| TME | Hot vs cold tumours determine immunotherapy response |
