def occurs(n,arr):
    for i in arr:
        if n==i:
            x=True
        else:
            x=False
    return(x)

print(occurs(2,[15, 38, 7, 23, 14]))