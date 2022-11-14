arr=[1,2,3,4,5]

arr[0]=arr[0]-1
print(f"a.{arr}")


arr[4]=arr[4]+4
print(f"b.{arr}")

arr[2]=arr[2]*2
print(f"c.{arr}")

for x in range(len(arr)):
    arr[x]=arr[x]+3
print(f"d.{arr}")