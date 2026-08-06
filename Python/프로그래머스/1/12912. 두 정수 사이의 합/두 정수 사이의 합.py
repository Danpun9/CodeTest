def solution(a, b):
    if a == b:
        return a
    
    a, b = min(a,b), max(a,b)
    
    return (b-a+1)*(a+b)/2