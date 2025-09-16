from tail_recurse import tail_call_optimized


# Calc the LCM in O(n) algo - just find the first num that both divided by
def lcm(n1, n2, count=1):
    if count % n1 == 0 and count % n2 == 0:
        return 0
    return 1 + lcm(n1, n2, count + 1)


# Calc the LCM in O(log(n)) with the Euclidean algo (the recurse is in the inner func)
def lcm_tail(n1, n2):
    @tail_call_optimized
    def gcd_tail(n1, n2):
        if n2 == 0:
            return n1

        return gcd_tail(n2, n1 % n2)

    return n1 * n2 // gcd_tail(n1, n2)


def main():
    F1 = 55
    F2 = 89

    # print(lcm(F1, F2))
    print(lcm_tail(F1, F2))


if __name__ == '__main__':
    main()
