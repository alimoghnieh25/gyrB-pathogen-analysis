from Bio import SeqIO

filename = "gyrB_proteins.fasta"

records = list(SeqIO.parse(filename, "fasta"))

print("Number of sequences:", len(records))

for record in records:
    print(record.id, "length =", len(record.seq))