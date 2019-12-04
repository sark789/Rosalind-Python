from Functions import InputFile


inputtext = InputFile().GetFileNoSplit("rosalind_ini12.txt")


def FindingAMotifInDNA(inputtext):
    motif = "CGGAACCCG"
    for i in range(0, len(inputtext)):
        if motif == inputtext[i:len(motif) + i]:
            print((i + 1), sep=" ", end=" ", flush=True)


FindingAMotifInDNA(inputtext)
