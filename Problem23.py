from Functions import InputFile
inputtext = InputFile().GetFileCustomSplit("rosalind_ini23.txt", ">")


def GlobalAlignmentWithScoringMatrix(inputtext):
    value = 0
    result1 = []
    result2 = []
    string1 = list(str(" " + inputtext[1]))
    string2 = list(str(" " + inputtext[0]))
    matrix = [[0 for x in range(len(string2))] for y in range(len(string1))]
    # value, upCell, leftCell, insertion = 0

    # first row and column
    # for row, element in enumerate(matrix):
    for element in range(0, len(string1)):
        matrix[element][0] = value
        value -= 5
        element += 1
    value = 0
    for element in range(0, len(string2)):
        matrix[0][element] = value
        value -= 5
        element += 1

    for row in range(1, len(string1)):
        for element in range(1, len(string2)):
            leftCell = matrix[row][element - 1]
            upCell = matrix[row - 1][element]
            replacement = matrix[row - 1][element - 1]
            if string1[row] != string2[element]:
                max_number = max(upCell - 5, leftCell - 5, replacement +
                                 InputFile().Blosum62((string2[element], string1[row])))
            else:
                penalty = InputFile().Blosum62(
                    ((string2[element], string1[row])))
                max_number = replacement + penalty
            matrix[row][element] = max_number

        # matrix
    # for i in matrix:
        # print(i)
    print(matrix[-1][-1])


GlobalAlignmentWithScoringMatrix(inputtext)
