def solution(s):
    
    zero_del = 0
    cnt = 0
    
    while s != "1":
        temp_s = []
        for i in range(len(s)):
            if s[i] == '0':
                zero_del += 1
            else:
                temp_s.append('1')
                
        s = bin(len(temp_s))[2:]
        cnt += 1
    
    return [cnt, zero_del]
                
                
        