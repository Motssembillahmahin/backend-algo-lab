def main():
    divisor_count = [0] * 1001

    for i in range(1, 1001):
        for j in range(i, 1001, i):
            divisor_count[j] += 1

    numbers = []
    for num in range(1, 1001):
        numbers.append((num, divisor_count[num]))

    numbers.sort(key=lambda x: (x[1], -x[0]))

    t = int(input())
    for case in range(1, t + 1):
        n = int(input())
        result = numbers[n - 1][0]
        print(f"Case {case}: {result}")


main()
