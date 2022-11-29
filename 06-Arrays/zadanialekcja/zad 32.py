def string(ar):
    x=f""
    for i in ar:
        x=x+f"{i},"
    return(x)

print(string([5,4,3,2,6,5]))