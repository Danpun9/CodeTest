def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        total = i
        x = i + 1
        while total < n:
            total += x
            x += 1
            
        if total == n:
            answer += 1
    
    return answer