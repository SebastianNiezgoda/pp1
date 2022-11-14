from re import I
from tkinter import X


arr1=[2,3,7,5,4]

a=arr1
print(f'a.{a}')

b=len(arr1)
print(f"b.{b}")

c=arr1[0]
print(f"c.{c}")

d=arr1[1]
print(f"d.{d}")

e=arr1[4]
print(f"e.{e}")

f=arr1[3]
print(f"f.{f}")

g=arr1[0]+arr1[4]
print(f"g.{g}")

h=arr1[2]
print(f"h.{h}")

for x in arr1[0:5]:
    print(x, end=" ")

print("")

for x in arr1[0:3]:
    print(x, end=" ")
    