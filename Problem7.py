from Functions import InputFile

inputtext = InputFile().GetFileNoSplit("rosalind_ini7.txt")


def CountingDNANucleotides(inputtext):
    nucleoNumber = {}
    inputtext = list(inputtext)
    for nucleotide in inputtext:
        if nucleotide in nucleoNumber:
            nucleoNumber[nucleotide] += 1
        else:
            nucleoNumber[nucleotide] = 1

    # sorting keys in dictionary alphabetically
    sortednames = sorted(nucleoNumber.keys(), key=lambda x: x.lower())

    for i in sortednames:
        print(str(nucleoNumber[i]) + " ", end="")


CountingDNANucleotides(inputtext)
