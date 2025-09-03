def mult_2(n):
    return n * 2


def pow_2(n):
    return n ** 2


def inverse(n):
    return 1 / n if n else None


def exec_ops(numbers, operations):
    # dict of each op name with the applying the op on the collection
    return dict(map(lambda op: (op.__name__, list(map(op, numbers))), operations))


def main():
    operations = [mult_2, pow_2, inverse]
    exec_ops(range(1000), operations)


if __name__ == "__main__":
    main()
