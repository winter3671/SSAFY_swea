'''
1. 문제 분석
매 초마다 command가 정수로 주어짐
1은 가속, 2는 감속, 0은 현재 속도 유지

2. 풀이방법 고안
속도는 m/s인데 매 초마다 주어지므로, 속도=거리라고 생각해도 무관
감속의 가속도가 현재 속도보다 더 크면 속도가 음수로 가는것이 아닌, 0으로 설정하는 것에 주의
'''
# import sys
# sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    V = 0   # 현재 속도
    move = 0    # 이동거리
    for _ in range(N):
        command = input()
        if command[0] == '0':    # 입력값이 0일 경우
            move += V
        else:   # 가속 또는 감속의 경우
            value = command[0]      # value = 1 또는 2
            A = int(command[-1])     # A는 가속도의 값
            if value == '1':
                V += A
                move += V
            else:
                if V - A < 0:
                    V = 0
                else:
                    V -= A
                move += V
    print(f'#{tc} {move}')