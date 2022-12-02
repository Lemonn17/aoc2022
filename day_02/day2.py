file_path = 'day_02\day2_data.txt'


# not so clean
opponent_dict_mapping = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
me_dict_mapping = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}
result_dict_mapping = {'X': 'lost', 'Y': 'draw', 'Z': 'won'}
winning_mapping = [('Rock','Scissors'), ('Scissors','Paper'), ('Paper','Rock')]
losing_mapping = [('Scissors','Rock'), ('Paper','Scissors'), ('Rock','Paper')]
score = {'won': 6, 'draw': 3, 'lost': 0, 'Rock' : 1, 'Paper': 2, 'Scissors':3}


def processing_input(file_path):
    data = open(file_path, "r")
    data_list = []
    for line in data.readlines():
        (opponent, me) = line.strip().split(" ")
        data_list += [(opponent, me)]
    return data_list

# part 1
def calulateScore(data_list):
    my_score = 0
    print(data_list)
    for each_round in data_list:
        if (me_dict_mapping[each_round[1]],opponent_dict_mapping[each_round[0]]) in winning_mapping: # won
            my_score += score['won'] + score[me_dict_mapping[each_round[1]]]
        elif opponent_dict_mapping[each_round[0]] == me_dict_mapping[each_round[1]]: # draw
            my_score += score['draw'] + score[me_dict_mapping[each_round[1]]]
        else:
            my_score += score['lost'] + score[me_dict_mapping[each_round[1]]]
    return my_score


# part 2
def calulateScoreV2(data_list):
    my_score = 0
    for each_round in data_list:
        if result_dict_mapping[each_round[1]] == 'won':
            for e in winning_mapping:
                if opponent_dict_mapping[each_round[0]] == e[1]:
                    my_score += score['won'] + score[e[0]]
        elif result_dict_mapping[each_round[1]] == 'draw':
            my_score += score['draw'] + score[opponent_dict_mapping[each_round[0]]]
        else:
            for e in losing_mapping:
                if opponent_dict_mapping[each_round[0]] == e[1]:
                    my_score += score['lost'] + score[e[0]]
    return my_score

def main():
    data_list = processing_input(file_path)
    print(calulateScoreV2(data_list))
    return

if __name__ == "__main__":
    main()