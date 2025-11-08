"""problem link: https://lightoj.com/problem/secret-origins"""


# ----------------------------------brute force------------------------------------------------------
def find_binary(m) -> str:
    """Find binary number"""
    binary = ""
    while m > 0:
        binary += str(m % 2)
        m = m // 2
    return binary[::-1]


def count_ones(n):
    """Count the number of 1s in binary representation"""
    return bin(n).count("1")


def main():
    t = int(input())
    for case_num in range(1, t + 1):
        n = int(input())
        target_ones = count_ones(n)
        i = n + 1
        while True:
            if count_ones(i) == target_ones:
                print(f"Case {case_num}: {i}")
                break
            i += 1


main()


# ----------------------------------bit manipulation------------------------------------------------------
def next_same_bits(n):
    rightOne = n & -n
    nextHigher = n + rightOne
    rightOnesPattern = n ^ nextHigher
    rightOnesPattern = (rightOnesPattern // rightOne) >> 2
    return nextHigher | rightOnesPattern


def main():
    t = int(input())
    for case_num in range(1, t + 1):
        n = int(input())
        result = next_same_bits(n)
        print(f"Case {case_num}: {result}")


main()
