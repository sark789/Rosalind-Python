from Functions import InputFile


inputtext = InputFile().GetInputTextWithNoFirstLine("rosalind_ini15.txt")


def SpeedingUpMotifFinding(inputtext):
    value = 0
    second_pointer_value = 0
    list_of_all = []
    list_of_tuples = []
    list_of_tuples.append((0, 'C'))
    list_of_all.append(0)
    second_pointer_location = 0
    prev_location = 0

    for i in range(0, len(inputtext) - 1):
        # mainpointer
        main_value = inputtext[i+1]
        list_of_tuples.append((i+1, main_value))
        # secondpointer
        second_pointer_value = inputtext[second_pointer_location]

        if main_value == second_pointer_value:
            value = value + 1
            second_pointer_location += 1

        else:
            while second_pointer_value != main_value:
                prev_location = list_of_all[second_pointer_location - 1]
                second_pointer_location = prev_location
                k = i + 1
                second_pointer_value = ([k[1] for k in list_of_tuples])
                second_pointer_value = second_pointer_value[second_pointer_location]
                value = second_pointer_location
                if second_pointer_value == main_value:
                    value += 1
                    second_pointer_location += 1
                if second_pointer_location == 0:
                    break

       #print(" ".join(str(value)))
        list_of_all.append(value)

    print(" ".join(map(str, list_of_all)))


SpeedingUpMotifFinding(inputtext)
