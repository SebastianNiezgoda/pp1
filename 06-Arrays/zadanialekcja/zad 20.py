def star(n):
    x=""
    for i in range(0,n):
        x=x+"*"
    return(x)

ar=[12, 6, 4, 9, 10]
z=0
for i in range(len(ar)):
    print(f"{ar[z]}={star(ar[z])}")
    z=z+1


