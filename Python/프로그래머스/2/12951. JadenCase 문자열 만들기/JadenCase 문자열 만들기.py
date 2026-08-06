def solution(s):
    words = s.split(' ')
    
    for i in range(len(words)):
        words[i] = words[i][:1].upper() + words[i][1:].lower()

    return ' '.join(words)