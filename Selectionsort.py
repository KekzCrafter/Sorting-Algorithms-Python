def selectionsort(list):
    length = len(list)
    i = 0

    # Sort as long the whole list hasn't been sorted
    # -1, so that the last number isn't compared with itself
    while(i < length - 1):
        
        min = i
        j = i + 1

        # Find the index of the lowest number
        while(j < length):
            first = list[min]
            compare = list[j]

            if compare < first:
                min = j

            j += 1

        # Bring lowest found number to positon
        first = list[i]
        list[i] = list[min]
        list[min] = first

        i += 1

    return list