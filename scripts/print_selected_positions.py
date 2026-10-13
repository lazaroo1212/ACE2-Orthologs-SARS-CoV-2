from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results" / "generated"
OUTPUT.mkdir(parents=True, exist_ok=True)

from Bio import SeqIO

# Define the function to extract specific positions from a sequence
def s(seq):
    positions = [23, 29, 30, 33, 34, 37, 40, 41, 44, 81, 82, 89, 352, 353, 354, 392]
    return ''.join(seq[pos] if pos < len(seq) else '-' for pos in positions)

# Ruta al archivo FASTA
fasta_path = ROOT / "data/raw/ace2_refseq_protein.fasta"

# Leer el archivo FASTA y aplicar la función a cada secuencia
for record in SeqIO.parse(fasta_path, "fasta"):
    seq_id = record.id
    sequence = str(record.seq)
    motif = s(sequence)
    print(f"{seq_id}\t{motif}")


