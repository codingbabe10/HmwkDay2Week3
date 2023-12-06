
Exersize 1:

def in_place_reverse(lst):
    start, end = 0, len(lst) - 1

    while start < end:
        # Swap elements at start and end indices
        lst[start], lst[end] = lst[end], lst[start]

        # Move indices towards each other
        start += 1
        end -= 1

# Example usage:
my_list = [1, 2, 3, 4, 5]
in_place_reverse(my_list)
print(my_list)




def swap(lst, i, j):
    # Swaps elements at indices i and j in the list
    lst[i], lst[j] = lst[j], lst[i]

def in_place_reverse(lst):
    start, end = 0, len(lst) - 1

    while start < end:
        # Use the custom swap function to swap elements
        swap(lst, start, end)

        # Move indices towards each other
        start += 1
        end -= 1

# Example usage:
my_list = [1, 2, 3, 4, 5]
in_place_reverse(my_list)
print(my_list)




