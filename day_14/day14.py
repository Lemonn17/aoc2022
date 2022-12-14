import time

file_path = 'day_14\day14_data.txt'

class Cave():
    def __init__(self,data_list,is_part2=False) -> None:
        self.rocks = set()
        self.sands = set()
        self.start = (500,-1)
        self.last_sand = (-1,-1)
        self.lowest_rock = 9999
        self.generate_rock(data_list)
        self.is_part2 = is_part2
        self.floor = self.lowest_rock + 2
        self.sand_counter = 0
        pass

    def sand_loop(self):
        temp = True
        while temp:
            temp = self.falling_sand(self.start)
            if temp == (9999,9999):
                break
            
        if self.is_part2:
            print('---- part 2 ----')
        else:
            print('---- part 1 ----')
        print('Sand : ',self.sand_counter, " : ", temp)

    def falling_sand(self,coor):
        x,y = coor
        down = (x,y+1)
        down_left = (x-1,y+1)
        down_right = (x+1,y+1)
        
        # exit case
        # ---- part 1 ----
        if not self.is_part2:
            if y >= self.floor:
                return (9999,9999)
        # ---- part 1 ----

        # ---- part 2 ----
        elif self.is_part2:
            if y > self.floor:
                return (9999,9999)
            elif y == self.floor:
                x_start_coor = x - 5
                x_end_coor = x + 5
                y_coor = self.floor
                # print(f"...creating floor ")
                temp_list = [[(x_start_coor,y_coor),(x_end_coor,y_coor)]]
                self.generate_rock(temp_list)
                return (-1,-1) # add floor and gen new sand
            elif (500,0) in self.sands or (500,0) in self.rocks:
                return (9999,9999)
        # ---- part 2 ----
            

        # down
        if not (down in self.rocks or down in self.sands):
            return self.falling_sand(down)

        # left
        elif not (down_left in self.rocks or down_left in self.sands):
            return self.falling_sand(down_left)

        # right
        elif not (down_right in self.rocks or down_right in self.sands):
            return self.falling_sand(down_right)
        # stop
        elif (down in self.rocks or down in self.sands):
            self.sands.add((x,y))
            self.sand_counter += 1
            self.last_sand = (x,y)
            return (x,y)

        
    def generate_rock(self,data_list):
        for index,data_line in enumerate(data_list):
            for i in range(1,len(data_line)):
                start_x,start_y = data_line[i-1]
                end_x,end_y = data_line[i]

                while (start_x,start_y) != (end_x,end_y):
                    self.rocks.add((start_x,start_y))
                    self.rocks.add((end_x,end_y))
                    if start_x == end_x:
                        if start_y < end_y:
                            start_y += 1
                            self.rocks.add((start_x,start_y))
                            continue
                        else:
                            start_y += -1
                            self.rocks.add((start_x,start_y))
                            continue
                    elif start_y == end_y:
                        if start_x < end_x:
                            start_x += 1
                            self.rocks.add((start_x,start_y))
                            continue
                        else:
                            start_x += -1
                            self.rocks.add((start_x,start_y))
                            continue

        self.lowest_rock = max(self.rocks, key = lambda t:t[1])[1]
        return



def processing_input(file_path):
    data = open(file_path, "r")
    lines = data.readlines()
    data_list = map(lambda line: map(lambda coor: tuple([int(e) for e in coor.split(',')]),line) ,[e.strip().split(' -> ') for e in lines])
    return list(map(lambda x: list(x),data_list))
def main():
    
    data_list = processing_input(file_path)
    a = Cave(data_list)
    # print(data_list)
    a.sand_loop()
    
    b = Cave(data_list,is_part2=True)
    b.sand_loop()
    return


if __name__ == "__main__":
    main()