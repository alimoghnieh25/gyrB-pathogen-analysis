from Bio import AlignIO
from Bio.Align import substitution_matrices
from itertools import combinations

alignment = AlignIO.read("gyrB_alignment.aln", "clustal")

num_sequences = len(alignment)
seq_ids = [record.id for record in alignment]

def p_distance(seq1, seq2):
    """
    Calculate simple p-distance: proportion of differing positions,
    ignoring columns where either sequence has a gap.
    """
    differences = 0
    compared_positions = 0

    for a, b in zip(seq1, seq2):
        if a == "-" or b == "-":
            continue  # skip gapped columns
        compared_positions += 1
        if a != b:
            differences += 1

    if compared_positions == 0:
        return None  # no comparable positions

    return differences / compared_positions

# Build a full pairwise distance matrix
distance_matrix = {}

for id1, id2 in combinations(seq_ids, 2):
    seq1 = str(alignment[seq_ids.index(id1)].seq)
    seq2 = str(alignment[seq_ids.index(id2)].seq)

    dist = p_distance(seq1, seq2)
    distance_matrix[(id1, id2)] = dist

# --- Print as a readable table ---
print("Pairwise p-distances (proportion of differing residues):\n")
print(f"{'':15}", end="")
for sid in seq_ids:
    print(f"{sid:>15}", end="")
print()

for id1 in seq_ids:
    print(f"{id1:15}", end="")
    for id2 in seq_ids:
        if id1 == id2:
            print(f"{0.0:15.4f}", end="")
        else:
            key = (id1, id2) if (id1, id2) in distance_matrix else (id2, id1)
            print(f"{distance_matrix[key]:15.4f}", end="")
    print()

# --- Save to CSV for use in tree-building step ---
import csv
with open("gyrB_distance_matrix.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([""] + seq_ids)
    for id1 in seq_ids:
        row = [id1]
        for id2 in seq_ids:
            if id1 == id2:
                row.append(0.0)
            else:
                key = (id1, id2) if (id1, id2) in distance_matrix else (id2, id1)
                row.append(round(distance_matrix[key], 4))
        writer.writerow(row)

print("\nSaved distance matrix to gyrB_distance_matrix.csv")