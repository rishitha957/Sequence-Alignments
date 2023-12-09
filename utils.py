from Bio import SeqIO

def find_closely_related_genomes(fasta_file, max_size_diff):
    records = list(SeqIO.parse(fasta_file, "fasta"))
    print(len(records))

    for i in range(len(records) - 1):
        print(len(records[i]))
        for j in range(i + 1, len(records)):
            seq1 = str(records[i].seq)
            seq2 = str(records[j].seq)

            size_diff = abs(len(seq1) - len(seq2))

            if size_diff <= max_size_diff:
                return seq1, seq2

    return None, None

# Example usage
fasta_file_path = "hg38Patch2.fa"  # Replace with your actual FASTA file path
max_size_difference = 100  # Adjust as needed

genome1, genome2 = find_closely_related_genomes(fasta_file_path, max_size_difference)

if genome1 is not None and genome2 is not None:
    print("Closely related genomes found:")
    print("Genome 1:", genome1)
    print("Genome 2:", genome2)
else:
    print("No closely related genomes found.")
