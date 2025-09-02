def get_penta_num(n):
    return n * (3 * n - 1) // 2


def pentaNumRange(n1, n2):
    return list(map(lambda n: get_penta_num(n), range(n1, n2)))  # go through each num in the range and apply the func
