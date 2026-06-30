def solution(strs, t):
    n = len(t)
    strs_set = set(strs)
    
    dp = [float('inf')] * (n+1)
    dp[0] = 0
    
    for i in range(1, n+1):
        for l in range(1, min(i,5)+1):
            if t[i-l:i] in strs_set:
                dp[i] = min(dp[i], dp[i-l]+1)
        
    if dp[-1] == float('inf'):
        return -1
    else:
        return dp[-1]