"""
Objectives:
- Review Python lists (arrays).
- Implement basic array operations (adding, removing, searching, sorting, 
reversing).
- Understand time complexity (Big O notation) for these operations.

"""

# Appending an element
# Different ways of initialising lists:
practice_list = ["Orange", "Banana", "Mango", "Orange", "Kiwi", "Melon"]
practice_list_2 = list()
practice_list_2 = [2, 56, 85, 33, 21, 45, 1, 74]
copy_list_1 = practice_list.copy()

element_to_append = "Apple"
element_to_append_2 = 42

practice_list.append(element_to_append)
practice_list_2.append(element_to_append_2)

print(practice_list)
print(practice_list_2)

# Inserting an element at a certain index
practice_list.insert(3, "Pineapple")
print(practice_list)

# Popping an element
practice_list.pop()
print(practice_list)
print(practice_list_2)
practice_list_2.pop(2)
print(practice_list_2)

# Removing an element
practice_list.remove("Orange")
print(practice_list)
del practice_list[0]

# Slicing a list
print(practice_list_2[:-1])
print(practice_list_2[::-1]) # prints a reversed list
# when indexing backwards, the first element of the slice is 
# not included (when indexing forwards, the last element is not included)
print(practice_list_2[-4:-1])

# Sorting using the Python in-built method
print(practice_list_2)
practice_list_2.sort() # sorting in place, returning None
print(practice_list_2)
print(practice_list)
practice_list.reverse() # reversing in place, returns None
print(practice_list)
print(copy_list_1) # still the unchanged version of the original list

def linear_search(arr: list, target):
    # Searches for target through a list, element by element, and returns
    # the index of the first occurence of target
    if target in arr:
        return arr.index(target)
    else:
        return -1
        
print(linear_search(practice_list, 'Melon'))
print(linear_search(practice_list, "Cat"))

# Practicing matrix transposition
# Complexity: O(i * j) where i=num_rows and j=num_columns
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

transposed_matrix = []

for row in matrix:
    print(row)
    for element in row:
        print(element)

num_columns = len(matrix[0])
print(num_columns)

for i in range(num_columns):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed_matrix.append(transposed_row)
print(transposed_matrix)

# This is the same as above but shorter
transposed_matrix = [[row[i] for row in matrix] for i in range(num_columns)]
print(transposed_matrix)

"""
Practicing simple functions for bioinformatics.
Example: Write a small function that takes a DNA sequence 
(represented as a string) and returns a list of the nucleotides 
(e.g., ['A', 'T', 'G', 'C']).
Example: Write a small function that, given the DNA sequence 
from the previous example, searches for a nucleotide in the array.
Example: Write a simple Python program that calculates the frequency 
of each nucleotide in a DNA sequence using an array.
"""

# Class nucleotide sequence.
# Reason for creating a class: to perform multiple functions on the sequence,
# all grouped together and to be performed only on nucleotide and not e.g.
# protein sequence

class NucleotideSequence():
    # At instance initiation, check if the letters are all nucleotides,
    # otherwise refuse to initialise the object and print an error message
    alphabet = ["A", "T", "G", "C", "U", "X"]
    def __init__(self, sequence: str):         
        # Complexity: O(n) where n is length of sequence
        for letter in sequence:
            if letter.upper() not in self.alphabet:
                raise TypeError("Unexpected letters in sequence. Possibly not a nucleic acid? \
                                Permitted letters: 'A', 'T', 'G', 'C', 'U', 'X'")
            else:
                self.sequence = sequence.upper()

    def __str__(self):
        return self.sequence

    """
    This was a supporting method, written as a draft for __init__ 
    def check_if_nucleic_acid(self):
        result = True
        for letter in self.sequence:
            print(letter)
            if letter.capitalize() not in self.alphabet:
                result = False
                break
        return result
    """

    def return_seq_as_list(self):
        # returns a list object containing individual nucleotides as strings
        # Complexity: O(n) where n is length of the sequence
        seq_as_list = []
        for letter in self.sequence:
            seq_as_list.append(letter)
        return seq_as_list
    
    def find_nucleotide(self, nucleotide: str) -> list:
        # checks for sensible input, then returns a sorted list of  
        # all positions at which nucleotide resides in sequence
        # Comlexity: O(n) where n is length of the sequence

        if len(nucleotide) > 1:
            print("Can only search for a single nucleotide, not sequence.")
            return None
        elif nucleotide not in self.alphabet:
            print("Not a nucleotide, cannot search. Permitted letters: 'A', 'T', 'G', 'C', 'U', 'X'")
        else:
            positions = []
            nuc_seq = self.return_seq_as_list()
            print(nuc_seq)
            for i in range(len(nuc_seq)):
                if nuc_seq[i] == nucleotide:
                    positions.append(i)
            return positions

    def calculate_nucleotide_frequencies(self):
        # Calculates frequency of each nucleotide in a sequence 
        # and returns a dictionary, where 
        # keys = nucleotides, values = frequencies
        # Complexity: O(n) where n is length of sequence

        frequencies = {'A': 0, 'T': 0, 'G': 0, 'C': 0, 'U': 0, 'X': 0}
        for letter in self.sequence:
            frequencies[letter] += 1
        return frequencies

class DNASequence(NucleotideSequence):
    alphabet = ["A", "T", "G", "C", "X"]
    def __init__(self, sequence: str):         
        # Complexity: O(n) where n is length of sequence
        for letter in sequence:
            if letter.upper() not in self.alphabet:
                raise TypeError("Unexpected letters in sequence. Possibly not a DNA? \
                                Permitted letters: 'A', 'T', 'G', 'C', 'X'")
            else:
                self.sequence = sequence.upper()

class RNASequence(NucleotideSequence):
    alphabet = ["A", "U", "G", "C", "X"]
    def __init__(self, sequence: str):         
        # Complexity: O(n) where n is length of sequence
        for letter in sequence:
            if letter.upper() not in self.alphabet:
                raise TypeError("Unexpected letters in sequence. Possibly not a RNA? \
                                Permitted letters: 'A', 'U', 'G', 'C', 'X'")
            else:
                self.sequence = sequence.upper()

sequence1 = NucleotideSequence("ATGCC")
print(sequence1.return_seq_as_list())

print(sequence1.find_nucleotide("C"))
print(sequence1.calculate_nucleotide_frequencies())

print(sequence1)
sequence3 = DNASequence("ATTTGCC")
sequence4 = RNASequence("AUUUGCC")
# sequence2 = NucleotideSequence("ATGCCBCU") # this would refuse to initialise

