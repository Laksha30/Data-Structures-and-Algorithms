def palindrome(i, n, string):
    if i >= n/2:
        return True
    
    if string[i] != string[n-i-1]:
        return False
    
    return palindrome(i+1, n, string)
        
        


string = input()
print(palindrome(0, len(string), string))