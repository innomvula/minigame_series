def bubble_sort(lst):
    n = len(lst)
    swap_occurred = True
    while swap_occurred:
        swap_occurred = False
        for i in range(n - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap_occurred = True
    return lst
            
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        minidx = i
        for j in range(i + 1, n):
            if lst[j] < lst[minidx]:
                minidx = j
        lst[i], lst[minidx] = lst[minidx], lst[i]
    return lst
        