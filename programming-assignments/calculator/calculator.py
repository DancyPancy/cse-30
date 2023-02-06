# Code by: Jack Wong
# Date: Fri Nov 18 2022
# About: client code - takes arithmetic expressions and evaluates them

from stack import Stack
from tree import ExpTree

def pemdas(op):
    precedence = {'^':1, '*':2, '/':2, '+':3, '-':3}

    if op in precedence.keys():
        return precedence[op]
    else:
        raise ValueError('ValueError: Invalid operator type') 

def infix_to_postfix(infix):
    ops = Stack()
    postfix = ''
    operand = ''
    for i in range(len(infix)):
        char = infix[i]
        
        if char in '()^*/+-':
            if operand != '':
                postfix += ' ' + operand
                operand = ''
            if char == '(': 
                ops.push(char)
            elif char == ')':
                while ops.peek() != '(':
                    postfix += ' ' + ops.pop()
                ops.pop()
            elif ops.isEmpty() or ops.peek() == '(' or (pemdas(ops.peek()) > pemdas(char)):
                ops.push(char)
            else:
                postfix += ' ' + ops.pop()
                ops.push(char)

        else:
            operand += char
    
    postfix += ' ' + operand
    while not ops.isEmpty():
        postfix += ' ' + ops.pop()
            
    return postfix.lstrip()

def calculate(infix):
    postfix = infix_to_postfix(infix)
    tree = ExpTree.make_tree(postfix.split())
    return ExpTree.evaluate(tree)

# a driver to test calculate module
if __name__ == '__main__':

    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0

    print('Welcome to Calculator Program!')
    while True:
        expression = input('Please enter your expression here. To quit enter \'quit\' or \'q\':\n').replace(' ', '').lower()
        if expression == 'quit' or expression == 'q':
            print('Goodbye!')
            break

        print(calculate(expression))
