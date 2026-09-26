from Bio import AlignIO

alignment = AlignIO.read("gyrB_alignment.aln", "clustal")

print("Number of sequences:", len(alignment))
print("Alignment length:", alignment.get_alignment_length())

for record in alignment:
    print(record.id, "length =", len(record.seq))