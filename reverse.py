# This is a python code for reversing a strand of DNA

# Prompt the user to enter a nucleotide sequence
dna_strand = input("Enter your nucleotide sequence: ")

# Function to reverse DNA sequence
def reverse_dna(dna_strand):
    return dna_strand[::-1]

# Print the reversed DNA sequence
print("The reverse of the DNA strand is: " + reverse_dna(dna_strand))
