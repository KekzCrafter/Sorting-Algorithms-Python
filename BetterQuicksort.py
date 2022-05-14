def quicksort(l, begin, end):
    if l != []:
        pivot = l[begin]
        left = begin
        right = end

        while left <= right:
            while l[left] < pivot:
                left = left + 1

            while l[right] > pivot:
                right = right - 1

            if left <= right:
                if left < right:
                    h = l[left]
                    l[left] = l[right]
                    l[right] = h

                left = left + 1
                right = right - 1

            if begin < right:
                l = quicksort(l, begin, right)
            if left < end:
                l = quicksort(l, left, end)
        
        return l
