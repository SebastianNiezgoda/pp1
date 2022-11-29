a1=[1,2,3,4,5,6,7,8]
a2=[2,3]

for i in a2:
    if i not in a1:
        status="nie nalezy"
        break
    else:
        status="nalezy"
        
print(status)
        