def partition(left, right, arr):
    pivot = arr[right]
    i = left - 1
    print("Pivot {}".format(pivot))
    print("i {}".format(i))

    for j in range(left, right):
        print("j {} Arr[j] {} Pivot {}".format(j, arr[j], pivot))
        if arr[j]<=pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)

    arr[i+1], arr[right] = arr[right], arr[i+1]
    print(arr)

    return i+1


def quickSort(left, right, arr):
    if left < right:
        p = partition(left, right, arr)
        print("P {}".format(p))
        quickSort(left, p-1, arr)
        quickSort(p+1, right, arr)


arr = [8, 7, 6, 1, 0, 9, 2]
print(arr)
quickSort(0, len(arr)-1, arr)
print(arr)