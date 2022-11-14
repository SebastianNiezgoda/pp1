arr=[-15,8,-31,47,-2,19]
y=arr[0]
z=arr[0]
for x in range(len(arr)):
    if arr[x]>y:
        y=arr[x]
for x in range(len(arr)):
    
    if arr[x]<z:
        z=arr[x]

print(f"max= {y}, min= {z}")

