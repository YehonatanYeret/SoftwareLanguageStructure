def is_prime(n):
    # go through all the number from 2 to sqrt of n and check if nis divided by 1 or more
    if n <= 0:
        return False
    return not any(filter(lambda x: n % x == 0, range(2, int(n ** 0.5) + 1)))


def twin_prime(n):
    if not n.isdigit() or not is_prime(int(n)):
        return "invalid input"
    num = int(n)
    if is_prime(num + 2):  # first check the follower number
        return num + 2
    if is_prime(num - 2):
        return num - 2
    return "invalid input"


def dict_of_twins(n):
    return dict(map(lambda y: (y, twin_prime(y)), filter(lambda x: is_prime(x), range(n))))


def main():
    n = input("enter prime number:\n").strip()
    print(twin_prime(n))


if __name__ == "__main__":
    main()
