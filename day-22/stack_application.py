#web browser history using stacks and files

stack=[]
while True:
    print("\n1. Visit Website")
    print("2. Back")
    print("3. Forward")
    choice=int(input("Enter your choice: "))
    if choice==1:
        website=input("Enter website: ")
        stack.append(website)
        with open("history.txt","a") as file:
           file.write(website+'\n')
        print("Visited: ",website)
    elif choice==2:
        if len(stack)==0:
            print("No previous pages...")
        else:
            stack.pop()
            if len(stack)==0:
                print("No previous pages...")
            else:
                print("Back to",stack[-1])
    elif choice==3:
        print("Browser History")
        if len(stack)==0:
            print("History empty...")
        else:
            for website in stack:
                print(website)
    elif choice==4:
        print("Exit")
    else:
        print("Invalid input...")