arr=[1,2,3,4,5,6,7,8,9]
arr1=[]
for i in arr:
    if i%2==0:
        arr1.append(i)

for i in arr:
    if i%2==1:
        arr1.append(i)
    

print(arr1)
