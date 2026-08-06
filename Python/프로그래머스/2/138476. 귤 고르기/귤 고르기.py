from collections import Counter

def solution(k, tangerine):
    counter = Counter(tangerine)
    
    counts = sorted(counter.values(), reverse=True)
    
    types = 0
    
    for count in counts:
        k -= count
        types += 1
        if k <= 0:
            break
            
    return types