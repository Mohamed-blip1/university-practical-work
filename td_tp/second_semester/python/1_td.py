#!/usr/bin/env python3

import math


# Ex1
def somme(n: int, p: int) -> int:
    result = int(0)

    for k in range(0, n):  # Using i+1
        result += (k + 1) ** p

    return result


# print(somme(5, 10))  # Should give 10874275


# Just a helper
def my_factorial(x: int) -> int:
    result = int(1)

    for i in range(x):
        result *= i + 1

    return result


# print(my_factorial(4)) # Should give 24


# Ex2
# a)
def exp1(x: int, n: int) -> bool:
    if x == 0:
        return False

    result = int(0)

    for i in range(n + 1):
        result += (x**i) / my_factorial(i)

    print(result)

    return True


# exp1(2, 3)  # Should give ≈ 6.333333333


# b)
def exp2(x: float) -> bool:
    if x == 0:
        return False

    epsilon = 10**-8
    result = int(0)
    i = int(0)

    while True:
        term = (x**i) / my_factorial(i)
        result += term

        if term < 10 ** (-8):
            break

        i += 1

    print(result)

    return True


# exp2(2.2)  # Should give ≈ 9.025013499176875


# Ex3
def est_parfait(n: int) -> bool:
    end = (n / 2) + 1
    acc = int(0)

    for i in range(1, int(end)):
        if n % i == 0:
            acc += i
        if acc == n:
            return True
    return False


# print(est_parfait(6))  # Should give True

# Ex4 TODO


# Ex5
def crible_eratosthene(n: int) -> list[int]:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(i + i, n + 1, i):
                is_prime[j] = False
    return [num for num, prime in enumerate(is_prime) if prime]


prime_numbers_to_compare_with_list = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
]

# print(crible_eratosthene(100))

# if prime_numbers_to_compare_with_list == crible_eratosthene(100):  # Should give True
#     print(True)


# Ex6


def my_function(x: float) -> float:
    return x**2 - 2


def my_zero(a, b, eps) -> float:
    if not my_function(a) * my_function(b) < 0:
        return None

    while (b - a) > eps:
        m = (a + b) / 2

        if my_function(m) * my_function(a) < 0:
            b = m
        else:
            a = m

    return m


# print(my_zero(1, 2, 10 ** (-6)))

# Ex7


def pgcd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a

    if a % b == 0:
        return b
    return pgcd(a, a % b)


print(pgcd(10, 12))

# Ex8


def somme_suite_arith(a: float, r: float, n: float) -> float:
    if n <= 0:
        return 0
    return a + somme_suite_arith(a + r, r, n - 1)


# print(somme_suite_arith(2, 3, 4))

# Ex9


def somme_suite_geo(a: float, r: float, n: float) -> float:
    if n <= 0:
        return 0
    return a + somme_suite_geo(a * r, r, n - 1)


# print(somme_suite_geo(1, 0.5, 10))

# Ex10 TODO

# Ex11


def febonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return febonacci(n - 1) + febonacci(n - 2)


# print(febonacci(10)) # Should give 55

# Ex12


def ackermann(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))


# print(ackermann(3, 2)) # Should give 29


def ex_13():
    notes = {}

    print("Enter students names or enter 'end' to stop:")
    while True:
        student_name = str(input("student name [or 'end']: "))

        if student_name == "end":
            break

        while True:
            try:
                note = float(input(f"Enter {student_name} note: "))
                break
            except ValueError:
                print("Error: Please Enter a valid number!")

        notes[student_name] = note

    print("\n--- Summary ---")
    for student, note in notes.items():
        print(f"{student} : {note}")


# ex_13()


def ex_14(user_dict: dict) -> tuple:
    """count, sum, max, min, avg"""
    vals = user_dict.values()

    if not vals:
        return (0, 0, 0, 0, 0)

    vals_num = len(vals)
    vals_sum = sum(vals)

    return (vals_num, vals_sum, max(vals), min(vals), vals_sum / vals_num)


# print(ex_14({"A": 20, "B": 20, "C": 20}))

# Ex: 15

minusc = set(chr(x) for x in range(ord("a"), ord("z") + 1))


# print(type(set("abc") & set("a")))


def n_oc_minusc(s: str) -> int:
    temp = set(s) & minusc
    return len(temp)


# print(n_oc_minusc("mOHAMEd"))


def ens_minusc(s: str) -> int:
    return set(s) & minusc


# print(ens_minusc("moHAMED"))


def nb_minusc(s: str) -> int:
    return len(ens_minusc(s))


# Ex: 16


def tltl(l_etud: list) -> list:
    return sorted(l_etud, key=lambda t: t[1])


# print(tltl([("Ali", 14), ("Sara", 18), ("Youssef", 12)]))


# Ex: 17


def fnpl(nums: list) -> list:
    return list(filter(lambda n: n % 2 == 0, nums))


# print(fnpl([1, 2, 3, 4, 5, 76, 8, 5, 3]))


# Ex: 18


def cal(nums: list) -> list:
    return list(map(lambda n: n**2, nums))


# nums = [1, 2, 3, 4, 5, 76, 8, 5, 3]

# print(cal(nums))

# Ex: 19


def mpl(s: str) -> list:
    return sorted(s, key=lambda x: len(x))


# print(mpl(["abc", "a", "ab"]))


# Ex: 20


def meal(d: dict) -> str:
    return max(d, key=lambda x: d[x])


d = {"a": 10, "b": 20, "c": 15}

# print(meal(d))
