from Functions import InputFile

inputtext = InputFile().GetFile("rosalind_ini20.txt")


def CountingPointMutations(inputtext):
    length = len(inputtext[0])
    notEquals = 0
    data1 = inputtext[0]
    data2 = inputtext[1]
    for char in range(0, length):
        if data1[char] != data2[char]:
            notEquals += 1
    print(notEquals)


CountingPointMutations(inputtext)
