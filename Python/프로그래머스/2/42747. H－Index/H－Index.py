def solution(citations):
    citations.sort(reverse=True)
    
    for h, citation in enumerate(citations, start=1):
        if citation < h:
            return h - 1
        
    return len(citations)