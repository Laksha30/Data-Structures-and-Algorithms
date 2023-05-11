#Print linearly from 1 to N 
#Print linearly from N to 1
#print linearly from 1 to N using backtracking 

def print1toN(i, n):
    if i == n+1:
        return

    print(i)
    print1toN(i+1, n)


def printNto1(n):
    if n == 0:
        return 
    
    print(n)
    printNto1(n-1)


def print1toNbacktrack(i, n):
    if i<1:
        return 
    
    print1toNbacktrack(i-1,n)
    print(i)
    


n = int(input())
print1toN(1, n)
printNto1(n)
print("Backtrack")
print1toNbacktrack(n,n)