def solution(s):
    answer = True
    
    p_cnt = 0
    y_cnt = 0
    
    for i in range(len(s)):
        if s[i] == 'P' or s[i] == 'p':
            p_cnt += 1
        elif s[i] == 'Y' or s[i] == 'y':
            y_cnt += 1

    return p_cnt == y_cnt