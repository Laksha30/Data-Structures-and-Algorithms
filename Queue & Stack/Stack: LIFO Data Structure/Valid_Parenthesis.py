'''
Given: String s
Output: Return True if the given string has valid parenthesis structure, else return False

Solution:
- Input the open parenthesis of any type in the stack as you traverse through the string 
- If you get a close parenthesis the, 
    - Check if the top of the stack is an open parenthesis of the same type, 
        - if True, then call the pop() method since we arrived at a pair 
        - else, return False, since we have an unmatched pair or no pair (i.e., stack is empty since a close parenthesis the first we receive)
    Traverse until we reach the end of the string 
- Check if the stack is empty
    - if True, then return True
    - Else, return False
'''


class Solution:
    def isValid(self, s: str) -> bool:
        self.stack = []
        for i in range(len(s)):
            if s[i] in "([{":
                #print(s[i])
                self.stack.append(s[i])
                #print(self.stack)
            
            else:
                #print(s[i])
                if not self.stack:
                    return False
                elif (s[i] == ')' and self.stack[len(self.stack)-1] == '(') or (s[i] == ']' and self.stack[len(self.stack)-1] == '[') or (s[i] == '}' and self.stack[len(self.stack)-1] == '{'):
                    #print("some")
                    self.stack.pop()
                else:
                    return False
        if not self.stack:
            return True
        return False
        