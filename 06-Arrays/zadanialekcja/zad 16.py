ar=[15, 8, 31, 47, 2, 19]
print("existed array:",end=" ")
for i in ar:
    print(i,end=" ")
print("\nnew array:",end=" ")
z=len(ar)-1
for i in range(len(ar)):
    print(ar[z],end=" ")
    z=z-1
