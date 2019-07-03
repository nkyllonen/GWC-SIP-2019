'''
Module for sorting a dictionary using it's values.

Source:
https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
'''
import operator

'''
sort_by_values: returns list of sorted (key, value) tuples
'''
def sort_by_values(dictionary):
    sorted_x = sorted(dictionary.items(), key=operator.itemgetter(1))
    return sorted_x

'''
get_max_N: return list of top N tuples from the sorted list
'''
def get_max_N(tuples, N):
    start = len(tuples) - N
    top10 = tuples[start:]
    return top10

def main():
    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

    # sort by value into (key, value) tuples
    sorted = sort_by_values(x)
    print(sorted)

    # get top 2 tuples
    top = get_max_N(sorted, 2)
    print(top)

if __name__ == '__main__':
    main()
