import string
from time import sleep
file_path = 'day_12\day12_data.txt'
letters = ['S'] + [ e for e in string.ascii_lowercase] + ['E']

letters_reverted = ['E'] + sorted([ e for e in string.ascii_lowercase],reverse=True) + ['S']
# print(letters_inverted)
position = {'start' : (-1,-1), 'end' : (-1,-1)}
step_grid = []

class GridWithSteps:
    def __init__(self,data_list,position,step_grid) -> None:
        self.grid = data_list
        self.step_grid = step_grid
        self.start_position = position['start']
        self.end_position = position['end']
        self.row = len(step_grid)
        self.column = len(step_grid[0])
        self.possible_position = []
        for row in range(self.row):
            for column in range(self.column):
                self.possible_position += [(row,column)]
        # part 1
        # self.step_grid[self.start_position[0]][self.start_position[1]][0] = 0
        # self.step_grid[self.start_position[0]][self.start_position[1]][1] = True
        # part 2
        self.step_grid[self.end_position[0]][self.end_position[1]][0] = 0
        self.step_grid[self.end_position[0]][self.end_position[1]][1] = True
        pass

    def get_shortest_end(self):
        print(self.step_grid[self.end_position[0]][self.end_position[1]][0])
    def get_shortest_start(self):
        position_list = []
        result_list = []
        for row_number,row in enumerate(self.grid):
            for column_number, column in enumerate(row):
                if self.grid[row_number][column_number] in ('a','S'):
                    position_list += [(row_number,column_number)]

        for position in position_list:
            if self.step_grid[position[0]][position[1]][1]:
                result_list += [self.step_grid[position[0]][position[1]][0]]

        print(min(result_list))


    def is_moveable_toward(self,from_position,to_position,letters_list):
        from_position_x, from_position_y = from_position[0],from_position[1]
        to_position_x, to_position_y = to_position[0],to_position[1]
        from_letter = self.grid[from_position_x][from_position_y]
        to_letter = self.grid[to_position_x][to_position_y]

        if from_letter == 'S':
            from_letter = 'a'
        if from_letter == 'E':
            from_letter = 'z'
        if to_letter == 'S':
            to_letter = 'a'
        if to_letter == 'E':
            to_letter = 'z'
            
        if (letters_list.index(from_letter) + 1) == letters_list.index(to_letter) or letters_list.index(from_letter) >= letters_list.index(to_letter) :
            # print(from_letter, letters.index(from_letter) ,to_letter, letters.index(to_letter))
            # print(from_letter,letters_list.index(from_letter),to_letter,letters_list.index(to_letter))
            return True
        else:
            return False 

    def shortest(self,current_position,letters):
        list_shortest =[]
        up_row, up_column  = current_position[0]-1,current_position[1]
        down_row, down_column  = current_position[0] + 1,current_position[1]
        left_row, left_column  = current_position[0],current_position[1] -1
        right_row, right_column  = current_position[0],current_position[1] + 1
        if (up_row, up_column) in self.possible_position and self.is_moveable_toward((up_row, up_column),current_position,letters):    
            is_up_visited = self.step_grid[up_row][up_column][1]
            if is_up_visited:
                list_shortest += [self.step_grid[up_row][up_column][0] + 1]
        if (down_row, down_column) in self.possible_position and self.is_moveable_toward((down_row, down_column),current_position,letters):    
            is_down_visited = self.step_grid[down_row][down_column][1]
            if is_down_visited:
                list_shortest += [self.step_grid[down_row][down_column][0] + 1]
        if (right_row, right_column) in self.possible_position and self.is_moveable_toward((right_row, right_column),current_position,letters):    
            is_right_visited = self.step_grid[right_row][right_column][1]
            if is_right_visited:
                list_shortest += [self.step_grid[right_row][right_column][0] + 1]

        if (left_row, left_column) in self.possible_position and self.is_moveable_toward((left_row, left_column),current_position,letters):    
            is_left_visited = self.step_grid[left_row][left_column][1]
            if is_left_visited:
                list_shortest += [self.step_grid[left_row][left_column][0] + 1]
        return list_shortest

    def process_new(self):
        is_loop = False
        while not is_loop:
            for row_number,row in enumerate(self.step_grid):
                for column_number,column in enumerate(row):
                    # part 1
                    # is_loop = self.step_grid[self.end_position[0]][self.end_position[1]][1] 
                    # self.process_helper(row_number,column_number,letters)

                    # print(f'running {row_number}, {column_number}')
                    # part 2
                    is_loop = self.step_grid[self.start_position[0]][self.start_position[1]][1] 
                    self.process_helper(row_number,column_number,letters_reverted)

    # part 1 brute forcing
    def process_helper(self,row_number,column_number,letters):
        current_position = (row_number,column_number)
        up_row, up_column  = current_position[0]-1,current_position[1]
        down_row, down_column  = current_position[0] + 1,current_position[1]
        left_row, left_column  = current_position[0],current_position[1] -1
        right_row, right_column  = current_position[0],current_position[1] + 1

        if self.step_grid[row_number][column_number][1]:
            
            # up
            if (up_row, up_column) in self.possible_position and self.is_moveable_toward(current_position,(up_row, up_column),letters):    
                is_up_visited = self.step_grid[up_row][up_column][1]
                next_step = [self.step_grid[row_number][column_number][0] + 1]
                if is_up_visited and self.step_grid[up_row][up_column][0] > min(next_step):
                    
                    next_step += self.shortest((up_row, up_column),letters)
                    self.step_grid[up_row][up_column][0] = min(next_step)
                elif not is_up_visited :
                    next_step = [self.step_grid[row_number][column_number][0] + 1]
                    self.step_grid[up_row][up_column][0] = min(next_step)
                    self.step_grid[up_row][up_column][1] = True

            # down
            if (down_row, down_column) in self.possible_position and self.is_moveable_toward(current_position,(down_row, down_column),letters):    
                is_down_visited = self.step_grid[down_row][down_column][1]
                next_step = [self.step_grid[row_number][column_number][0] + 1]
                if is_down_visited and self.step_grid[down_row][down_column][0] > min(next_step):
                    next_step += self.shortest((down_row, down_column),letters)
                    self.step_grid[down_row][down_column][0] = min(next_step)
                elif not is_down_visited :
                    next_step = [self.step_grid[row_number][column_number][0] + 1]
                    self.step_grid[down_row][down_column][0] = min(next_step)
                    self.step_grid[down_row][down_column][1] = True

            # left
            if (left_row, left_column) in self.possible_position and self.is_moveable_toward(current_position,(left_row, left_column),letters):    
                is_down_visited = self.step_grid[left_row][left_column][1]
                next_step = [self.step_grid[row_number][column_number][0] + 1]
                if is_down_visited and self.step_grid[left_row][left_column][0] > min(next_step):
                    next_step += self.shortest((left_row, left_column),letters)
                    self.step_grid[left_row][left_column][0] = min(next_step)
                elif not is_down_visited :
                    if (row_number,column_number) == (0,3):
                        print(f'next : {next_step}')
                    next_step = [self.step_grid[row_number][column_number][0] + 1]
                    self.step_grid[left_row][left_column][0] = min(next_step)
                    self.step_grid[left_row][left_column][1] = True

            # right
            if (right_row, right_column) in self.possible_position and self.is_moveable_toward(current_position,(right_row, right_column),letters):    
                is_right_visited = self.step_grid[right_row][right_column][1]
                next_step = [self.step_grid[row_number][column_number][0] + 1]
                if is_right_visited and self.step_grid[right_row][right_column][0] > min(next_step):
                    next_step += self.shortest((right_row, right_column),letters)
                    self.step_grid[right_row][right_column][0] = min(next_step)
                elif not is_right_visited :
                    next_step = [self.step_grid[row_number][column_number][0] + 1]
                    self.step_grid[right_row][right_column][0] = min(next_step)
                    self.step_grid[right_row][right_column][1] = True
        # print()
        # for i in self.step_grid:
        #     print(i)
        # print() 
        # sleep(0.25)

    # maximum recursion // not used 
    def process(self,current_position):
        start_x, start_y = current_position[0],current_position[1]
        self.step_grid[start_x][start_y][1] = True
        self.step_grid[self.start_position[0]][self.start_position[1]][0] = 0
        next_step = [self.step_grid[start_x][start_y][0] + 1]
        # TODO

        up_row, up_column  = current_position[0]-1,current_position[1]
        down_row, down_column  = current_position[0] + 1,current_position[1]
        left_row, left_column  = current_position[0],current_position[1] -1
        right_row, right_column  = current_position[0],current_position[1] + 1

        # go up
        if (up_row, up_column) in self.possible_position and self.is_moveable_toward(current_position,(up_row, up_column)):    
            is_up_visited = self.step_grid[up_row][up_column][1]
            if is_up_visited and self.step_grid[up_row][up_column][0] > min(next_step):
                next_step = [self.step_grid[start_x][start_y][0] + 1]
                next_step += self.shortest((up_row, up_column),letters)
                self.step_grid[up_row][up_column][0] = min(next_step)
                if (up_row, up_column) == self.end_position or (up_row, up_column) == self.start_position :
                    return
                else:
                    self.process((up_row,up_column))
                
            elif not is_up_visited :
                next_step = [self.step_grid[start_x][start_y][0] + 1]
                self.step_grid[up_row][up_column][0] = min(next_step)
                self.step_grid[up_row][up_column][1] = True
                if (up_row, up_column) == self.end_position:
                    return
                else:
                    self.process((up_row,up_column))
        
        # go donw
        if (down_row, down_column) in self.possible_position and self.is_moveable_toward(current_position,(down_row, down_column)):    
            is_down_visited = self.step_grid[down_row][down_column][1]
            if is_down_visited and self.step_grid[down_row][down_column][0] > min(next_step):
                next_step = [self.step_grid[start_x][start_y][0] + 1]
                next_step += self.shortest((down_row, down_column),letters)
                self.step_grid[down_row][down_column][0] = min(next_step)
                if (down_row, down_column) == self.end_position or (down_row, down_column) == self.start_position :
                    self.process((down_row,down_column))
                else:
                    self.process((down_row,down_column))
            elif not is_down_visited and not (down_row, down_column) == self.end_position:
                next_step = [self.step_grid[start_x][start_y][0] + 1]
                self.step_grid[down_row][down_column][0] = min(next_step)
                self.step_grid[down_row][down_column][1] = True
                self.process((down_row,down_column))
            elif not is_down_visited and (down_row, down_column) == self.end_position:
                next_step = [self.step_grid[start_x][start_y][0] + 1]
                self.step_grid[down_row][down_column][0] = min(next_step)
                self.step_grid[down_row][down_column][1] = True
                return
        
        
        # go left
        if (left_row, left_column) in self.possible_position and self.is_moveable_toward(current_position,(left_row, left_column)):    
            is_left_visited = self.step_grid[left_row][left_column][1]
            if is_left_visited and self.step_grid[left_row][left_column][0] > min(next_step):
                next_step = [self.step_grid[start_x][start_y][0] + 1]
                next_step += self.shortest((left_row, left_column),letters)
                self.step_grid[left_row][left_column][0] = min(next_step)
                if (left_row, left_column) == self.end_position or (left_row, left_column) == self.start_position :
                    self.process((left_row,left_column))
                else:
                    self.process((left_row,left_column))
            elif not is_left_visited and not (left_row, left_column) == self.end_position:
                next_step = [self.step_grid[start_x][start_y][0] + 1]
                self.step_grid[left_row][left_column][0] = min(next_step)
                self.step_grid[left_row][left_column][1] = True
                self.process((left_row,left_column))
            elif not is_left_visited and (left_row, left_column) == self.end_position:
                next_step = [self.step_grid[start_x][start_y][0] + 1]
                self.step_grid[left_row][left_column][0] = min(next_step)
                self.step_grid[left_row][left_column][1] = True
                return

        # run right
        if (right_row, right_column) in self.possible_position and self.is_moveable_toward(current_position,(right_row, right_column)):    
            is_right_visited = self.step_grid[right_row][right_column][1]
            if is_right_visited and self.step_grid[right_row][right_column][0] > min(next_step):
                next_step = [self.step_grid[start_x][start_y][0] + 1]
                next_step += self.shortest((right_row, right_column),letters)
                self.step_grid[right_row][right_column][0] = min(next_step)
                if (right_row, right_column) == self.end_position or (right_row, right_column) == self.start_position :
                    self.process((right_row,right_column))
                else:
                    self.process((right_row,right_column))
            elif not is_right_visited and not (right_row, right_column) == self.end_position:
                next_step = [self.step_grid[start_x][start_y][0] + 1]
                self.step_grid[right_row][right_column][0] = min(next_step)
                self.step_grid[right_row][right_column][1] = True
                self.process((right_row,right_column))
            elif not is_right_visited and (right_row, right_column) == self.end_position:
                next_step = [self.step_grid[start_x][start_y][0] + 1]
                self.step_grid[right_row][right_column][0] = min(next_step)
                self.step_grid[right_row][right_column][1] = True
                return
            


def processing_input(file_path,position,step_grid):
    data = open(file_path, "r")
    data_list = []

    
    
    for index, line in enumerate(data.readlines()):
        data_list += [[e for e in line.strip()]]
        step_grid += [[[0,False] for e in line.strip()]]

    for i,data_row in enumerate(data_list):
        for j,data in enumerate(data_row) :
            if data == 'S':
                position['start'] = (i,j)
            if data == 'E':
                position['end'] = (i,j)

    return data_list

def main():
    data_list = processing_input(file_path,position,step_grid)
    # print(data_list)
    grid = GridWithSteps(data_list,position,step_grid) 
    # print(grid.start_position,grid.end_position)
    grid.process_new()
    # print()
    # for i in grid.step_grid:
    #     print(i)
    # part 1
    # grid.get_shortest_end()
    grid.get_shortest_start()
    return


if __name__ == "__main__":
    main()