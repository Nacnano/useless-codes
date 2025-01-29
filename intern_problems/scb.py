# Simply count all the possible ways to get the sum of t with n dice and k faces
# Easy
def func(n, k, t):
    # dp[dice][total]
    dp = [ [0] * 1000 for i in range(n+1)]
    dp[0][0] = 1;
    
    for dice in range(1, n+1):
        for face in range(1, k+1):
            for total in range(0, t+1):
                dp[dice][total+face] += dp[dice-1][total]

    for i in range(0, dice+1):
        for j in range(0 ,k+2):
            print(dp[i][j], end=" ")
        print("\n")
        
        
    return dp[n][t]

print(func(4, 10, 7))



