from Bio import AlignIO

alignment = AlignIO.read("gyrB_alignment.aln", "clustal")

conserved_positions = []

for position in range(alignment.get_alignment_length()):

    column = alignment[:, position]

    # Ignore columns containing gaps
    if "-" not in column and len(set(column)) == 1:
        conserved_positions.append(position + 1)

print("Total alignment positions:", alignment.get_alignment_length())
print("Completely conserved amino-acid positions:", len(conserved_positions))

print("\nFirst 50 conserved positions:")
print(conserved_positions[:50])