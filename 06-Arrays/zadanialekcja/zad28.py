arr=[1,0,9,4,]

for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)
n=len(arr)//2
print(arr[n])