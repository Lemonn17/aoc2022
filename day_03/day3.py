import string

file_path = 'day_03\day3_data.txt'

letters = [ e for e in string.ascii_lowercase] + [e for e in string.ascii_uppercase]
priority = {}

for index, charactor in enumerate(letters):
    priority[charactor] = index + 1

def processing_input(file_path):
    data = open(file_path, "r")
    data_list = []
    for line in data.readlines():
        data_list += [line.strip()]
    return data_list

#part 1
def rearrangement(data_list):
    sum_priority = 0
    for rug_sack in data_list:
        compartment_ize = int(len(rug_sack)/2)
        first_compartment = set(e for e in rug_sack[:compartment_ize])
        second_compartment = set(e for e in rug_sack[compartment_ize:])
        duplicate_char = ''.join(first_compartment.intersection(second_compartment))
        sum_priority += priority[duplicate_char]
    return sum_priority

#part 2
def rearrangementV2(data_list):
    sum_priority = 0
    processing_data = []
    for index, rug_sack in enumerate(data_list):
        if index % 3 == 2:
            processing_data += [set(e for e in rug_sack)]
            common_char = ''.join( processing_data[0].intersection(processing_data[1]).intersection(processing_data[2]))
            sum_priority += priority[common_char]
            processing_data = []
        else:
            processing_data += [set(e for e in rug_sack)]
    return sum_priority

def main():
    data_list = processing_input(file_path)
    # print(rearrangement(data_list))
    print(rearrangementV2(data_list))
    return

if __name__ == "__main__":
    main()