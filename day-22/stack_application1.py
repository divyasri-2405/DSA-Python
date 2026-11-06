#check whether the expression is balanced or not

expression=input("Enter the expression: ")
stack=[]
for ch in expression:
    if ch=='(':
        stack.append(ch)
    elif ch==')':
        if len(stack)==0:
            print("Not balanced")
            break
        stack.pop()
else:
    if len(stack)==0:
        print("balanced")
    else:
        print("Not balanced")