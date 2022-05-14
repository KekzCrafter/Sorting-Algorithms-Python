def insertsort(list):
    length = len(list)
    i = 1

    # Sort as long the whole list hasn't been sorted
    while i < length:

        element = list[i]
        j = i
        
        # Is the selected element lower than it's nearby element to the left?
        # Keep comparing and switch position if needed
        while (j > 0) and element < list[j - 1]:
            list[j] = list[j - 1]
            list[j - 1] = element

            j = j - 1

        # Keep element at position
        list[j] = element
        i = i + 1
    
    return list