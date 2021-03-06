import sys
from collections import deque


def bfs(a, b, result_a, result_b):
    plus_a = [-1, -2, -2, -1, 1, 2,  2,  1]  # -1 = 상, 1 = 하
    plus_b = [-2, -1,  1,  2, 2, 1, -1, -2]  # -1 = 좌, 1 = 우
    queue = deque()
    queue.append((a, b))

    while queue:
        queue_a, queue_b = queue.popleft()
        # graph[queue_a][queue_b] = 0

        if queue_a == result_a and queue_b == result_b:
            return graph[queue_a][queue_b]

        for i in range(8):
            moved_a = queue_a + plus_a[i]
            moved_b = queue_b + plus_b[i]

            if 0 <= moved_a < I and 0 <= moved_b < I:
                if graph[moved_a][moved_b] == 0:
                    graph[moved_a][moved_b] = graph[queue_a][queue_b] + 1
                    queue.append((moved_a, moved_b))

                continue


T = int(sys.stdin.readline())

for _ in range(T):
    I = int(sys.stdin.readline())
    graph = [I * [0] for _ in range(I)]

    b1, a1 = map(int, sys.stdin.readline().split())
    b2, a2 = map(int, sys.stdin.readline().split())

    print(bfs(a1, b1, a2, b2))