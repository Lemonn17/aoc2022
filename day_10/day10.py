file_path = 'day_10\day10_data.txt'
command_cycle = {'noop': 1, 'addx': 2}
pixel = ('.','#')


def processing_input(file_path):
    data = open(file_path, "r")
    data_list = []
    for line in data.readlines():
        data_list += [line.strip()]
    return data_list

def run_program(data_list,register_x):
    clock_cycle = 1
    interesting_signals = []
    ctr_rows = []
    ctr = ''
    sprite_position = '###.....................................'

    for input in data_list:
        input_split = input.split(' ')
        cycle_use = command_cycle[input_split[0]]


        for i in range(cycle_use):
            # if clock_cycle == 240:
            #     print(clock_cycle, register_x, sprite_position)
                
            # part 1
            if clock_cycle % 40 == 20 and clock_cycle < 225:
                signal_strength = register_x*clock_cycle
                interesting_signals  += [signal_strength] 

            # part 2
            if (clock_cycle-1) % 40 == 0:
                ctr_rows += [ctr]
                ctr = ''

            if is_draw_ctr(clock_cycle,sprite_position):
                ctr += '#'
            else:
                ctr += '.'
            if i == 1 and cycle_use == 2:
                register_x += int(input_split[1])
                if register_x == -1:
                    sprite_position = '#.......................................'
                # elif register_x == 0:
                #     sprite_position = '##......................................'
                # elif register_x == 1:
                #     sprite_position = '###.....................................'
                # elif register_x == 2:
                #     sprite_position = '.###....................................'
                # elif register_x == 37:
                #     sprite_position = '....................................###.'
                # elif register_x == 39:
                #     sprite_position = '......................................##'
                # elif register_x == 40:
                #     sprite_position = '.......................................#'
                # elif register_x == -2 or register_x == 41:
                #     sprite_position = '........................................'
                else:
                    sprite_position = sprite_position.replace('#','.')
                    sprite_position = sprite_position[:register_x-1] + pixel[1] + pixel[1] + pixel[1] + sprite_position[register_x+2:]
            # print(f'cycle : \t {clock_cycle} \t register : {register_x}')
            # print(f'ctr :\t\t {ctr}')
            # print(f'sprite :\t {sprite_position}')
            clock_cycle += 1
    ctr_rows += [ctr]

    # part 1
    print(sum(interesting_signals))

    # part 2
    for each_row in ctr_rows:
        print(each_row)

def is_draw_ctr(clock_cycle,sprite_position):
    ctr_position = (clock_cycle%40) -1
    if sprite_position[ctr_position] == pixel[1]:
        return True
    else:
        return False



def main():
    data_list = processing_input(file_path)
    register_x = 1
    # print(data_list)
    run_program(data_list,register_x)
    return

if __name__ == "__main__":
    main()

