def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        total = 0
        x = i
        while total < n:
            total += x
            x += 1
            
        if total == n:
            answer += 1
    
    return answer