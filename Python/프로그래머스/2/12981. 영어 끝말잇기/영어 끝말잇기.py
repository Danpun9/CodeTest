def solution(n, words):
    used_words = set()
    
    for i, word in enumerate(words):
        player = (i % n) + 1
        turn = (i // n) + 1
        
        # 단어 시작-끝 비교
        if i > 0 and word[0] != words[i-1][-1]:
            return [player, turn]
        
        # 중복단어
        if word in used_words:
            return [player, turn]
          
        # 이상 없음
        used_words.add(word)
        
    return [0, 0]
