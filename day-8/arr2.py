'''#count the occurences in an array
arr=input("Enter fruits: ").split()
key=input("Enter a fruit: ")
count=0
for i in range(len(arr)):
    if arr[i]==key:
        count+=1
print(count)

#reverse a string
word=input("enter a fruit: ")
reverse=''
for i in word:
    reverse=i+reverse
print(reverse)

#reverse word return the count
#count the occurences in word
word=input("enter a word: ")
char=input("enter a character: ")
c=0
for i in word:
    if i==char:
        c+=1
print(c)'''

#find the largest word
words=input("enter names: ").split()
largest=words[0]
for word in words:
    if len(word)>len(largest):
        largest=word
print('Largest: ',largest)
