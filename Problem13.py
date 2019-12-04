from Functions import InputFile


inputtext = InputFile().GetInputTextWithNoFirstLine("rosalind_ini13.txt")


def KmerComposition(inputtext):
    kmers = InputFile().fourMerComposition()
    for i in range(0, len(kmers)):
        kmer = kmers[i]
        result = 0
        for j in range(0, len(inputtext)):
            if kmer == inputtext[j:4 + j]:
                result += 1
        print(result, sep=" ", end=" ", flush=True)


KmerComposition(inputtext)
