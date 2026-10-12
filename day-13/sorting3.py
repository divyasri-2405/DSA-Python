'''#flip sorting/pancake sort-TC-O(N^2)
def flip(arr,k):
    i=0
    j=k-1
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
def pancakesort(arr):
    for size in range(len(arr),1,-1):
        max_index=0
        for i in range(1,size):
            if arr[i]>arr[max_index]:
                max_index=i
        flip(arr,max_index+1)
        flip(arr,size)
    return arr
arr=list(map(int,input("Enter n elements : ").split()))
print('Sorted array: ',pancakesort(arr))'''

#quick sort-TC-N(log(n)) or O(n)
def part(arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quicksort(arr,low,high):
    if low<high:
        p=part(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)
arr=list(map(int,input("Enter n elements: ").split()))
quicksort(arr,0,len(arr)-1)
print("sorted array: ",arr)