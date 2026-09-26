Results and Discussion

Sequence Conservation



Multiple sequence alignment of the six bacterial GyrB proteins produced an alignment of 810 positions (reflecting small insertions/deletions relative to the 804–806 amino acid native protein lengths). Of these, 471 positions (58.1%) were completely conserved across all six organisms — identical amino acids at every position, in every species.



Because conservation percentage is bounded by the number of sequences compared (with six sequences, only 100%, 83.3%, 66.7%, 50%, 33.3%, and 16.7% are mathematically possible), positions were grouped into these discrete tiers rather than arbitrary round-number thresholds. This showed 121 additional positions at ≥80% identity (i.e., conserved in 5 of 6 organisms), for a combined 592 positions (73.1%) at high conservation.



Conserved positions were not randomly distributed — they clustered into 32 distinct regions of ≥80% identity spanning 5 or more consecutive positions. The two longest such regions were positions 9–50 (42 residues) and 86–131 (46 residues), both entirely conserved at 100% identity. Long, unbroken conserved stretches like these are a strong indicator of structurally or catalytically essential regions, since random mutation would be expected to erode conservation at sites under no functional constraint. Given that GyrB's N-terminal region contains the ATP-binding (GHKL) domain essential to the gyrase mechanism, these early conserved blocks are plausible candidates for that domain, though this would need confirming against annotated domain boundaries (e.g., via UniProt or Pfam) before being stated definitively.



Evolutionary Relationships



Pairwise p-distances (proportion of differing residues, gapped columns excluded) between the six GyrB sequences ranged from 0.0336 to 0.3238. The three Enterobacteriaceae species — Salmonella Typhimurium, Escherichia coli, and Klebsiella pneumoniae — showed the smallest pairwise distances (0.0336–0.0510), consistent with their shared taxonomic family. Pseudomonas aeruginosa was the most divergent from every other sequence (0.3134–0.3238), consistent with its placement in a distinct bacterial order (Pseudomonadales) from the other five organisms, all of which belong to Gammaproteobacteria more broadly but different families.



A Neighbor-Joining tree constructed from this distance matrix (cross-validated against a UPGMA tree, which produced the same topology) placed Salmonella and E. coli as the closest pair (branch length 0.0168 each), joined next by K. pneumoniae to form the Enterobacteriaceae clade. Vibrio cholerae and Haemophilus influenzae branched off at intermediate distances, and P. aeruginosa formed the outermost branch with the longest branch length (0.159), consistent with it being the most evolutionarily distant organism in the dataset.



Notably, these relationships were recovered directly from GyrB protein sequence data alone, without any taxonomic labels provided to the analysis — the tree independently reproduced known bacterial classification, supporting GyrB's utility as a phylogenetic marker in addition to its role as a conserved, essential gene.



Limitations



This analysis has several limitations worth noting. The p-distance metric used for the distance matrix does not correct for multiple substitutions occurring at the same site (unlike models such as Jukes-Cantor or Kimura 2-parameter), which can lead to underestimated distances for more diverged sequence pairs — though given the relatively close relationship of the organisms studied here, this effect is likely modest. The dataset is also limited to six organisms and a single protein; broader taxon sampling and comparison against additional core genes would strengthen confidence in the phylogenetic signal observed.

