from Functions import InputFile


# inputtext = InputFile().GetFileNoSplit("rosalind_ini9.txt") #comment for prob17


def ComplementingAStrandOfDNA(inputtext):
    firstStrand = list(inputtext)
    reverseStrand = []
    for i in range(0, len(firstStrand) + 1):
        # reversing: ACT = TCA
        reverseStrand.append(firstStrand[len(firstStrand)-1 - i])
        # complementing A and T, and C and G
        if reverseStrand[i] == "A":
            reverseStrand[i] = "U"
        elif reverseStrand[i] == "U":
            reverseStrand[i] = "A"
        elif reverseStrand[i] == "C":
            reverseStrand[i] = "G"
        elif reverseStrand[i] == "G":
            reverseStrand[i] = "C"

        #print(str(reverseStrand[i - 1]), end="")
    return reverseStrand


# ComplementingAStrandOfDNA(inputtext)
