MAX = 1000 + 999 + 998 + 1

def solution(nums):
    
    prime_set = get_prime(MAX)
    
    res = 0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k] in prime_set:
                    res += 1
    

    return res

def get_prime(max):
    prime_list = [True] * (max+1)
    prime_list[0] = prime_list[1] = False
    
    for i in range(2, int(max**0.5) + 1):
        if prime_list[i]:
            for j in range(i*i, max+1, i):
                prime_list[j] = False
                
    return {i for i, prime in enumerate(prime_list) if prime}