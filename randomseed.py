import random

seed = 6668666

random.seed(a=seed)

#36 numbers

#each number is chosen by picking 4 numbers 1 to 6 inclusive and summing the three highest

def roll_stat():
    draw_four = []
    for i in range(4):
        draw = random.randint(1, 6)
        draw_four.append(draw)
    draw_four.sort()
    summands = draw_four[1::]
    return sum(summands)

def format_output(sample_setlist):
    row_list = [sample_setlist[6*n:6*n+6] for n in range(6)]
    col_list= [sample_setlist[n::6] for n in range(6)]
    
    return row_list, col_list
    

def create_sample_grid(length=36):
    sample_set = []
    for i in range(36):
        sample_set.append(roll_stat())

    row_list, col_list = format_output(sample_set)

    return row_list, col_list, sample_set

def diagonals(sample):
    topleft = [sample[i][i] for i in range(6)]
    topright = [sample[i][5-i] for i in range(6)]

    return [topleft, topright]

def output_grid(grid):
    print("\n------------------------NEW OUTPUT--------------------------")
    print("\nOutput Grid:")
    for i in range(len(grid)):
        print(grid[i])
