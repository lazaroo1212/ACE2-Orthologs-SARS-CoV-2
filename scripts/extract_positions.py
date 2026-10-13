from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results" / "generated"
OUTPUT.mkdir(parents=True, exist_ok=True)

# extract_custom_sequences.py

# Define the positions of interest (0-based indexing)
positions = [23, 29, 30, 33, 34, 37, 40, 41, 44, 81, 82, 89, 352, 353, 354, 392]

# Dictionary to store sequences from FASTA
sequences = {}

# Read the FASTA file
fasta_path = ROOT / "data/raw/ace2_refseq_protein.fasta"
with open(fasta_path, "r") as file:
    current_id = ""
    current_seq = []
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            if current_id:
                sequences[current_id] = ''.join(current_seq)
            current_id = line[1:]  # Remove '>'
            current_seq = []
        else:
            current_seq.append(line)
    if current_id:
        sequences[current_id] = ''.join(current_seq)

# Generate custom sequences
custom_sequences = {
    id_: ''.join(seq[pos] for pos in positions if pos < len(seq))
    for id_, seq in sequences.items()
}

# Write results to output file
output_path = OUTPUT / "custom_sequences.fasta"
with open(output_path, "w") as out_file:
    for id_, custom_seq in custom_sequences.items():
        out_file.write(f">{id_}\n{custom_seq}\n")

print(f"Custom sequences written to {output_path}")
