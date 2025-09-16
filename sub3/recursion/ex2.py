from ex1 import tuple_1000_tail
from tail_recurse import tail_call_optimized


# Sum the first element with the entire list
def rec_sum(l):
    if not l:
        return 0
    return l[0] + rec_sum(l[1:])


# Send the sum in the parameters to the function
@tail_call_optimized
def rec_sum_tail(l, n=0):
    if not l:
        return n
    return rec_sum_tail(l[1:], n + l[0])


def main():
    t = tuple_1000_tail()

    # print(rec_sum(t))
    print(rec_sum_tail(t))


if __name__ == '__main__':
    main()
