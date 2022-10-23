count=0
number=1
sum=0


while number!=0:
    number=int(input("podaj liczbe"))
    sum=sum+number
    count=count+1
    if number==0:
        break
print(f"Podałeś {count-1} liczb, suma to {sum} a średnia to {sum/(count-1)}")