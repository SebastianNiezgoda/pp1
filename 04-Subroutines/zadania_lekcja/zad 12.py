def sum(n):
    sum=0
    x=0
    for i in range(0,n+1):
        x=x+1
        sum=sum+x
    return(sum)

print(sum(10))