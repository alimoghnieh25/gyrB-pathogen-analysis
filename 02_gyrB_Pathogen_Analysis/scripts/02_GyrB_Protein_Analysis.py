from Bio import Entrez

Entrez.email = "alimoghnieh888@gmail.com"

accessions = [
    "NP_064724.1",
    "QGJ10764.1",
    "NP_462735.1",
    "CDO11772.1",
    "BBE11218.1",
    "XYW55554.1"
]

output_file = "gyrB_proteins.fasta"

with open(output_file, "w") as file:

    for accession in accessions:

        print("Downloading:", accession)

        handle = Entrez.efetch(
            db="protein",
            id=accession,
            rettype="fasta",
            retmode="text"
        )

        sequence = handle.read()

        file.write(sequence)

        handle.close()

print("All sequences saved!")