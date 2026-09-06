def solution(sequence, k):
    left = 0
    curr_sum = 0
    min_length = float('inf')
    best_range = [0, 0]
    
    for right in range(len(sequence)):
        curr_sum += sequence[right]

        while curr_sum > k:
            curr_sum -= sequence[left]
            left += 1

        if curr_sum == k:
            current_length = right - left
            if current_length < min_length:
                min_length = current_length
                best_range = [left, right]

    return best_range