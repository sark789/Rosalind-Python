from Functions import InputFile
import re


inputtext = InputFile().GetFileCustomSplit("rosalind_ini10.txt", "\n>")


def ComputingGCContent(inputtext):
    newList = []
    b = 0
    n = 13  # >Rosalind_0808
    for i in inputtext:
        result = 0
        CGcounter = 0
        ATcounter = 0

        print(i[0:n])
        for eachChar in i[n:len(i)]:
            if eachChar == "C" or eachChar == "G":
                CGcounter += 1
            else:
                ATcounter += 1
            result = CGcounter / (CGcounter + ATcounter) * 100
        print(result)


ComputingGCContent(inputtext)
