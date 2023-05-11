def paramSum(n, sum):
    if n == 0:
        print("Parameterized sum is {}".format(sum))
        return 
    
    paramSum(n-1, sum+n)


def functSum(n):
    if n < 1:
        return 0
    
    return n + functSum(n-1)


n = int(input())
paramSum(n, 0)
print("Functional Sum is {}".format(functSum(n)))