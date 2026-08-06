def solution(s):
    sets = s[2:-2].split("},{")

    sets.sort(key=len)
    
    answer = []
    seen = set()
    
    for s_set in sets:

        nums = list(map(int, s_set.split(",")))
        for num in nums:
            if num not in seen:
                seen.add(num)
                answer.append(num)
                
    return answer