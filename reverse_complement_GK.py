# This dictionary defines the pairs for the nucleotide complement
# A pairs with T, C pairs with G, and vice versa.
pairs = {
    "A": "T",  # Adenine (A) pairs with Thymine (T)
    "C": "G",  # Cytosine (C) pairs with Guanine (G)
    "G": "C",  # Guanine (G) pairs with Cytosine (C)
    "T": "A",  # Thymine (T) pairs with Adenine (A)
}

# Prompt the user to input a nucleotide sequence (DNA sequence)
input_sequence = input("Enter your nucleotide sequence: ")

# Initialize an empty string to store the reverse complement
reverse_complement = ""

# Loop through the input sequence in reverse order (from last base to first base)
# We start from len(input_sequence) - 1 (the last base) down to 0 (inclusive), stepping backwards.
for index in range(len(input_sequence) - 1, 0, -1):  # Starting from the last character

    # Get the base at the current index of the sequence
    base = input_sequence[index]

    # Find the complement of the base from the 'pairs' dictionary
    complement = pairs[base]

    # Append the complement base to the reverse_complement string
    reverse_complement += complement

# Print out the reverse complement sequence
print("The reverse complement of the input DNA sequence is: " + reverse_complement)
