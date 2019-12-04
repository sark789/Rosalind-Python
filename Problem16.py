from Functions import InputFile
import math

inputtext = InputFile().GetFileByLines("rosalind_ini16.txt", 2)


def IntroductionToRandomStrings(inputtext):
    DNA_string = str(inputtext[0])
    new_DNA = []
    result = []

    for i in DNA_string:
        new_DNA.append(i)
    numbers = inputtext[1].split()

    CGcounter = 0
    ATcounter = 0
    for i in new_DNA:
        if i == "C" or i == "G":
            CGcounter += 1
        else:
            ATcounter += 1
        # GCcontent = CGcounter / (CGcounter + ATcounter)

    numbers = list(map(float, numbers))
    # ENACBA : PROBABILITY = math.log10(((1 - podan GCcontent) / 2) ^ št.AinTnukleotidov) * (podanGCcontent / 2) ^ št.GinCnukleotidov
    for i in numbers:
        PROBABILITY = math.log10((((1-i) / 2)**ATcounter)
                                 * (i / 2) ** CGcounter)

        result.append("%0.3f" % PROBABILITY)  # izpiše do 3. float point
    print(*result)


IntroductionToRandomStrings(inputtext)
