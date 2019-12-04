from Functions import InputFile

inputtext = InputFile().GetFileCustomSplit("rosalind_ini19.txt", ">")


def CreatingADistanceMatrix(inputtext):
    length = len(inputtext[0])
    result = []
    for j in inputtext:
        for k in inputtext:
            notEquals = 0
            for char in range(0, length):
                if j[char] != k[char]:
                    notEquals += 1 / length
            result.append(notEquals)
        print(*result, sep=" ", end="\n")
        result = []


CreatingADistanceMatrix(inputtext)
