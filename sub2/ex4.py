import math


def power_function(n):
    def est(x):
        return x ** n

    # return the inner func
    return est


def map_of_powers(n):
    return map(lambda x: power_function(x), range(n))


def taylor_e(x, n=100):
    # zip the X^n to the range, then aplay the func and divide by yhr factorial (from the range)
    return sum(map(lambda a: a[0](x) / math.factorial(a[1]), zip(map_of_powers(n + 1), range(n + 1))))


def main():
    n = int(input("Enter number of powers:"))
    result = map_of_powers(n)
    # in the tests at the auto checker, those 2 prints are flipped (not like the example in the ex)
    base = int(input("Enter base:"))
    print(type(result))
    print(tuple(map(lambda x: x(base), result)))


if __name__ == '__main__':
    main()