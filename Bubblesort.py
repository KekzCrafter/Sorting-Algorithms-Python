def bubblesort(list):
    length = len(list)

    # Sort as long the whole list hasn't been sorted
    while(length > 0):

        # Compare first element with all other elements that haven't been sorted already
        for i in range(0, length - 1):

            # Next element to compare
            first = list[i]
            compare = list[i + 1]

            # Switch positions if first element is larger
            if first > compare:
                list[i] = compare
                list[i + 1] = first
        
        length -= 1
    
    return list