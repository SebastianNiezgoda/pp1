n1=0
n2=1
nterms=50
count=0
print("Fibonacci sequence:")
for i in range(0,51):
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1