import math


file_path = 'day_09\day9_data.txt'

def processing_input(file_path):
    data = open(file_path, "r")
    data_list = []
    for line in data.readlines():
        direction, length = line.strip().split(' ')
        data_list += [[direction, int(length)]]
    return data_list

def move_knot(is_head,head_position, tail_position):
    if not is_adjacent(head_position, tail_position):
        tail_position = new_knot_position(head_position,tail_position)
    return tail_position


# this is hard to follows :(
def new_knot_position(head_position,tail_position):

    head_x = head_position[0]
    head_y = head_position[1]
    tail_x = tail_position[0]
    tail_y = tail_position[1]

    dx = head_x - tail_x
    dy = head_y - tail_y
    adx, ady = abs(dx), abs(dy)


    # head [2,2] tail [0,0] -> [1,1] case 1
    # head [-2,-2] tail [0,0] -> [-1,-1] case 1
    # head [2,-2] tail [0,0] -> [1,-1] case 1
    # head [-2,2] tail [0,0] -> [-1,1] case 1
    # case 1
    if adx == 2 and ady == 2:
        if dx > 0:
            tail_x += 1 
        else:
            tail_x += -1

        if dy > 0:
            tail_y += 1
        else:
            tail_y += -1
            
    
    # head [4,2] tail [3,0] -> [4,1] case 2-1
    # case 2
    else:
        # directly move up/down/left/right
        if ady == 0:
            if dx > 0:
                tail_x += 1
            else:
                tail_x += -1
        elif adx == 0:
            if dy > 0:
                tail_y += 1
            else:
                tail_y += -1
        # case 2-1
        elif ady == 2 and adx == 1:
            if dy > 0:
                tail_y += 1
            else:
                tail_y += -1
            tail_x = head_x

        elif adx == 2 and ady == 1:
            if dx > 0:
                tail_x += 1
            else:
                tail_x += -1
            tail_y = head_y

    new_position = [tail_x,tail_y]

    return new_position

def is_adjacent(head_position, tail_position):
    head_x = head_position[0]
    head_y = head_position[1]
    tail_x = tail_position[0]
    tail_y = tail_position[1]
    distance = math.sqrt(((head_x-tail_x)**2) + ((head_y-tail_y)**2))
    # print(distance)
    if (distance >= 2):
        return False
    else:
        return True

def cal_knots(data_list,starting_position,knots):
    knots_position = []
    tail_knot_positions = []
    for _ in range(knots):
        knots_position += [starting_position]

    knot_position_list = []
    for each_move in data_list:
        direction = each_move[0]
        distance = each_move[1]
        for _ in range(distance):

            knot_position_list += knots_position[1:]
            head_x = knots_position[0][0]
            head_y = knots_position[0][1]

            if direction == 'U':
                knots_position[0] = [head_x,head_y + 1]
            elif direction == 'D':
                knots_position[0] = [head_x,head_y - 1]
            elif direction == 'L':
                knots_position[0] = [head_x - 1 ,head_y]
            elif direction == 'R':
                knots_position[0] = [head_x + 1,head_y]

            for i in range(knots -1):
                head_position = knots_position[i]
                tail_position = knots_position[i + 1]
                tail_position = move_knot(direction,head_position, tail_position)
                knots_position[i + 1] = tail_position
            # print(f'rope : {knots_position}  \n ###################')
            tail = knots_position[-1]
            tail_knot_positions += [(tail[0],tail[1])]
        # print(counter, knots_position)
    temp = set(tail_knot_positions)
    print(len(temp))
    return 

def main():
    data_list = processing_input(file_path)
    starting_position = [0,0]
    # part 1
    cal_knots(data_list,starting_position,2)

    # part 2
    cal_knots(data_list,starting_position,10)
    return

if __name__ == "__main__":
    main()

