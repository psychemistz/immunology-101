# Computational Immunology

## Overview

This capstone module brings together all prior immunology concepts and connects
them to the **bioinformatics tools and pipelines** you'll use in practice.
Computational immunology sits at the intersection of immunology, genomics, and
data science — applying algorithms to decode immune function from high-
throughput data.

---

## The Computational Immunology Landscape

| Domain | Key Question | Tools/Methods |
|--------|-------------|---------------|
| **Immune cell identification** | What cells are in my sample? | scRNA-seq clustering, CIBERSORTx, flow cytometry gating |
| **Receptor repertoire analysis** | What antigens can these cells recognise? | BCR/TCR-seq, AIRR tools, VDJtools |
| **Antigen prediction** | Which peptides will trigger an immune response? | NetMHCpan, IEDB tools, pVACtools |
| **Cell communication** | Which cells are talking to which? | CellChat, NicheNet, CellPhoneDB |
| **Spatial immune architecture** | Where are immune cells in tissue? | Spatial transcriptomics, Squidpy, CODEX |
| **Systems immunology** | How do immune components integrate? | Network analysis, multi-omics integration |

---

## Key Pipelines & Workflows

### 1. Immune Cell Type Annotation (scRNA-seq)

```
Raw counts → QC/filtering → Normalisation → Clustering →
Marker gene identification → Cell type annotation
```

Key markers (from Module 01):
- T cells: CD3E, CD4, CD8A
- B cells: CD19, MS4A1 (CD20)
- NK cells: NKG7, GNLY
- Macrophages: CD68, CD163
- Dendritic cells: ITGAX (CD11c), CLEC4C

Tools: Scanpy, Seurat, CellTypist, scType

### 2. Immune Deconvolution (Bulk RNA-seq)

```
Bulk expression matrix → Signature matrix selection →
Deconvolution algorithm → Cell fraction estimates
```

Estimates immune cell proportions from bulk data when single-cell
resolution isn't available.

Tools: CIBERSORTx, MCP-counter, TIMER, EPIC, quanTIseq

### 3. BCR/TCR Repertoire Analysis

```
VDJ-enriched sequencing → Assembly → V/D/J annotation →
Clonotype calling → Diversity metrics → Clonal expansion analysis
```

Connects receptor sequence to immune specificity (Modules 03–04).

Tools: Cell Ranger VDJ, IgBLAST, MiXCR, Immcantation, scRepertoire

### 4. Neoantigen Prediction Pipeline

```
Tumour WES/WGS → Somatic variant calling → HLA typing →
Peptide-MHC binding prediction → Neoantigen ranking →
Validation (mass spec / T cell assays)
```

Combines Modules 04 (T cells), 06 (tolerance), 08 (tumour immunology).

Tools: pVACtools, NetMHCpan, OptiType (HLA typing), MuPeXI

### 5. Ligand–Receptor Communication Analysis

```
scRNA-seq with cell type labels → L-R database lookup →
Statistical testing for enriched interactions →
Communication network visualisation
```

Maps the cytokine/chemokine signalling from Module 05.

Tools: CellChat, CellPhoneDB, NicheNet, LIANA

### 6. Spatial Immune Mapping

```
Spatial transcriptomics data → Cell type deconvolution/annotation →
Spatial autocorrelation → Neighbourhood enrichment →
Co-localisation analysis
```

Reveals tissue-level immune architecture — where cells are, not just what.

Tools: Squidpy, Giotto, RCTD, Cell2location, SpatialData

---

## Key Databases

| Database | Content | URL |
|----------|---------|-----|
| **IEDB** | Immune epitopes (B cell, T cell, MHC ligands) | iedb.org |
| **IMGT** | Immunoglobulin and TCR gene nomenclature | imgt.org |
| **ImmPort** | Shared immunology data repository (NIAID-funded) | immport.org |
| **VDJdb** | Curated TCR-epitope associations | vdjdb.cdr3.net |
| **TCIA** | Tumour immune characterisation data | tcia.at |

---

## Integrative Analysis: Putting It Together

A real-world immunology project might combine:

1. **scRNA-seq** → identify immune cell types and states (Module 01)
2. **TCR-seq** → link T cell clonotypes to phenotype (Module 04)
3. **Neoantigen prediction** → find immunogenic tumour mutations (Module 08)
4. **Spatial transcriptomics** → map immune cells in tissue context (Module 02)
5. **CellChat** → infer cytokine-mediated communication (Module 05)
6. **Clinical correlation** → link immune features to patient outcomes

*Analogy: each tool is a microservice — the real power comes from the
integrated pipeline that combines them.*

---

## Bioinformatics Relevance

This entire module IS the bioinformatics relevance section. Every concept
from Modules 01–09 connects to a computational method:

| Module | Computational Connection |
|--------|------------------------|
| 01 Immune cells | Cell type annotation, deconvolution |
| 02 Innate immunity | ISG signatures, pathway enrichment |
| 03 Antibodies | BCR-seq, antibody engineering |
| 04 T cells | TCR-seq, neoantigen prediction, HLA typing |
| 05 Cytokines | Ligand-receptor analysis, pathway analysis |
| 06 Tolerance | HLA-disease association (GWAS), Treg signatures |
| 07 Memory/vaccination | Systems vaccinology, repertoire tracking |
| 08 Tumour immunology | TME deconvolution, biomarker discovery |
| 09 Infectious disease | Phylogenetics, host-pathogen interactions |

---

## Summary

| Concept | Key Point |
|---------|-----------|
| Cell annotation | scRNA-seq clustering + marker genes → cell identity |
| Deconvolution | Estimate immune fractions from bulk RNA-seq |
| Repertoire analysis | BCR/TCR-seq → diversity, clonality, specificity |
| Neoantigen prediction | Mutations + HLA typing + binding prediction |
| Cell communication | Ligand-receptor analysis from expression data |
| Spatial analysis | Where immune cells are in tissue, not just what |
