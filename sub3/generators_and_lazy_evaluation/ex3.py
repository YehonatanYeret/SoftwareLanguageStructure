import math


def taylor(x):
    s = 1  # the sum till now
    n = 1
    while True:
        yield s
        s += (x ** n) / math.factorial(n)  # The taylor formula
        n += 1  # n increase by 1 for the next num to sum


def main():
    e = taylor(2)
    for i in range(30):
        print(next(e))


if __name__ == '__main__':
    main()
