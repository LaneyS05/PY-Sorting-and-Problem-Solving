# Write your solution for algorithm 2 below
def sort_list(list):
    sorted_list = sorted(list)
    return sorted_list

unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Unsorted List:", unsorted_list)

sorted_result = sort_list(unsorted_list)
print("Sorted List:", sorted_result)
