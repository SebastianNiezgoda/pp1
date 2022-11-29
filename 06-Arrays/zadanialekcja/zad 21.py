def compare(arr1,arr2):
    if len(arr1)==len(arr2):
        x=0
        for i in range(len(arr1)):
            if arr1[x]==arr2[x]:
                wynik=True
            else:
                wynik=False
                break
    else:
        wynik=False
    
    return(wynik)

print(compare([3,2,1],[3,2]))