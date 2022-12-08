file_path = 'day_08\day8_data.txt'

def processing_input(file_path):
    data = open(file_path, "r")
    data_list = []
    for line in data.readlines():
        data_list += [[int(e) for e in line.strip()]]
    return data_list

def interior(data_list):
    grid_x = len(data_list[0])
    grid_y = len(data_list)
    is_interior_tree = []
    
    for i in range(grid_x):
        is_interior_tree += [[]]
        for j in range(grid_y):
            is_interior_tree[i] += [True]

    for i in range(grid_x):
        for j in range(grid_y):
            if i == 0 or j == 0 or i == grid_x -1 or j == grid_y - 1:
                is_interior_tree[i][j] = False
            else :
                is_interior_tree[i][j] = True
    return is_interior_tree

# part 1
def is_visible(data_list,interior_tree):
    visibility_counter = 0
    transpose = [list(e) for e in zip(*data_list)]
    for row, treeRow in enumerate(data_list):
        for column, tree_heigh in enumerate(treeRow):
            if interior_tree[row][column]:
                
                up = max(transpose[column][:row])
                down = max(transpose[column][row+1:])

                left = max(data_list[row][:column])
                right = max(data_list[row][column+1:])


                if tree_heigh > min([up,down,left,right]):
                    visibility_counter += 1
                    print(row,column,tree_heigh, f': {up, down, left, right }')
    return visibility_counter + ((len(interior_tree)*4) -4 )

# part 2
def scenic_score(data_list,interior_tree):
    scenic_scores = []
    transpose = [list(e) for e in zip(*data_list)]
    for row, treeRow in enumerate(data_list):
        for column, tree_heigh in enumerate(treeRow):
            if interior_tree[row][column]:
                
                up = transpose[column][:row]
                down = transpose[column][row+1:]

                left = data_list[row][:column]
                right = data_list[row][column+1:]
            
                up.reverse()
                left.reverse()
                scenic = 1
                for direction in (up,down,left,right):  
                    tree_counter = 0
                    
                    is_block = False
                    for tree in direction:
                        if tree_heigh > tree and not is_block:
                            tree_counter+= 1
                        elif tree_heigh == tree and not is_block:
                            tree_counter+= 1
                            is_block = True
                        elif not is_block:
                            tree_counter+= 1
                            is_block = True
                    scenic = scenic* tree_counter
                    # print(direction,tree_counter, scenic)
                scenic_scores += [scenic]
                    
    return max(scenic_scores)     

# 0,1,2,3,4 -> 1,2,3
def main():
    data_list = processing_input(file_path)
    interior_tree = interior(data_list)
    #part 1
    # print(is_visible(data_list,interior_tree))
    #part 2
    print(scenic_score(data_list,interior_tree))
    return

if __name__ == "__main__":
    main()
