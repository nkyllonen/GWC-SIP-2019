'''
Module for sorting a dictionary using it's values.
'''
import operator

'''
sort_by_values: returns list of sorted (key, value) tuples

Source:
https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
'''
def sort_by_values(dictionary):
    sorted_x = sorted(dictionary.items(), key=operator.itemgetter(1))
    return sorted_x

'''
get_max_N: return list of top N tuples from the sorted list
'''
def get_max_N(tuples, N):
    start = len(tuples) - N
    top10 = tuples[start:]      # create sublist containing the last N tuples
    return top10

'''
tuples_to_lists: convert a list of tuples into two lists
    keys    :    list containing the first tuple values
    values  :    list containing the second tuple values
'''
def tuples_to_lists(tuples):
    keys = []
    values = []

    for tup in tuples:
        keys.append(tup[0])
        values.append(tup[1])

    return (keys, values)

def main():
    x = {"a": 2, "b": 4, "c": 3, "d": 1, "e": 0, "f": 5}

    # sort by value into (key, value) tuples
    sorted = sort_by_values(x)
    print(sorted)

    # get top 2 tuples
    top = get_max_N(sorted, 2)
    print(top)

    # convert list of tuples into two lists
    (list_of_keys, list_of_values) = tuples_to_lists(top)
    print("keys: " , list_of_keys)
    print("values: " , list_of_values)

if __name__ == '__main__':
    main()
