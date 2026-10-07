#linear data structures
'''Arrays
1.create and display
2.insert
3.delete
4.append
5.remove'''

#create and print an array
'''arr=list(map(int,input("Enter elements: ").split()))
print(arr)

arr=list(map(int,input().split()))
print(*arr) #used to unpack the data or remove the list structure

#access an element with index value
arr=list(map(int,input('Enter elements: ').split()))
index=int(input("Enter your index value: "))
print("Element: ",arr[index])
print('Element: ',arr[index]+55)
print(*arr)

#create and insert an element print an array at desired location or index and last position
arr=list(map(int,input("Enter elements: ").split()))
print(*arr)
index=int(input("Enter your index value: "))
value=int(input("Enter the value to be placed at index: "))
arr.insert(index,value) #inserted at desired location or index
print(*arr)
arr.append(value) #insert the value at last position
print(*arr)

#create and delete an element at index or desired location and last-print an array
arr=list(map(int,input("Enter elements: ").split()))
print(*arr)
value=int(input("Enter the value to be deleted: "))
arr.remove(value)
print(*arr)
index=int(input("Enter index: "))
arr.pop(index)
print(*arr)
arr.pop()
print(*arr)

#search an element and return an index value
arr=list(map(int,input("Enter elements: ").split()))
print(*arr)
value=int(input("Enter the value to be searched: "))
found=False
for i in range(len(arr)):
    if arr[i]==value:
        found=True
        print(value,"found at index: ",i)
        break
if found==False:
    print("Element not in array...........!")

#find the minimum value and print the minimum value
arr=list(map(int,input("Enter elements: ").split()))
min=arr[0]
for i in range(1,len(arr)):
    if arr[i]<min:
        min=arr[i]
print(min)

#swapping and sorted TC_O(n^2) #reverse bubble sort
arr=list(map(int,input("Enter elements: ").split()))
print(*arr)
n=len(arr)
for i in range(n):
      for j in range(0,n-i-1): 
         if arr[j]>arr[j+1]:
             arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr)'''

arr=list(map(int,input("Enter elements: ").split()))
print(*arr)
n=len(arr)
for i in range(n):
      for j in range(i+1,n): 
         if arr[i]>arr[j]:
             arr[i],arr[j]=arr[j],arr[i]
print(*arr)