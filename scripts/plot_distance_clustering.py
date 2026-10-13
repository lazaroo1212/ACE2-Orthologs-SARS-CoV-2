from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results" / "generated"
OUTPUT.mkdir(parents=True, exist_ok=True)


import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

# Sample data
data = {
    "Species": [
        "Human", "Chimpanzee", "Gorilla", "Cat", "Rat", "Wild boar",
        "Cow", "Koala", "Bat", "Mouse", "Opossum", "Chicken",
        "Platypus", "Dog"
    ],
    "Distance": [0, 0, 0, 21, 34, 34, 38, 42, 43, 45, 46, 88, 109, 113]
}

df = pd.DataFrame(data)

# Create a 2D array from the 1D distances (required by linkage)
X = df["Distance"].values.reshape(-1, 1)

# Cluster one-dimensional values; this is not a species phylogeny
Z = linkage(X, method='average')  # UPGMA

# Plot the dendrogram horizontally
plt.figure(figsize=(10, 8))
dendrogram(Z, labels=df["Species"].values, orientation='left')
plt.title("Exploratory clustering of distances to human ACE2")
plt.xlabel("Difference between supplied distance values")
plt.ylabel("Species")
plt.tight_layout()
plt.savefig(OUTPUT / "distance_clustering.png", dpi=200)
plt.show()
