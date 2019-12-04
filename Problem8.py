from Functions import InputFile


# inputtext = InputFile().GetFileNoSplit("rosalind_ini8.txt") #comment if u use it in another Problem


def TransribingDNAtoRNA(inputtext):
    inputtext = inputtext.replace("T", "U")
    # print(inputtext)

    return inputtext


# TransribingDNAtoRNA(inputtext)
