import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index,row) in data.iterrows()}

name = input("what's your name? ").upper()
phonetic_name = [alphabet[letter] for letter in name]
print(phonetic_name)