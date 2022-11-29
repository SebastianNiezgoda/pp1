def create_2d_array(x,y):
    n=[]
    n2=[]
    for i in range(0,x):
        n.append(0)
    for i in range(0,y):
        n2.append(n)
    return(n2)




print(create_2d_array(2,4))