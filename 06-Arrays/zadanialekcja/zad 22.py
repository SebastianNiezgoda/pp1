a1=[4,36,12,28,9,44,5] 
a2=[5,1,36]
z=0
o=0
for i in range(len(a1)):
    for j in a2:
        if a1[z]==j:
            p=""
            break
        else:
            p=a1[z]
    print(p,end=" ")
    z=z+1
            

    
