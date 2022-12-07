file_path = 'day_07\day7_data.txt'

def processing_input(file_path):
    data = open(file_path, "r")
    data_list = []
    for line in data.readlines():
        data_list += [line.strip()]
    return data_list

def directory_dict(data_list):
    dir = {}
    current_dir = ['/']
    for data in data_list:
        # Check command
        print(current_dir)
        if data.strip()[0] != '$':
            size_or_type,file_name = data.strip().split(' ')
            if ''.join(current_dir) in dir.keys():
                dir[''.join(current_dir)] += [(''.join(current_dir) + file_name + '/',size_or_type)]
            else:
                dir[''.join(current_dir)] = [(''.join(current_dir) + file_name + '/',size_or_type)]
        elif data.strip() == '$ cd ..':
            current_dir = current_dir[:-2]
        elif data.strip() == '$ cd /':
            current_dir = ['/']
        elif data.strip() != '$ ls':
            go_to = data.split(' ')[-1]
            current_dir += [go_to,'/']
            # if go_to in 
    # print(dir)
    return dir

# dir_size {dir: size, '/a/e/' : 584}
def dir_size(dir):
    list_of_keys = list(dir.keys())
    list_of_keys.sort(key=len,reverse=True)
    size_dict = {}
    for directory in list_of_keys:
        dir_size = 0
        for item in dir[directory]:
            if item[1] != 'dir':
                dir_size += int(item[1])
            else:
                dir_size += size_dict[item[0]]
        size_dict[directory] = dir_size
    return size_dict

def solve_1(size_dict):
    print(sum(filter(lambda x: x <= 100000,list(size_dict.values()))))

def solve_2(size_dict):
    total_size = 70000000
    needed_size = 30000000
    dir_used = max(size_dict.values())
    dir_size = list(size_dict.values())
    dir_size.sort(reverse=False)
    free_space = total_size - dir_used
    delete_size_require_atleast = needed_size - free_space
    for size in dir_size:
        if size >= delete_size_require_atleast:
            return size


def main():
    data_list = processing_input(file_path)
    dir = directory_dict(data_list)
    size_dict = dir_size(dir)
    # part 1
    solve_1(size_dict)
    print(solve_2(size_dict))
    return

if __name__ == "__main__":
    main()
