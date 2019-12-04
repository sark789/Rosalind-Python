from Functions import InputFile
inputtext = InputFile().GetFileCustomSplit("rosalind_ini21.txt", ">")


def EditDistance(inputtext):

    string1 = list(str(" " + inputtext[0]))
    string2 = list(str(" " + inputtext[1]))
    matrix = [[0 for x in range(len(string2))] for y in range(len(string1))]
    #value, upCell, leftCell, insertion = 0

    # first row and column
    # for row, element in enumerate(matrix):
    for element in range(0, len(string1)):
        if element < len(string2):
            matrix[0][element] = element
        matrix[element][0] = element
        element += 1

    for row in range(1, len(string1)):
        for element in range(1, len(string2)):
            upCell = matrix[row][element - 1]
            leftCell = matrix[row - 1][element]
            replacement = matrix[row - 1][element - 1]
            if string1[row] != string2[element]:
                min_number = min(upCell, leftCell, replacement)
            else:
                min_number = min(upCell, leftCell, replacement - 1)
            matrix[row][element] = min_number + 1
    # matrix
    for i in matrix:
        print(i)
    # min_distance
    print(matrix[-1][-1])


EditDistance(inputtext)
