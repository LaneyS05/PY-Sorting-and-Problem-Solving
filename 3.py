# Write your solution for algorithm 3 below
def sort_list_descending(list):
    sorted_list = sorted(list, reverse=True)
    return sorted_list

unsorted_list = [3, 1, 4, 9, 2, 6, 5]
print("Unsorted List:", unsorted_list)

sorted_descending = sort_list_descending(unsorted_list)
print("Sorted List:", sorted_descending)
