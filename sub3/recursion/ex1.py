from tail_recurse import tail_call_optimized


def tuple_1000(t=1):
    if t == 1000:
        return (t,)
    return (t,) + tuple_1000(t + 1)


@tail_call_optimized
def tuple_1000_tail(t=()):
    if len(t) == 1000:
        return t
    return tuple_1000_tail(t+(len(t)+1,))


# print(tuple_1000_tail())
