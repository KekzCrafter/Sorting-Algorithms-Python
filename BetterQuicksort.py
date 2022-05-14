def quicksort(L, anfang, ende):
    if L != []:
        pivot = L[anfang]
        links = anfang
        rechts = ende

        while links <= rechts:
            while L[links] < pivot:
                links = links + 1

            while L[rechts] > pivot:
                rechts = rechts - 1

            if links <= rechts:
                if links < rechts:
                    h = L[links]
                    L[links] = L[rechts]
                    L[rechts] = h

                links = links + 1
                rechts = rechts - 1

            if anfang < rechts:
                L = quicksort(L, anfang, rechts)
            if links < ende:
                L = quicksort(L, links, ende)
        
        return L