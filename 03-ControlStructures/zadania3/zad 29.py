#29.	Write a program that calculates the sum and arithmetic mean of numbers entered from the keyboard. 
# Entering 0 ends entering numbers. 
count=0
sum=0
number=1

while number !=0:
    number=int(input("podaj liczbe"))
    sum=sum+number
    count +=1
    if number==0:
        break

print(f'podałeś {count} liczb, suma to {sum}, a średnia to {sum/count}')

