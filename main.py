import pandas as pd

# Load the NATO phonetic alphabet CSV
data = pd.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary mapping letters to NATO codes
nato_dict = {row.letter: row.code for index, row in data.iterrows()}

# Get user input
word = input("Enter a word: ").upper()

# Convert letters to NATO phonetic codes
phonetic_list = [
    nato_dict[letter]
    for letter in word
    if letter in nato_dict
]

print(phonetic_list)