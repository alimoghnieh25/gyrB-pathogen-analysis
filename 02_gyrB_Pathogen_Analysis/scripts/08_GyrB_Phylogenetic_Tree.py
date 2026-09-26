from Bio.Phylo.TreeConstruction import DistanceMatrix, DistanceTreeConstructor
from Bio import Phylo
import matplotlib.pyplot as plt

# Sequence IDs in the order you want them in the matrix
seq_ids = ["NP_064724.1", "XYW55554.1", "BBE11218.1", "CDO11772.1", "QGJ10764.1", "NP_462735.1"]

# Lower-triangle distance matrix (must match Biopython's expected format:
# row i has i+1 values, from the diagonal leftward)
matrix_data = [
    [0.0],
    [0.3213, 0.0],
    [0.3134, 0.2584, 0.0],
    [0.3172, 0.2466, 0.2204, 0.0],
    [0.3176, 0.2481, 0.2179, 0.0498, 0.0],
    [0.3238, 0.2531, 0.2267, 0.0510, 0.0336, 0.0],
]

dm = DistanceMatrix(names=seq_ids, matrix=matrix_data)

constructor = DistanceTreeConstructor()

# Neighbor-Joining tree (generally preferred over UPGMA — doesn't assume a constant molecular clock)
nj_tree = constructor.nj(dm)

print("=== Neighbor-Joining Tree ===")
Phylo.draw_ascii(nj_tree)

# Also build UPGMA for comparison
upgma_tree = constructor.upgma(dm)
print("\n=== UPGMA Tree ===")
Phylo.draw_ascii(upgma_tree)

# Save trees in Newick format (standard phylogenetics file format)
Phylo.write(nj_tree, "gyrB_nj_tree.nwk", "newick")
Phylo.write(upgma_tree, "gyrB_upgma_tree.nwk", "newick")

print("\nSaved trees to gyrB_nj_tree.nwk and gyrB_upgma_tree.nwk")

# Draw and save a proper figure of the NJ tree
fig = plt.figure(figsize=(8, 6))
axes = fig.add_subplot(1, 1, 1)
Phylo.draw(nj_tree, axes=axes, do_show=False)
plt.savefig("gyrB_nj_tree.png", dpi=300, bbox_inches="tight")
print("Saved tree figure to gyrB_nj_tree.png")