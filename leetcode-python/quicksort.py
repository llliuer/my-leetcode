ARR = [26, 44, 38, 5, 47, 15, 36, 3, 27, 2, 46, 4, 19, 50, 48]


def getPivotIndex(arr, i, j):
    pivot = arr[i]
    iturn = 0
    jturn = 1
    while i < j:
        if jturn:
            if arr[j] > pivot:
                j = j - 1
            else:
                jturn = 0
                iturn = 1
                arr[i] = arr[j]
                i = i + 1
            continue
        if iturn:
            if arr[i] < pivot:
                i = i + 1
            else:
                jturn = 1
                iturn = 0
                arr[j] = arr[i]
                j = j - 1
    arr[i] = pivot
    return i


def quicksort(arr, low, high):
    if low < high:
        pivot = getPivotIndex(arr, low, high)

        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)
    return


ARR = [26, 44, 38, 5, 47, 15, 36, 3, 27, 2, 46, 4, 19, 50, 48]
quicksort(ARR, 0, len(ARR) - 1)
print(ARR)
