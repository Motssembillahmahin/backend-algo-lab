"""problem link: https://lightoj.com/problem/double-ended-queue"""
from collections import deque

def main():
    t = int(input())

    for case_num in range(1, t + 1):
        n, m = map(int, input().split())
        dq = deque()

        print(f"Case {case_num}:")

        for _ in range(m):
            command = input().split()
            operation = command[0]

            if operation == "pushLeft":
                x = int(command[1])
                if len(dq) < n:
                    dq.appendleft(x)
                    print(f"Pushed in left: {x}")
                else:
                    print("The queue is full")

            elif operation == "pushRight":
                x = int(command[1])
                if len(dq) < n:
                    dq.append(x)
                    print(f"Pushed in right: {x}")
                else:
                    print("The queue is full")

            elif operation == "popLeft":
                if len(dq) > 0:
                    value = dq.popleft()
                    print(f"Popped from left: {value}")
                else:
                    print("The queue is empty")

            elif operation == "popRight":
                if len(dq) > 0:
                    value = dq.pop()
                    print(f"Popped from right: {value}")
                else:
                    print("The queue is empty")

