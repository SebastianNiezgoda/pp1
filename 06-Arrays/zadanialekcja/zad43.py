def indenity_matrix(size):
    for rows in range(size):
        for col in range(size):
            if col==rows:
                print(1,end=" ")
                
            else:
                print(0,end=" ")
        print()
                


indenity_matrix(3)
print()
indenity_matrix(5)
print()
indenity_matrix(8)