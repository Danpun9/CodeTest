def solution(elements):
    n = len(elements)
    
    sum_set = set()
    
    elements = elements * 2
    
    for i in range(n):
        for j in range(n):
            sum_set.add(sum(elements[j:j+i+1]))
    
    return len(sum_set)