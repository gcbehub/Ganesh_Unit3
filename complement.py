# This is a python code for complementing a strand of DNA

# Prompt the user to enter a nucleotide sequence
dna_strand = input("Enter your nucleotide sequence: ")


# Function to complement the DNA sequence
def complement_dna(dna_strand):
    # Define the complement for each nucleotide
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    # Create the complementary strand by mapping each nucleotide
    return ''.join(complement[nucleotide] for nucleotide in dna_strand.upper())


# Print the complementary DNA sequence
print("The complementary DNA strand is: " + complement_dna(dna_strand))
