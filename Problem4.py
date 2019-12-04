from Functions import InputFile


inputtext = InputFile()
inputtext = inputtext.GetFile("rosalind_ini4.txt")


def ConditionsAndLoops(inputtext):
    a = inputtext[0]
    b = inputtext[1]
    suma = 0
    for x in range(int(a), int(b) + 1):
        if x % 2 == 1:
            suma += x

    return suma


result = ConditionsAndLoops(inputtext)
print(result)
