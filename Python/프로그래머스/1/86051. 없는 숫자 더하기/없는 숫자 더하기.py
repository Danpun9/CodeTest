def solution(numbers):
    answer = 9*10/2
    
    for num in numbers:
        answer -= num
    
    return answer