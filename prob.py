from cartprod import cartprod

def generate_combinations(n,k):
    result = []
    combinations = cartprod(n,k)
    for combination in combinations:
        if checkTpl(combination,k):
            result.append(combination)
    return result

def checkTpl(tup,k):
    if k==1:
        return True
    flag = True
    for i in range(k-1):
        if int(tup[i+1])==0 or int(tup[i])==0:
            flag = False
        elif int(tup[i+1])%int(tup[i])!=0:
            flag = False
    
    return flag