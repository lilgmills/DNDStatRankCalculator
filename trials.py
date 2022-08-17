from randomseed import *


def new_master_list(list_of_candidates):
    new_masterlist = []
    for candidate in list_of_candidates:
        new_masterlist.extend(candidate)

    return new_masterlist

def max_stat(stat_rolls):
    master = new_master_list(stat_rolls)

    try: return max(master)
    except: return

def max_two_of_top_ranking(stat_rolls):

    ranked_rolls = rank_stat_roll_best_top_two(stat_rolls)[-1][::]

    ranked_rolls.sort()

    return ranked_rolls[-1], ranked_rolls[-2]    
        
    
def top_two_sum(stat_rolls):
    
    maximum_sums = []
    current_max = None
    
    for i, stat_list in enumerate(stat_rolls):
        sort_stat_list = stat_list[::]
        sort_stat_list.sort()
        s = sort_stat_list[-1]
        t = sort_stat_list[-2]
        current_max = s + t

        maximum_sums.append(current_max)

    return max(maximum_sums)


def obtain_best_max_for_two_stat_fills(stat_rolls):
    #requirements:
    #contains the max sum of the highest two stats
    #contains the lowest sum of remaining entries

    lowest_remaining_sum = None
    obtains_max = []           #list of indices and stat roll candidates that meet the max condition for top two values
    remaining_sums = []
    idxs = []

    current_max_top_two_sum = top_two_sum(stat_rolls)

    max_value = None
    second_max_value = None

    for i, rolls in enumerate(stat_rolls):
        sorted_rolls = rolls[::]

        sorted_rolls.sort()

        top_roll = sorted_rolls[-1]
        second_best = sorted_rolls[-2]
        
        stat_list_top_sum = top_roll + second_best
        
        if stat_list_top_sum == current_max_top_two_sum:
            obtains_max.append([i, rolls])

            del sorted_rolls[-1]
            del sorted_rolls[-1] # this was originally a mistake: we just need to delete the [-1] element twice; the
                                 # second largest will be the new [-1] entry when the [-1] entry is deleted

            remaining_sum = sum(sorted_rolls)
            remaining_sums.append(remaining_sum)

            idxs.append(i)

            if lowest_remaining_sum is None:
                lowest_remaining_sum = remaining_sum
            elif remaining_sum < lowest_remaining_sum:
                lowest_remaining_sum = remaining_sum

    # obtains_max
    # remaining_sums
    # remaining_sum
    # returns, idx, stat_roll[at_idk]
    
    # we have to run through the "obtains_max" indices once more to determine which one has the lowest remaining sum

    for i, candidate in enumerate(obtains_max):
        if remaining_sums[i] == lowest_remaining_sum:
            at_idx = idxs[i]
            return at_idx, stat_rolls[at_idx]


            
def obtain_best_candidate(stat_rolls):
    #requirements:
    #contains the max stat
    #obtains the lowest sum of remaining entries

    lowest_remaining_sum = None
    obtains_max = []            #list of indices and stat roll candidates that meet the max condition
    remaining_sums = []
    idxs = []

    current_max = max_stat(stat_rolls)

    for i, rolls in enumerate(stat_rolls):                  
        rolls_set = set(rolls)
        if current_max in rolls_set:
            obtains_max.append([i, rolls])
            
            sorted_rolls = rolls[::]
            sorted_rolls.sort()
            
            del sorted_rolls[-1]
            
            remaining_sum = sum(sorted_rolls)
            remaining_sums.append(remaining_sum)

            idxs.append(i)
            
            if lowest_remaining_sum is None:
                lowest_remaining_sum = remaining_sum              
            elif remaining_sum < lowest_remaining_sum:
                lowest_remaining_sum = remaining_sum

    for i, candidate in enumerate(obtains_max):
        if remaining_sums[i] == lowest_remaining_sum:
            at_idx = idxs[i]
            return at_idx, stat_rolls[at_idx]
    

def rank_stat_rolls(stat_rolls):
    if stat_rolls == []:
        return []
    else:
        idx, best = obtain_best_candidate(stat_rolls)

        new_vector = stat_rolls[::]

        del new_vector[idx]

        # print("\n index: ", idx, "\n best: ", best, " \n stat_rolls[" + str(idx) + "]: ", stat_rolls[idx])

        # print("\n new_vector: ", new_vector)
        
        return rank_stat_rolls(new_vector) + [best]

def rank_stat_roll_best_top_two(stat_rolls):
    if stat_rolls == []:
        return []
    else:
        idx, best = obtain_best_max_for_two_stat_fills(stat_rolls)

        new_vector = stat_rolls[::]

        del new_vector[idx]
        
        return rank_stat_roll_best_top_two(new_vector) + [best]


def print_ranking():
    rows, cols, sample_set = create_sample_grid()

    output_grid(rows)
    
   
    print("\nDiagonals:")
    print(diagonals(rows))
    print("\n-------------------------------------------------------------")
    print("------------------------NEW RANKING--------------------------")
    print("-------------------------------------------------------------")

    list_of_stat_rolls = rows + cols + diagonals(rows)

    print("max stat roll: ", max_stat(list_of_stat_rolls))
    print("max two of best stat roll: ", "".join(str(max_two_of_top_ranking(list_of_stat_rolls)))[1:-1])

    print("list of all stat roll candidates: ", list_of_stat_rolls)

    print("ranking:\n",rank_stat_rolls(list_of_stat_rolls))

    print("ranking best two:\n",rank_stat_roll_best_top_two(list_of_stat_rolls))
    return

def run_seed(a = seed):
    random.seed(a)
    print_ranking()


for a in range(77, 89):
    run_seed(a)
    



        
