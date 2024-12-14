
def cartprod(n,k):
    initialval = 0
    for kf in range(k-1):
        initialval+=1
        initialval*=10
    initialval+=1
    print(initialval)

    finalval = 10**(n+1) - 1
    arrayy = []
    for i in range(initialval,finalval+1):
        itemm = list(str(i))
        flag = True
        for j in itemm:
            if int(j)>n:
                flag = False
                break
        if flag:
            arrayy.append(tuple(itemm))

    return arrayy
