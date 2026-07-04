def solution(A,B):
    A.sort()
    B.sort()
    
    l = len(A)
    answer = 0
    for i in range(l):
        answer += A[i] * B[l-i-1]

    return answer