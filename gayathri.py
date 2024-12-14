MOD = 10000  

def count_valid_arrays(N, K):
    
    dp = []  
    for i in range(K + 1):  
        dp.append([0] * (N + 1))  
    for x in range(1, N + 1):
        dp[1][x] = 1  
    for i in range(2, K + 1):  
        for x in range(1, N + 1):  
            for y in range(1, N + 1):  
                if x % y == 0:  
                    dp[i][x] += dp[i - 1][y]  
                    dp[i][x] %= MOD  

    
    result = 0
    for x in range(1, N + 1):  # Loop over all possible last elements of arrays of length K
        result += dp[K][x] 
        result %= MOD  
    print(dp)
    return result  
N = int(input("Enter the maximum number (N): "))  
K = int(input("Enter the length of the array (K): "))  
print(count_valid_arrays(N, K))