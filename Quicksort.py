def quicksort(list):
    if list != []:

        # Save pivot element
        pivot = list[0]

        # Remove pivot element
        list.remove(pivot)

        # Create two empty lists
        lower, higher = [], []

        # Compare other numbers with pivot
        for x in list:
            if x < pivot:
                lower = lower + [x]
            else:
                higher = higher + [x]

        # Recursion: sort the two lists from beginning
        lower_sorted = quicksort(lower)
        higher_sorted = quicksort(higher)

        # Get all together
        list = lower_sorted + [pivot] + higher_sorted

    return list