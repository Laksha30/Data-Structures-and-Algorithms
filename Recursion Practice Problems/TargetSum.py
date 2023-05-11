def TargetSum(i, Sum, n, arr, target, subsetSum):
    
    if i >= n:
        print(Sum)
        if Sum == target:
            flag = 1
        return 
    
    #pick
    TargetSum(i+1, Sum+arr[i], n, arr, target, flag)

    #reject
    TargetSum(i+1, Sum, n, arr, target, flag)


arr = list(map(int, input().split()))
target = int(input())
print(TargetSum(0, 0, len(arr), arr, target, []))
