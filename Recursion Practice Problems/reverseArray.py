def reverseArray(i, n, arr):
    if i >= n/2:
        return 
    
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    reverseArray(i+1, n, arr)


arr = list(map(int, input().split()))
reverseArray(0, len(arr), arr)
print(arr)