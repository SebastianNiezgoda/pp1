def minmax(arr):
    x=[]
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    x.append(arr[0])
    x.append(arr[len(arr)-1])
    return(x)

print(minmax([4,2,8,4,7,9,5]))
    