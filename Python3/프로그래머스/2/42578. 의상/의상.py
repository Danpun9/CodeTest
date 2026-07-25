def solution(clothes):
    type_cnt = {}
    for _, c_t in clothes:
        type_cnt[c_t] = type_cnt.get(c_t, 0) + 1
    
    answer = 1
    for cnt in type_cnt.values():
        answer *= (cnt + 1)
    
    return answer - 1