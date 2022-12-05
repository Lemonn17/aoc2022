file_path = 'day_05\day5_data.txt'



def processing_input(file_path):
    data = open(file_path, "r")
    is_crate = True
    starting_crate = []
    operators = []
    for line in data.readlines():
        if is_crate and line.strip() != '':
            starting_crate += [line.replace('\n','')]
        elif line.strip() == '':
            is_crate = False
        else:
            temp_op = list(filter(lambda x: x not in ['move','from','to'],tuple(e for e in line.strip().split(' '))))
            operators += [temp_op]
    return (stack_crate(starting_crate),operators)

# LIFO order
def stack_crate(starting_crate):
    stack_crate = {}
    temp_crate = []
    number_of_stacks = starting_crate[-1].strip().split('  ')
    crate_input = starting_crate[:-1]

    for i in crate_input:
        temp_crate += [list(filter(lambda x: x != '',i.replace('    ',' [#] ').replace('[','').replace(']','').split(' ')))]

    ## process bottom of the stack first
    temp_crate.reverse()

    for i in range(len(number_of_stacks)):
        stack_crate[str(i+1)] = []
    for list_of_crate in temp_crate:
        for index,crate in enumerate(list_of_crate):
            if crate != '#':
                stack_crate[str(index+1)].append(list_of_crate[index])
    return stack_crate

# part 1
def move_crate(stack_crate, operators):
    for operator in operators:
        number_of_crate_move = int(operator[0])
        move_from = operator[1]
        move_to = operator[2]
        for i in range(number_of_crate_move):
            # print("move from :", stack_crate[move_from]) 
            moving_crate = stack_crate[move_from].pop()
            stack_crate[move_to] += moving_crate
            # print("pop :", moving_crate) 
            # print("after pop :", stack_crate[move_from]) 
            # print("move to :", stack_crate[move_to]) 

        # print(stack_crate)
    return

# part 2
def move_crate_v2(stack_crate, operators):
    for operator in operators:
        number_of_crate_move = int(operator[0])
        move_from = operator[1]
        move_to = operator[2]
        # print("move from :", stack_crate[move_from]) 
        # print("move to :", stack_crate[move_to]) 
        moving_crate = stack_crate[move_from][-number_of_crate_move:]
        stack_crate[move_from] = stack_crate[move_from][:-number_of_crate_move]
        stack_crate[move_to] += moving_crate
        # print("after pop :", stack_crate[move_from]) 
        # print(stack_crate)

    return

def get_message(stack_crate):
    msg = ''
    for i in stack_crate.values():
        msg += i[-1]
    return msg

def main():
    stack_crate,operators = processing_input(file_path)
    # print(stack_crate,operators)
    # move_crate(stack_crate, operators)
    move_crate_v2(stack_crate, operators)
    print(get_message(stack_crate))
    return

if __name__ == "__main__":
    main()