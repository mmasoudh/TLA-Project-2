def main():
    input_file = input("Please Enter The File Dir \n")
    input_file = open(input_file, 'r')
    states = part_zero()(input_file)
    mainList = part_one(states)

    for i in range(4 * int(states[0])):
        print(mainList[0] + " -> " + mainList[1] + mainList[2] + " | " + mainList[1] + mainList[3])
        for j in range(2 * int(states[0])):
            del mainList[0]

    for i in range(len(mainList)):
        print(mainList[i])
if __name__ == "__main__":
    main()


def part_zero(File):
    inputed_items = []
    for line in File:
        line = line.split("\n")
        inputed_items.append(line)


    for i in range(len(inputed_items)):
        if inputed_items[i][-1] == '':
            del inputed_items[i][-1]

    inputList = []
    for i in range(len(inputed_items)):
        inputList.append(inputed_items[i][0])

    inputList = [char.replace('->', '') for char in inputList]
    inputList = [char.replace('*', '') for char in inputList]
    inputList = [char.replace('_', '') for char in inputList]

    return inputList

def part_one(List):
    stateNumber = int(List[0])
    stack_alphabet = List[1]
    stack_alphabet = stack_alphabet.split(",")
    transition = []
    non_transiton = []
    for i in range(4,len(List)):
        anything = List[i].split(",")
        if anything[3] != "" :
            transition.append(List[i])
        else:
            non_transiton.append(List[i])

    CFGList = []
    for l in range(stateNumber):
        if l == 0:
            for i in range(len(transition)):
                local_var = transition[i].split(",")
                local_str = ""
                local_str = local_str + str(anything[0])
                local_str = local_str + str(anything[2])
                local_str = local_str + str(anything[4])
                CFGList.append(local_str)
                for j in range(stateNumber-1):
                    local_str = ""
                    local_str = local_str.join(anything[1])
                    CFGList.append(local_str)
                    for m in range(0,stateNumber):

                        local_str = ""
                        if len(anything[3])>1:
                            local_str = local_str.join(str("("+anything[0]+str(anything[3][0])+"q"+str(m)+")"+"("+"q"+str(m)+str(anything[3][1])+anything[4]+")"))
                        else:
                            local_str = local_str.join(str("(" + anything[0] + str(anything[3][0]) + "q" + str(m) + ")"))
                        CFGList.append(local_str)
        else:
            for i in range(len(transition)):
                anything = transition[i].split(",")
                local_str = ""
                local_str = local_str + str(anything[0])
                local_str = local_str + str(anything[2])
                local_str = local_str + "qf"
                CFGList.append(local_str)
                for j in range(stateNumber - 1):
                    local_str = ""
                    local_str = local_str.join(anything[1])
                    CFGList.append(local_str)
                    for m in range(0, stateNumber):
                        local_str = ""
                        if (len(anything[3]) > 1):
                            local_str = local_str.join(str(
                                "(" + anything[0] + str(anything[3][0]) + "q" + str(m) + ")" + "(" + "q" + str(m) + str(
                                    anything[3][1]) + "qf" + ")"))
                        else:
                            local_str = local_str.join(str(
                                "(" + anything[0] + str(anything[3][0]) + "q" + str(m) + ")"))

                        CFGList.append(local_str)


    others = Other_transition(non_transiton)
    for i in range(len(others)):

        CFGList.append(others[i])
    return CFGList

def Other_transition(lst):
    CFG = []
    for i in range(len(lst)):
        string = ""
        Var = lst[i].split(",")
        string = string + str(Var[0])
        string = string + str(Var[2])
        string = string + str(Var[4])
        string = string + " -> "
        if Var[1] != "":
            string = string + str(Var[1])
        else:
            string = string + "_"

        CFG.append(string)
    return CFG





