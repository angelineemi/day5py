def list1():
    lis=[]
    for i in range(1,20+1):
        lis.append(i**2)
    return(lis[5:])
print(list1())
