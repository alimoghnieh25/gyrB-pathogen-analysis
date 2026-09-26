import matplotlib
matplotlib.use("Agg")  # non-interactive backend — draws straight to file, no GUI window
import matplotlib.pyplot as plt
from Bio import Phylo

# Load the tree you already built and saved
tree = Phylo.read("gyrB_nj_tree.nwk", "newick")

fig = plt.figure(figsize=(10, 6))
axes = fig.add_subplot(1, 1, 1)

Phylo.draw(tree, axes=axes, do_show=False)

plt.savefig("gyrB_nj_tree.png", dpi=300, bbox_inches="tight")
plt.close(fig)  # explicitly close the figure to free memory/resources

print("Saved tree figure to gyrB_nj_tree.png")