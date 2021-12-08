# Selectionsort
def selectionsort(list):
    length = len(list)
    i = 0

    # Wiederhole, solange komplette Liste nicht verglichen wurde
    # -1, damit letzte Zahl nicht nochmal mit sich selbst verglichen wird
    while(i < length - 1):

        
        print(list)
        min = i
        j = i

        # Finde die Position der kleinsten Zahl in der restlichen Liste
        while(j < length):
            first = list[min]
            compare = list[j]

            if compare < first:
                min = j

            j += 1

        # Tausche verglichene Zahl mit der kleinsten, die oben gefunden wurde
        first = list[i]
        list[i] = list[min]
        list[min] = first

        i += 1

    return list

L = [5, 3, 8, 1, 12, 7, -2]
print(selectionsort(L))

# Bubblesort (better version)
def bubblesort(list):
    length = len(list)

    # Wiederhole, solange komplette Liste nicht verglichen wurde
    while(length > 0):

        # Vergleiche erstes Element mit allen anderen Zahlen
        for i in range(0, length - 1):

            # Element zum vergleichen
            first = list[i]
            compare = list[i + 1]

            # Größeres Element steigt um 1 auf
            if first > compare:
                list[i] = compare
                list[i + 1] = first
        
        length -= 1
    
    return list

# Quicksort (multiple lists version)
def quicksort(list):
    if list != []:

        # Hole Pivot Element (Erstes Element aus Liste)
        pivot = list[0]

        # Entferne Pivot aus Liste
        list.remove(pivot)

        # Erstelle zwei leere Listen
        lower, higher = [], []

        for x in list:
            if x < pivot:
                lower = lower + [x]
            else:
                higher = higher + [x]

        # Rekursion: Sortiere Unterlisten
        lower_sorted = quicksort(lower)
        higher_sorted = quicksort(higher)

        # Zusammenfügen
        list = lower_sorted + [pivot] + higher_sorted

    return list

# Insertsort
def insertsort(list):
    length = len(list)
    i = 0

    # Wiederhole, solange die komplette Liste nicht verglichen wurde
    while i < length:
        element = list[i]
        rest = i
        
        # Ist die ausgewählte Zahl kleiner als die vorherige in der Liste?
        # Vergleiche mit allen vorherigen Zahlen
        while (rest > 0) and element < list[rest - 1]:
            list[rest] = list[rest - 1]
            list[rest - 1] = element

            rest = rest - 1

        list[rest] = element
        i = i + 1
    
    return list