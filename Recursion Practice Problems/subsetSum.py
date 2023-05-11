def subsetSum(ind, sum, arr, n, subset):
    if ind == n:
        subset.append(sum)
        #print(subset)
        return 
    
    #pick
    subsetSum(ind+1, sum+arr[ind], arr, n, subset)

    #not-pick
    subsetSum(ind+1, sum, arr, n, subset)

    print(subset.sort())


arr = list(map(int, input().split()))
subsetSum(0, 0, arr, len(arr), [])
