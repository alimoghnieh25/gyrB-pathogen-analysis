\# GyrB Pathogen Protein Analysis



Comparative bioinformatics analysis of the DNA gyrase subunit B (GyrB) protein across six bacterial pathogens, using Python and Biopython to investigate sequence conservation and evolutionary relationships.



\## Overview



This project retrieves real GyrB protein sequences from NCBI, aligns them, and analyzes conservation and phylogenetic relationships — moving from raw sequence data to a biologically interpretable result.



\*\*Pipeline:\*\*



Biological question → sequence retrieval (NCBI) → sequence verification →

multiple sequence alignment (CLUSTAL Omega) → conservation analysis →

distance matrix → phylogenetic tree → biological interpretation





\## Organisms analyzed



| Organism                      | Accession   | Length |

|--------------------------------|-------------|-------:|

| \*Pseudomonas aeruginosa\* PAO1 | NP\_064724.1 | 806 aa |

| \*Escherichia coli\*            | QGJ10764.1  | 804 aa |

| \*Salmonella\* Typhimurium LT2  | NP\_462735.1 | 804 aa |

| \*Klebsiella pneumoniae\*       | CDO11772.1  | 805 aa |

| \*Vibrio cholerae\*             | BBE11218.1  | 805 aa |

| \*Haemophilus influenzae\*      | XYW55554.1  | 806 aa |



\## Key results



\- \*\*471 of 810\*\* alignment positions (58.1%) were completely conserved across all six organisms.

\- \*\*32 conserved regions\*\* (≥80% identity, ≥5 residues) were identified, the longest spanning 46 and 42 residues — candidate functionally important regions.

\- Pairwise sequence distances and the resulting phylogenetic tree \*\*independently recovered known bacterial taxonomy\*\*, clustering the three Enterobacteriaceae species (\*E. coli\*, \*Salmonella\*, \*Klebsiella\*) tightly together, with \*P. aeruginosa\* as the most divergent outgroup.



Full discussion in \[`RESULTS.md`](./RESULTS.md).



\## Repository structure



scripts/ Analysis scripts, in pipeline order

data/ Input sequences and alignment

results/ Output files (conservation scores, distance matrix, trees, figure)





\## Methods summary



| Step | Tool/Method |

|------|-------------|

| Sequence retrieval | NCBI Entrez (Biopython) |

| Multiple sequence alignment | CLUSTAL Omega (EMBL-EBI web service) |

| Conservation analysis | Custom Python (per-position identity scoring) |

| Distance calculation | p-distance (proportion of differing residues) |

| Tree construction | Neighbor-Joining and UPGMA (Biopython `Phylo`) |



\## Requirements



\- Python 3.x

\- Biopython

\- matplotlib



\## Author



Ali Moghnieh — Biochemistry student, independent bioinformatics project.

