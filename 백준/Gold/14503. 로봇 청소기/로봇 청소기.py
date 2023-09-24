def clean_room(N, M, r, c, d, room):
    # 방향 설정: 북, 동, 남, 서 (반시계 방향)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    def turn_left(d):
        return (d - 1) % 4

    count = 0  # 청소한 칸 수
    while True:
        # 1. 현재 위치 청소
        if room[r][c] == 0:
            room[r][c] = 2  # 청소 완료 표시
            count += 1

        # 2. 왼쪽 방향으로 회전하면서 탐색
        no_clean = True
        for _ in range(4):
            # 왼쪽 방향으로 회전
            d = turn_left(d)
            nr, nc = r + dr[d], c + dc[d]

            # 아직 청소하지 않은 곳이라면 이동하고 1번부터 반복
            if room[nr][nc] == 0:
                r, c = nr, nc
                no_clean = False
                break

        # 3. 네 방향 모두 청소되었거나 벽인 경우 후진
        if no_clean:
            nr, nc = r - dr[d], c - dc[d]
            if room[nr][nc] == 1:  # 후진도 불가능하면 종료
                break
            r, c = nr, nc

    return count

# 입력 받기
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 로봇 청소기 작동 및 결과 출력
result = clean_room(N, M, r, c, d, room)
print(result)
