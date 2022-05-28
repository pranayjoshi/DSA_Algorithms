def BS(lst, num):
    low, high = 0, len(lst)-1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == num:
            return mid
        elif num > lst[mid]:
            low = lst[mid] + 1
        elif num < lst[mid]:
            high = lst[mid] - 1
    else:
        return -1

print(BS([1,2,3,4,5,6,7,8], 6))

