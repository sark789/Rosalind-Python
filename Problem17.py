from Functions import InputFile
from Problem8 import TransribingDNAtoRNA
from Problem9 import ComplementingAStrandOfDNA
inputtext = InputFile().GetFileNoSplit("rosalind_ini17.txt")


def FindingGenesWithORFs(inputtext):
    # convert T to U since it is RNA (problem 8 code)
    convert = (TransribingDNAtoRNA(inputtext))
    # reverse and complement
    reverse = ComplementingAStrandOfDNA(convert)
    data = "".join(reverse)
    codons = []
    genes = []
    codon_table = InputFile().GetRNACodonTable()
    start_codon = "AUG"
    stop_codon = "STOP"
    for i in range(0, len(inputtext)):
        if start_codon == data[i:len(start_codon) + i]:
            for j in range(i, len(inputtext), 3):
                current_data = data[j:len(start_codon) + j]
                current_data = codon_table.get(current_data)
                if current_data == stop_codon:
                    genes.append("".join(codons))
                    codons = []
                    break
                if j + 3 >= len(inputtext):
                    if current_data != None:
                        codons.append(current_data)
                    genes.append("".join(codons))
                    codons = []
                    break
                codons.append(current_data)

    print(max(genes, key=len))  # prints the longest element in list


FindingGenesWithORFs(inputtext)
