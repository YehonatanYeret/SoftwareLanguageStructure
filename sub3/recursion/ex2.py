from ex1 import tuple_1000_tail
from tail_recurse import tail_call_optimized


def rec_len(l):
    if not l:
        return 0
    return l[0] + rec_len(l[1:])


@tail_call_optimized
def rec_len_tail(l, n=0):
    if not l:
        return n
    return rec_len_tail(l[1:], n + l[0])


t = tuple_1000_tail()
print(rec_len_tail(t))
