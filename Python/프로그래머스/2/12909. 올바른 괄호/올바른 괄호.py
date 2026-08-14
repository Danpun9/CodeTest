def solution(s):
    answer = True
    
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            if cnt != 0:
                cnt -= 1
            else:
                return False
            
    if cnt != 0:
        return False

    return True