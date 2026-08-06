def solution(n):
    MOD = 1234567
    
    if n == 1:
        return 1 % MOD
    elif n == 2:
        return 2 % MOD
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % MOD
    
    return dp[n]
