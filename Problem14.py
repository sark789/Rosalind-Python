from Functions import InputFile
from itertools import product


inputtext = InputFile().GetFileByLines("rosalind_ini14.txt", 2)


def EnumeratingKMersLexicographically(inputtext):

    symbols = inputtext[0].split(sep=" ", )
    # string_symbols = "".join(symbols)
    string_len = int(inputtext[1])
    for roll in product(symbols, repeat=string_len):
        print("".join(roll))


EnumeratingKMersLexicographically(inputtext)
