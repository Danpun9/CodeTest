def solution(participant, completion):
    
    end_runner = dict()
    for i in completion:
        if i not in end_runner:
            end_runner[i] = 1
        else:
            end_runner[i] += 1
            
    for i in participant:
        if i not in end_runner or i in end_runner and end_runner[i] == 0:
            return i
        else:
            end_runner[i] -= 1