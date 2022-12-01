file_path = 'day_01\day1_data.txt'



def processing_input(file_path):
    data_file = open(file_path, "r")

    calories_dict = {}
    elf_number = 0
    for line in data_file.readlines():
        if line != "\n":
            if calories_dict.get(elf_number) == None:
                calories_dict[elf_number] = [int(line.strip())]
            else:
                calories_dict[elf_number].append(int(line.strip()))
        else:
            elf_number += 1
    return calories_dict


# part 1
def most_carried(calories_dict):
    return max(sum(e) for e in calories_dict.values())

# part 2
def most_three_carried(calories_dict):
    return sum(sorted([sum(e) for e in calories_dict.values()], reverse=True)[:3])


if __name__ == "__main__":
    calories_dict = processing_input(file_path)
    print(most_three_carried(calories_dict))