def solution(n):
    n_bin = bin(n)
    
    answer = n + 1
    
    while True:
        answer_bin = bin(answer)
        if answer_bin.count('1') == n_bin.count('1'):
            return answer
        
        answer += 1