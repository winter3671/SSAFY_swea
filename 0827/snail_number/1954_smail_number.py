import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    num = 1
    jump = 0

    if N == 1:
        arr[0][0] = 1
    else:
        while True:
            for i in range(N-1-(jump * 2)):
                arr[jump][i+jump] = num
                num += 1
            if num == N**2+1:
                break
            for i in range(N-1-(jump * 2)):
                arr[i+jump][N-1-jump] = num
                num += 1
            if num == N ** 2 + 1:
                break
            for i in range(N-1-(jump * 2)):
                arr[N-1-jump][N-1-i-jump] = num
                num += 1
            if num == N**2+1:
                break
            for i in range(N-1-(jump * 2)):
                arr[N-1-i-jump][jump] = num
                num += 1
            if num == N**2+1:
                break
            jump += 1

    print(f'#{tc} {" ".join(map(str, arr))}')
