file_path = 'day_04\day4_data.txt'

def processing_input(file_path):
    data = open(file_path, "r")
    data_list = []
    for line in data.readlines():
        data_list += [line.strip()]
    return data_list

# part 1
def check_subset_range(data_list):
    sum_subset_section = 0
    for line in data_list:
        first_elf, second_elf = line.strip().split(',')
        first_elfs_section_start,first_elfs_section_end  = (int(e) for e in first_elf.split('-')) 
        second_elfs_section_start,second_elfs_section_end  = (int(e) for e in second_elf.split('-'))
        first_section = set(e for e in range(first_elfs_section_start,first_elfs_section_end+1))
        second_section =  set(e for e in range(second_elfs_section_start,second_elfs_section_end+1))
        if first_section.issubset(second_section) or second_section.issubset(first_section):
            sum_subset_section += 1
    return sum_subset_section

# part 2
def check_intersect_range(data_list):
    sum_subset_section = 0
    for line in data_list:
        first_elf, second_elf = line.strip().split(',')
        first_elfs_section_start,first_elfs_section_end  = (int(e) for e in first_elf.split('-')) 
        second_elfs_section_start,second_elfs_section_end  = (int(e) for e in second_elf.split('-'))
        first_section = set(e for e in range(first_elfs_section_start,first_elfs_section_end+1))
        second_section =  set(e for e in range(second_elfs_section_start,second_elfs_section_end+1))
        if len(first_section.intersection(second_section)) > 0:
            sum_subset_section += 1
    return sum_subset_section

def main():
    data_list = processing_input(file_path)
    # print(check_subset_range(data_list))
    print(check_intersect_range(data_list))
    return

if __name__ == "__main__":
    main()