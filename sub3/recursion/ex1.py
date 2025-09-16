from tail_recurse import tail_call_optimized


# Each time add tuple with the next num
def tuple_1000(t=1):
    if t == 1000:
        return (t,)
    return (t,) + tuple_1000(t + 1)


# Add the tuple in the parameters of the function
@tail_call_optimized
def tuple_1000_tail(t=()):
    if len(t) == 1000:
        return t
    return tuple_1000_tail(t + (len(t) + 1,))


def main():
    # print(tuple_1000())
    print(tuple_1000_tail())


if __name__ == '__main__':
    main()
