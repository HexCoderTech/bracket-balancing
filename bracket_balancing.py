'''
“Check if a given mathematical expression has balanced brackets.”

Valid brackets: (), {}, []

Example: 
(1+2) * 3 + ( x - {y +3}) —> okay

(1+2) * 3 + ( x - {y +3} —> not okay 

(1+ {x-3)} —> not okay 

[{1+x-[y-3]}] —> okay 

1+2 —> okay

{[]({})(())}[] —> okay

'''

def bracket_balancing(expression):
    '''Check if a given mathematical expression has balanced brackets.'''
    brackets = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in expression:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    return not stack


if __name__ == '__main__':
    expression = input('Enter an expression: ')
    if expression.strip() == '':
        print('No expression entered.')
 
    elif bracket_balancing(expression):
        print('Balanced')
    else:
        print('Not balanced')
