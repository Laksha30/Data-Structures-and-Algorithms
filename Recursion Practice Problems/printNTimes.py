#print a name N times using recursion

def name(n):
    if n == 0:
        return 
    print("Hello")
    name(n-1)


n =  int(input())
name(n)