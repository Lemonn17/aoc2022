file_path = 'day_06\day6_data.txt'

def processing_input(file_path):
    data = open(file_path, "r")
    data_list = []
    for line in data.readlines():
        data_list += [line.strip()]
    return data_list


def start_of_packet_marker(data_list,number_of_distinct_char):
    list_of_char = []
    for index, char in enumerate(data_list[0]):
        if index > number_of_distinct_char-1:
            chars = data_list[0][index-number_of_distinct_char:index]
            set_char = set(e for e in chars)

            if len(set_char) == len(chars):
                return index

def main():
    data_list = processing_input(file_path)
    # part 1
    print(start_of_packet_marker(data_list,4))
    # part 2
    print(start_of_packet_marker(data_list,14))
    return

if __name__ == "__main__":
    main()