# Codon Usage Heatmap

A beginner bioinformatics project 

## What it does
- Reads a DNA sequence from a FASTA file
- Counts how often each of the 64 possible codons appears
- Generates a heatmap of codon usage
- Compares codon bias between human and bacterial genes

## Organisms compared
- **Human insulin gene** (NM_000207) — short, highly biased
- **E. coli lac operon** (J01636) — longer, different preferences

## Key finding
Human and E. coli genes show dramatically different codon preferences.
This is why drug manufacturers must rewrite human genes using 
bacteria-friendly codons — a process called codon optimization.

## Tools used
- Python 3
- matplotlib
- seaborn
- pandas

## How to run
1. Download a gene sequence as a FASTA file from NCBI
2. Save it as `sequence.fasta`
3. Run `python codon_heatmap.py`
