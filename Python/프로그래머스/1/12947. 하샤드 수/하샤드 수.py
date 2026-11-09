def solution(x):
    
    x_clone = x
    digit_sum = 0
    
    while x_clone > 0:
        digit_sum += x_clone % 10
        x_clone //= 10
        
    return x % digit_sum == 0