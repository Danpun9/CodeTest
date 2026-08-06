def solution(n, w, num):
    answer = 0

    # num 상자의 위치 구하기
    target_row = (num - 1) // w
    pos = (num - 1) % w

    if target_row % 2 == 0:
        target_col = pos
    else:
        target_col = w - 1 - pos

    # num이 있는 층부터 위층까지 확인
    row = target_row

    while True:
        # 현재 층의 target_col 위치에 있는 상자 번호 구하기
        if row % 2 == 0:
            box_num = row * w + target_col + 1
        else:
            box_num = row * w + (w - 1 - target_col) + 1

        # 존재하는 상자라면 꺼내기
        if box_num <= n:
            answer += 1

        row += 1

        # 다음 층의 시작 번호가 n보다 크면 종료
        if row * w + 1 > n:
            break

    return answer