from Functions import InputFile
inputtext = InputFile().GetFileCustomSplit("rosalind_ini22.txt", ">")


def EditDistanceAlignment(inputtext):
    result1 = []
    result2 = []
    string1 = list(str(" " + inputtext[1]))
    string2 = list(str(" " + inputtext[0]))
    matrix = [[0 for x in range(len(string2))] for y in range(len(string1))]
    # value, upCell, leftCell, insertion = 0

    # first row and column
    # for row, element in enumerate(matrix):
    for element in range(0, len(string1)):
        matrix[element][0] = element
        element += 1

    for element in range(0, len(string2)):
        matrix[0][element] = element
        element += 1

    for row in range(1, len(string1)):
        for element in range(1, len(string2)):
            leftCell = matrix[row][element - 1]
            upCell = matrix[row - 1][element]
            replacement = matrix[row - 1][element - 1]
            if string1[row] != string2[element]:
                min_number = min(upCell, leftCell, replacement)
            else:
                min_number = min(upCell, leftCell, replacement - 1)
            matrix[row][element] = min_number + 1
    # finding min path
    currentRowAndElement = (len(string1) - 1, len(string2) - 1)
    while currentRowAndElement != (0, 0):
        leftCell = matrix[currentRowAndElement[0]
                          ][currentRowAndElement[1] - 1] + 1
        replacement = matrix[currentRowAndElement[0] -
                             1][currentRowAndElement[1] - 1]
        if string2[currentRowAndElement[1]] != string1[currentRowAndElement[0]]:
            replacement += 1
        upCell = matrix[currentRowAndElement[0] -
                        1][currentRowAndElement[1]] + 1

        dict1 = {
            leftCell: "leftCell", replacement: "replacement", upCell: "upCell"}
        dict2 = {"replacement": (currentRowAndElement[0] -
                                 1, currentRowAndElement[1] - 1),
                 "leftCell": (currentRowAndElement[0], currentRowAndElement[1] - 1), "upCell": (currentRowAndElement[0] -
                                                                                                1, currentRowAndElement[1])}
        min_val = dict1.get(min(dict1))
        currentRowAndElement = dict2.get(min_val)

        if(min_val == "leftCell"):
            result1.append("-")
            result2.append(string2[currentRowAndElement[1]+1])
        if(min_val == "upCell"):
            result2.append("-")
            result1.append(string1[currentRowAndElement[0]+1])
        if(min_val == "replacement"):
            result2.append(string2[currentRowAndElement[1]+1])
            result1.append(string1[currentRowAndElement[0]+1])
        # matrix
    # for i in matrix:
        # print(i)
    # min_distance
    print(matrix[-1][-1])
    print("".join(reversed(result2)))
    print("".join(reversed(result1)))
    editDistance = matrix[-1][-1]

    with open("C:\\Users\\timpo\\OneDrive\\Namizje\\Bioinformatika\\rezultat22.txt", 'w') as f:
        f.write('{}'.format(editDistance) + '\n')
        f.write("".join(reversed(result2)) + '\n')
        f.write("".join(reversed(result1)) + '\n')


EditDistanceAlignment(inputtext)
