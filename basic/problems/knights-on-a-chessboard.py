"""problem link: https://lightoj.com/problem/knights-on-chessboard"""


def knights_on_chessboard():
    t = int(input())
    for i in range(1, t + 1):
        m, n = map(int, input().split())

        if m == 1 or n == 1:
            result = max(m, n)
        elif m == 2 or n == 2:
            larger = max(m, n)
            c = (larger // 4) * 4
            remainder = larger % 4

            if remainder == 1:
                result = c + 2
            elif remainder > 1:
                result = c + 4
            else:
                result = c
        else:
            result = (m * n + 1) // 2

        print(f"Case {i}: {result}")


knights_on_chessboard()
