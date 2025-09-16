from sub1.ex4 import is_prime


def prime_gen():
    n = 1  # Assume that 1 is prime
    while True:
        # I used the is_prime() func from sub1.ex4
        if is_prime(n):
            yield n
        n += 1


def main():
    p = prime_gen()
    for i in range(100):
        print(next(p))


if __name__ == '__main__':
    main()
