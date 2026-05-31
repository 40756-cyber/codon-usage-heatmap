import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

def read_fasta(filename):
    with open(filename) as f:
        lines = f.readlines()
    sequence = "".join(line.strip() for line in lines[1:]).upper()
    return sequence

def get_codon_counts(sequence):
    codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)]
    return Counter(codons)

bases = ['A', 'T', 'G', 'C']
all_codons = [a+b+c for a in bases for b in bases for c in bases]

human = read_fasta("sequence.fasta")
ecoli = read_fasta("ecoli.fasta")

human_counts = get_codon_counts(human)
ecoli_counts = get_codon_counts(ecoli)

human_data = [[human_counts.get(all_codons[i*4+j], 0) for j in range(4)] for i in range(16)]
ecoli_data  = [[ecoli_counts.get(all_codons[i*4+j],  0) for j in range(4)] for i in range(16)]

fig, axes = plt.subplots(1, 2, figsize=(12, 12))

sns.heatmap(human_data, annot=True, fmt='d', cmap='YlGnBu', ax=axes[0],
            xticklabels=['A','T','G','C'],
            yticklabels=[all_codons[i*4] for i in range(16)])
axes[0].set_title("Human Insulin Gene")

sns.heatmap(ecoli_data, annot=True, fmt='d', cmap='OrRd', ax=axes[1],
            xticklabels=['A','T','G','C'],
            yticklabels=[all_codons[i*4] for i in range(16)])
axes[1].set_title("E. coli Lac Operon")

plt.tight_layout()
plt.savefig("comparison_heatmap.png")
print("Saved as comparison_heatmap.png!")

# Top 10 codons for each
human_top = sorted(human_counts.items(), key=lambda x: x[1], reverse=True)[:10]
ecoli_top  = sorted(ecoli_counts.items(),  key=lambda x: x[1], reverse=True)[:10]

human_labels, human_vals = zip(*human_top)
ecoli_labels, ecoli_vals = zip(*ecoli_top)

fig2, axes2 = plt.subplots(1, 2, figsize=(14, 5))

axes2[0].bar(human_labels, human_vals, color='steelblue')
axes2[0].set_title("Human Insulin — top 10 codons")
axes2[0].set_ylabel("Count")

axes2[1].bar(ecoli_labels, ecoli_vals, color='tomato')
axes2[1].set_title("E. coli Lac Operon — top 10 codons")
axes2[1].set_ylabel("Count")

plt.tight_layout()
plt.savefig("top10_codons.png")
print("Saved as top10_codons.png!")