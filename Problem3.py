
def StringsAndLists(file_name: str):
    path = f'C:\\Users\\timpo\\OneDrive\\Namizje\\Bioinformatika\\{file_name}'

    # saves the file in inputFile, with - makes sure the file is closed and cleaned
    with open(path, 'r') as inputFile:
        text = inputFile.read().split()

    inputText = text[0]
    part1 = str(inputText[int(text[1]):int(text[2])+1])
    part2 = str(inputText[int(text[3]):int(text[4])+1])
    result = part1 + " " + part2
    print(result)


StringsAndLists("rosalind_ini3.txt")
