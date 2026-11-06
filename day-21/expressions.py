#expressions-stack
#prefix
#infix
#postfix

'''#infix to prefix operation of an operation

def precedence(op):
    if op=='+' or op=='-':
        return 1
    if op=='*' or op=='/':
        return 2
    if op=='^':
        return 3
    return 0
expression=input("Enter a infix expression: ")
expression=expression[::-1]
stack=[]
output=[]
for ch in expression:
    if ch.isalnum():
        output.append(ch)
    else:
        while stack and precedence(stack[-1])>=precedence(ch):
            output.append(stack.pop())
        stack.append(ch)
while stack:
    output.append(stack.pop())
prefix=''.join(output[::-1])
print(prefix)

#infix to postfix operation of an operation

def precedence(op):
    if op=='+' or op=='-':
        return 1
    if op=='*' or op=='/':
        return 2
    if op=='^':
        return 3
    return 0
expression=input("Enter a infix expression: ")
stack=[]
output=[]
for ch in expression:
    if ch.isalnum():
        output.append(ch)
    else:
        while stack and precedence(stack[-1])>=precedence(ch):
            output.append(stack.pop())
        stack.append(ch)
while stack:
    output.append(stack.pop())
postfix=''.join(output)
print(postfix)'''

#prefix to postfix

expression=input("Enter expression: ")
stack=[]
for ch in expression[::-1]:
    if ch.isalnum():
        stack.append(ch)
    else:
        a=stack.pop()
        b=stack.pop()
        stack.append(a+b+ch)
print(stack[-1])