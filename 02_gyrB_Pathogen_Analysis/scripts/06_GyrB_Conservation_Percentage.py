from Bio import AlignIO
from collections import Counter

alignment = AlignIO.read("gyrB_alignment.aln", "clustal")

total_positions = alignment.get_alignment_length()
num_sequences = len(alignment)

results = []  # (position, most_common_aa, count, percent, conservation_class)

for i in range(total_positions):
    column = alignment[:, i]
    counts = Counter(column)

    # Most common residue at this position (may be a gap "-")
    most_common_aa, count = counts.most_common(1)[0]
    percent = (count / num_sequences) * 100

    # Classify conservation level
    if percent == 100:
        conservation_class = "100%"
    elif percent >= 90:
        conservation_class = ">=90%"
    elif percent >= 80:
        conservation_class = ">=80%"
    elif percent >= 50:
        conservation_class = ">=50%"
    else:
        conservation_class = "<50%"

    results.append((i + 1, most_common_aa, count, percent, conservation_class))

# --- Summary counts ---
from collections import Counter as C
class_counts = C(r[4] for r in results)

print("Total alignment positions:", total_positions)
print("\nConservation breakdown:")
for label in ["100%", ">=90%", ">=80%", ">=50%", "<50%"]:
    print(f"  {label:>6}: {class_counts.get(label, 0)}")

# --- Save full per-position table to CSV ---
import csv
with open("gyrB_conservation_scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Position", "Most_Common_AA", "Count", "Percent_Conserved", "Class"])
    writer.writerows(results)

print("\nSaved full per-position table to gyrB_conservation_scores.csv")

# --- Highly conserved regions (stretches of >=80% conserved positions) ---
def find_conserved_regions(results, threshold=80, min_length=5):
    regions = []
    start = None
    for pos, aa, count, percent, cls in results:
        if percent >= threshold:
            if start is None:
                start = pos
        else:
            if start is not None and (pos - 1 - start + 1) >= min_length:
                regions.append((start, pos - 1))
            start = None
    if start is not None and (total_positions - start + 1) >= min_length:
        regions.append((start, total_positions))
    return regions

regions = find_conserved_regions(results, threshold=80, min_length=5)
print(f"\nConserved regions (>=80% identity, length >=5): {len(regions)}")
for r in regions[:20]:
    print(f"  positions {r[0]}-{r[1]} (length {r[1]-r[0]+1})")