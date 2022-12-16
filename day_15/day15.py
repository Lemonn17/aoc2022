import re
from collections import deque
import time

file_path = 'day_15\day15_data.txt'


def distance(x,y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


def processing_input(file_path):
    data = open(file_path, "r")
    lines = data.readlines()
    data_list = []

    for line in lines:
        temp_sensor, temp_beacon =  line.strip().split(':')
        re_extract = r"x=\-*\d+\,\sy=\-*\d+"
        temp_str_sensor = re.findall(re_extract,temp_sensor)[0].replace('x=','').replace('y=','').replace(' ','')
        temp_str_beacon = re.findall(re_extract,temp_beacon)[0].replace('x=','').replace('y=','').replace(' ','')
        sensor = [tuple(i for i in [int(e) for e in temp_str_sensor.split(',')]) ]
        beacon = [tuple(i for i in [int(e) for e in temp_str_beacon.split(',')]) ]
        temp = sensor + beacon
        data_list += [temp]
    return data_list

class World:

    def __init__(self,data_list,row) -> None:
        self.sb_coor = data_list
        self.sensor_range_row = set()
        self.sensor = set()
        self.beacon = set()

        for idx,sb in enumerate(self.sb_coor):
            # print(f'running : {idx}')
            s,b = (sb[0],sb[1])
            d = distance(s,b)
            self.sensor.add((s[0],s[1],d))   
            remainning_distance = d - abs(s[1] - row)
            for i in range(s[0] - remainning_distance, s[0] + remainning_distance + 1):
                self.sensor_range_row.add((i,row))
                # 4898736
            if b[1] == row:
                self.beacon.add(b) 
        pass

    def solve_1(self):
        
        # part 1
        print(len(self.sensor_range_row) - len(self.beacon))
        # if self.sensor_range_row != set():
        #     return max(self.sensor_range_row)[0] - min(self.sensor_range_row)[0] + 1 == len(self.sensor_range_row)
        # else:
        #     return False
        # print()

    def possible_beacon(self):
        for sx,sy,d in self.sensor:
            s = (sx,sy)
            for dx in range(d + 2):
                # top right edge
                dy = d + 1 - dx
                for x,y in [(s[0] + dx,s[1] + dy),(s[0] + dx,s[1] - dy),(s[0] - dx,s[1] + dy),(s[0] - dx,s[1] - dy)]:
                    # print(self.check_exist_all_sensors(temp[0],temp[1]),s) 
                    if not (0 <= x <= 4000000 and 0 <= y <= 4000000):
                        continue
                    if self.check_exist_all_sensors(x,y):
                        return (4000000 * x) + y

    def check_exist_all_sensors(self,x,y):
        for sx,sy,d in self.sensor:
            s = (sx,sy)
            if distance((x,y),s) <= d:
                return False
        return True
    def solve_2(self):
        
        print(f"part 2 done {self.possible_beacon()}")





def main():
    
    data_list = processing_input(file_path)
    world = World(data_list=data_list,row=2000000)
    world.solve_1()
    world.solve_2()
    return


if __name__ == "__main__":
    main()
