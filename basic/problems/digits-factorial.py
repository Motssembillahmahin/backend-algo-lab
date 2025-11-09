import math


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def get_total_integer(number, base):
    converted_number = ''
    while number > 0:
        converted_number += str(number % base)
        number = number // base
    return len(converted_number)

def digits_in_factorial(n, base):
    if n == 0 or n == 1:
        return 1
    log_sum = sum(math.log10(i) for i in range(2, n + 1))
    return int(log_sum / math.log10(base)) + 1


def main():
    t = int(input("Enter a number: "))
    for case_num in range(1, t + 1):
        number, base = map(int, input("Enter number and base: ").split())
        print(f"Case {case_num}: {digits_in_factorial(number, base)}")

main()

