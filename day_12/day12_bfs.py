from collections import deque

file_path = 'day_12\day12_data.txt'

class Grid:

    def __init__(self,data_list,is_part2=False) -> None:
        self.data = data_list 
        self.grid = {} # grid of height
        self.is_visited = set() 
        self.queue = deque()
        self.is_part2 = is_part2
        for r, row in enumerate(self.data):
            for c, char in enumerate(row):
                if char == 'E':
                    self.grid[(r,c)] = ord('z')- ord('a')
                    self.end_position = (r,c)
                elif char == 'S':
                    self.queue.append((char,r,c,0)) # char, row, column, distance
                    self.grid[(r,c)] = 0
                elif is_part2 and char == 'a':
                    self.queue.append((char,r,c,0)) # char, row, column, distance
                    self.grid[(r,c)] = 0
                else:
                    self.grid[(r,c)] = ord(char) - ord('a')
                
                    

    def process_shortest(self):
        while self.queue:
            char,row,column,distance = self.queue.popleft()
            if self.end_position == (row,column):
                return distance 
            if (row,column) in self.is_visited:
                continue
            self.is_visited.add((row,column))
            for row_diff, column_diff in [(0,1),(1,0),(-1,0),(0,-1)]:
                next_in_queue_row = row+row_diff
                next_in_queue_column = column+column_diff
                if (next_in_queue_row,next_in_queue_column) in self.grid.keys():
                    if self.grid[(row,column)] + 1 >= self.grid[(next_in_queue_row,next_in_queue_column)]:
                        next_char = self.data[next_in_queue_row][next_in_queue_column]
                        self.queue.append((next_char,next_in_queue_row,next_in_queue_column,distance + 1))
    
    def debug(self):
        for r, row in enumerate(self.data):
            each_row = []
            for c, char in enumerate(row):
                each_row += [self.grid[(r,c)]]
            print(each_row)
                


def processing_input(file_path):
    data = open(file_path, "r")
    data_list = []

    for index, line in enumerate(data.readlines()):
        data_list += [[e for e in line.strip()]]
    return data_list

def main():
    data_list = processing_input(file_path)
    grid_part1 = Grid(data_list)
    # print(grid_part1.debug())
    val = grid_part1.process_shortest()
    print(f'part 1 : {val}')

    
    grid_part2 = Grid(data_list,True)
    # print(grid_part2.debug())
    val = grid_part2.process_shortest()
    print(f'part 2 : {val}')
    # grid.debug()

    return


if __name__ == "__main__":
    main()
