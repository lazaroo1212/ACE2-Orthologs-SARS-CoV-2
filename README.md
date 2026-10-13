# ACE2 Orthologs and SARS-CoV-2

A group project completed for **Algorithms in Biology**, part of the BSc in Bioinformatics at the Universitat Politècnica de Catalunya (UPC).

**Authors:** David Lázaro Alfranca, Luis Carlos Ospina and Jan Jardí.

## Overview

This project explores variation in ACE2 protein sequences across species and its potential relationship with susceptibility to SARS-CoV-2.

We compared full-length sequences and a subset of 16 positions of interest, using sequence alignment, Python scripts and tree visualisation. The analysis also examines why sequence similarity alone is insufficient to establish susceptibility or resistance.

## Research question

To what extent can differences in ACE2 sequences help us understand differences in susceptibility to SARS-CoV-2 across species?

## Approach

1. Collect ACE2 protein sequences in FASTA format.
2. Explore multiple sequence alignment approaches.
3. Extract 16 selected sequence positions using Python.
4. Align the extracted sequences with Clustal Omega.
5. Generate a tree with FastTree and visualise it with Biopython.
6. Discuss the results and their biological limitations.

The accompanying presentation also discusses MAFFT and T-COFFEE.

## Repository structure

```text
scripts/              Python scripts
data/raw/            Original full-length ACE2 sequences
data/processed/      Existing selected-sequence input for the tree workflow
results/original/     Preserved coursework outputs
results/generated/    New outputs (ignored by Git)
presentation/         Original group presentation
requirements.txt      Python dependencies
```

## Setup and usage

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Clustal Omega (`clustalo`) and FastTree (`FastTree`) must be installed separately and available on PATH for tree generation. Dependency versions are not pinned; this is not a locked computational environment.

Run from the repository root:

```bash
python scripts/extract_positions.py
python scripts/print_selected_positions.py
python scripts/plot_distance_clustering.py
python scripts/build_sequence_tree.py
```

- `extract_positions.py` extracts selected positions and writes a FASTA file.
- `print_selected_positions.py` prints selected positions, using a dash for missing positions. It was separated from the original clustering script.
- `plot_distance_clustering.py` uses the manually entered values from the original script and saves a figure.
- `build_sequence_tree.py` aligns the existing `data/processed/custom_ace2_sequences.fasta`, runs FastTree and displays the tree. It does **not** use the newly extracted file automatically: the two inputs have not been established as equivalent.

Paths are resolved relative to the repository, so no personal filesystem paths are required. New results go to `results/generated/`; original outputs are preserved separately. Plot display requires a graphical environment.

## Interpretation and limitations

- The extraction scripts use **zero-based sequence indices**. These must be checked against the numbering and alignment of the reference sequence before interpreting them as equivalent biological positions across species.
- A tree based on only 16 selected residues captures limited sequence information and should not be treated as a definitive species phylogeny.
- The dendrogram in `plot_distance_clustering.py` clusters one-dimensional distances relative to human ACE2. It is not a phylogenetic reconstruction from a complete matrix of pairwise sequence distances.
- ACE2 sequence similarity alone does not establish susceptibility or resistance to SARS-CoV-2. Other factors include ACE2 expression, proteases such as TMPRSS2 and additional host–pathogen interactions.

## Presentation

[Download the original slides](presentation/ACE2_Orthologs_and_SARS-CoV-2.pptx)

[ACE2 Orthologs and SARS-CoV-2 — project presentation](https://docs.google.com/presentation/d/19XlnW8hMCTbZgnRDucnfug4ekN6KbkX3IV53708QfGg/edit)

Access depends on the presentation’s sharing settings.

## Project status

This repository preserves an educational analysis and its supporting scripts. This publication copy reorganises the original coursework files, updates paths, separates the two tasks previously combined in `tree.py`, and replaces the legacy Clustal Omega Python wrapper with a checked command-line call. It does not revise the biological analysis.

Python syntax was checked and position extraction was compared with the original script. The full alignment, tree and plotting workflow has not been revalidated.
