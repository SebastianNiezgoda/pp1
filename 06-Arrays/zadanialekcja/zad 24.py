arr=[2, 3, 2 ,5 ,8 ,1, 9, 8]
arr1=[]


for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if arr[i]==arr[j]:
            break
        else:
            arr1.append(arr[i])
    
        



print(arr1)