from Functions import InputFile


inputtext = InputFile().GetFileNoSplit("rosalind_ini11.txt")


def TranslatingRNAintoProtein(inputtext):
    startCodons = []
    result = []

    for i in range(0, len(inputtext), 3):
        startCodons.append(inputtext[i:i+3])

    codonTable = InputFile().GetRNACodonTable()

    for codon in startCodons:
        if codon in codonTable.keys():
            result = str(codonTable[codon]).replace(
                "STOP", "").rstrip()
            print(result, sep=' ', end='', flush=True)


TranslatingRNAintoProtein(inputtext)
