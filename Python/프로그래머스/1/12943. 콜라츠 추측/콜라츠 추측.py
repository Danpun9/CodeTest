def solution(num):
    cnt = 0
    
    while True:
        if cnt >= 500:
            cnt = -1
            break
            
        if num == 1:
            break
        
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
            
        cnt += 1
        
    return cnt