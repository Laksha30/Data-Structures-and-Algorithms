'''
Given: An Array -> Tokens
Output: An integer obtained after evaluating the given 'tokes' array

Solution:
1. Initialise a stack 
2. Iterate through the given 'tokens' list
3. If the element is a digit or the 0th index of the element is minus (-) and the rest is a digit
    - then push the element into the list after type conversion from string to an integer value
4. Else, 
    - pop the top of the stack twice and save the elements in a variable
    - If the traversed element is 
        - '+' - then add both the popped values and push the result in the stack
        - '-' - then subtract both the popped values and push the result in the stack
        - '*' - then multiply both the popped values and push the result in the stack
        - '/' - then divide both the popped values and push the result in the stack
5. After the end of the traversal, return the popped value of the stack. 
'''

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isdigit() or (i[0] == '-' and i[1:].isdigit()):
                stack.append(int(i))
            else: 
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    stack.append(b + a)
                elif i == '-':
                    stack.append(b - a)
                elif i == '*':
                    stack.append(b * a)
                else:
                    stack.append(int(b / a))
                
        return stack.pop()
        