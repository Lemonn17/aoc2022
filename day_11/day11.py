from functools import reduce
import math


file_path = 'day_11\day11_data.txt'
all_monkeys = []
divisible_dict = {}
def processing_input(file_path,all_monkeys):
    data = open(file_path, "r")

    for index, line in enumerate(data.readlines()):
        # print(index+1,line,(index+1) % 7 == 0)
        if (index+1)  % 7 == 2:
            starting_items = [int(e) for e in line.strip().replace("Starting items: ","").split(",")] # 79, 98
        if (index+1)  % 7 == 3:
            operation = line.strip().replace("Operation: new = ","") # old * 19
        if (index+1)  % 7 == 4:
            test_condition = int(line.strip().replace("Test: divisible by ","")) # 23
        if (index+1)  % 7 == 5:
            true_monkey_index = int(line.strip().replace("If true: throw to monkey ","")) # 2
        if (index+1)  % 7 == 6:
            false_monkey_index = int(line.strip().replace("If false: throw to monkey ","")) # 3
        if (index+1) % 7 == 0:
            monkey = Monkey(starting_items,operation,test_condition,true_monkey_index,false_monkey_index)
            all_monkeys += [monkey]
    monkey = Monkey(starting_items,operation,test_condition,true_monkey_index,false_monkey_index)
    all_monkeys += [monkey]



class Monkey:
    def __init__(self,starting_items,operation,test_condition,true_monkey_index,false_monkey_index) -> None:
        self.items = starting_items
        self.ops = operation
        self.test_ops = test_condition
        self.test_true_action = true_monkey_index
        self.test_false_action = false_monkey_index
        self.number_of_inspection = 0
        pass
    
    def cal_ops(self,item):
        old = item
        worry_level = eval(self.ops) 
        return worry_level

    def add_item(self,item):
        self.items += [item]

    # part 1
    def action_part1(self,item):
        new_worry_level = self.cal_ops(item) // 3
        if new_worry_level % self.test_ops == 0:
            all_monkeys[self.test_true_action].add_item(new_worry_level) 
            # print(f"Item : {item} with worry level {new_worry_level} is thrown to monkey {self.test_true_action}")
        else:
            all_monkeys[self.test_false_action].add_item(new_worry_level)
            # print(f"Item : {item} with worry level {new_worry_level} is thrown to monkey {self.test_false_action}")

    # part 2
    def action_part2(self,item):
        lcm = math.lcm(*[monkey.test_ops for monkey in all_monkeys])
        new_worry_level = self.cal_ops(item) % lcm
        if new_worry_level % self.test_ops == 0:
            all_monkeys[self.test_true_action].add_item(new_worry_level) 
            # print(f"Item : {item} with worry level {new_worry_level} is thrown to monkey {self.test_true_action}")
        else:
            all_monkeys[self.test_false_action].add_item(new_worry_level)
            # print(f"Item : {item} with worry level {new_worry_level} is thrown to monkey {self.test_false_action}")

    def inspect(self):
        for item in self.items:
            # self.action_part1(item)
            self.action_part2(item)
            self.number_of_inspection += 1
        self.items = []

def solve(all_monkeys):
    number_of_inspections = []
    for monkey in all_monkeys:
        number_of_inspections += [monkey.number_of_inspection]
    number_of_inspections.sort(reverse=True)
    
    result = reduce((lambda x, y: x * y), number_of_inspections[:2])
    print(result)



def main():
    processing_input(file_path,all_monkeys)
    
    for round in range(10000):
        for index,monkey in enumerate(all_monkeys):
            # print(f"Monkey[{index}]")
            monkey.inspect()
        # print('\n',f'End of round : {round+1} ','\n')
        # for index, i in enumerate(all_monkeys):
            # print(f"Monkey {index}: {i.items}")
        
        
        # print('\n','\n')

    for index,monkey in enumerate(all_monkeys):
        print(f'Monkey {index} inspected items {monkey.number_of_inspection} times')
    solve(all_monkeys)
    # run_program(data_list,register_x)
    # print()
    return

if __name__ == "__main__":
    main()

