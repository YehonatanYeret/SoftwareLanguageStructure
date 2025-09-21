import sys
import time


def gen_0_to_10000():
    return [i for i in range(10001)]


def gen_0_to_10000_lazy():
    return (i for i in range(10001))


def first_5000():
    return gen_0_to_10000()[5000:]


# I used yield so each time we get the next number till 5000 - but still in a lazy way
def first_5000_lazy():
    i = 0
    g = gen_0_to_10000_lazy()
    while i < 5000:
        yield next(g)


def main():
    start = time.time()
    g1 = gen_0_to_10000()
    end = time.time()
    print(f"gen in normal way took: {end - start} sec' and takes {sys.getsizeof(g1)} bytes ")

    start = time.time()
    g2 = gen_0_to_10000_lazy()
    end = time.time()
    print(f"gen in lazy way took: {end - start} sec' and takes {sys.getsizeof(g2)} bytes")

    print()

    # The fist 5000 items
    start = time.time()
    s1 = first_5000()
    end = time.time()
    print(f"first 5000 items in normal way took: {end - start} sec' and takes {sys.getsizeof(s1)} bytes ")

    start = time.time()
    s2 = first_5000_lazy()
    end = time.time()
    print(f"first 5000 in lazy way took: {end - start} sec' and takes {sys.getsizeof(s2)} bytes")

    # Ensure that we don't change the type when slicing the list/generator
    assert type(s1) is type(g1)
    assert type(s2) is type(g2)


if __name__ == '__main__':
    main()
