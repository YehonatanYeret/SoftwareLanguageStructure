def is_prime(n):
    # go through all the number from 2 to sqrt of n and check if nis divided by 1 or more
    if n <= 0:
        return False
    return not any(filter(lambda x: n % x == 0, range(2, int(n ** 0.5) + 1)))


def twin_prime(n):
    if is_prime(n + 2):
        if is_prime(n - 2):
            return n - 2, n + 2  # for case there is 2 twins
        return n + 2
    if is_prime(n - 2):
        return n - 2
    return None


def dict_of_twins(n):
    return dict(map(lambda y: (y, twin_prime(y)), filter(lambda x: is_prime(x), range(n))))


def main():
    n = input("enter prime number:\n").strip()
    if not n.isdigit() or not is_prime(int(n)) or not twin_prime(int(n)):
        print("invalid input")
    else:
        print(twin_prime(int(n)))


if __name__ == "__main__":
    main()

