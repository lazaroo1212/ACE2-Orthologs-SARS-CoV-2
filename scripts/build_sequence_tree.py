from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results" / "generated"
OUTPUT.mkdir(parents=True, exist_ok=True)

from Bio import Phylo
import matplotlib.pyplot as plt
import subprocess

# Align sequences using Clustal Omega
subprocess.run([
    "clustalo", "--infile", str(ROOT / "data/processed/custom_ace2_sequences.fasta"),
    "--outfile", str(OUTPUT / "aligned.fasta"), "--force", "--verbose"
], check=True)

# Build tree using FastTree (correct syntax, no -prot flag needed)
with open(OUTPUT / "tree.nwk", "w") as treefile:
    subprocess.run(["FastTree", str(OUTPUT / "aligned.fasta")], stdout=treefile, check=True)

# Load and draw the tree
tree = Phylo.read(OUTPUT / "tree.nwk", "newick")
Phylo.draw(tree)
