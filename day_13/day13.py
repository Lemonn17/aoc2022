from functools import cmp_to_key

file_path = 'day_13\day13_data.txt'

def order(data_list,order_list):
    sum_indx = 0
    
    for idx, pair in enumerate(data_list):
        # print(pair)
        left,right = (pair[0],pair[1])
        order_list += [left,right]
        temp = compare(left,right)
        if temp == -1:
            sum_indx += idx + 1
            print(f'pair {idx + 1} : True \t {pair} \n\n' )
        else:
            print(f'pair {idx + 1} : False \t {pair} \n\n' )
    # print(order_list)
    print(sum_indx)
    
        
def compare(left_input,right_input):
    left = left_input
    right = right_input
    # print(f'comparing : {left} | {right} ')
    if isinstance(left,int) and isinstance(right,int):
        if left < right:
            return -1 # true
        if left == right:
            return 0 # equal
        else:
            return 1 # false
    elif isinstance(left, list) and isinstance(right, list):
        if left == [] and right == []:
            return 0
        elif left == []:
            return -1
        elif right == []:
            return 1
        else:

            temp_left = left[0]
            temp_right = right[0]
            temp = compare(temp_left,temp_right)
            # print('################',temp,temp != "None")
            if temp == 0:
                return compare(left[1:],right[1:])
            else:
                return temp
    elif isinstance(left, int) and isinstance(right, list):
        return compare([left],right)
    elif isinstance(left, list) and isinstance(right, int):
        return compare(left,[right])



def processing_input(file_path):
    data = open(file_path, "r")
    lines = data.read()
    data_list = [] + [e.split('\n') for e in lines.split('\n\n')]
    for i, each_pair in enumerate(data_list):
        data_list[i] = [eval(each_pair[0]),eval(each_pair[1])]
        
    return data_list
def main():
    
    data_list = processing_input(file_path)
    order_list = [[[2]],[[6]]]
    # part 1
    print("------------part 1------------")
    order(data_list,order_list)

    print("------------part 2------------")
    temp = sorted(order_list, key=cmp_to_key(compare))
    result = 1
    for idx,i in enumerate(temp):
        if i in ([[2]],[[6]]):
            result = result * (idx + 1)
    print(result)
    return


if __name__ == "__main__":
    main()
