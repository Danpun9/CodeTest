fibo_map = {}
div = 1234567

def solution(n):
    return fibo(n)

def fibo(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n in fibo_map:
        return fibo_map[n]
    
    if n%2 == 0:
        m = n//2
        temp1 = fibo(m-1)
        temp2 = fibo(m)
        
        fibo_map[n] = ((2*temp1+temp2)) * temp2 % div
        return fibo_map[n]
    else:
        m = (n+1)/2
        temp1 = fibo(m)
        temp2 = fibo(m-1)
        
        fibo_map[n] = (temp1*temp1+temp2*temp2) % div
        return fibo_map[n]