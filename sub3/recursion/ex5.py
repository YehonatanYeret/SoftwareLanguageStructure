from tail_recurse import tail_call_optimized


def sortedzip(l):
    @tail_call_optimized
    def sortedlists(l):
        if len(l) == 1:
            return sorted(l)
        return [sorted(l[0])] + sortedlists(l[1:])

    return list(zip(*sortedlists(l)))


def sortedzip_tail(l):
    def sortedlists(l, sl):
        if len(l) == 1:
            return sl + sorted(l)
        return sortedlists(l[1:], sl + [sorted(l[0])])

    return list(zip(*sortedlists(l, [])))


def main():
    lists = [[i] * 5 for i in range(1000)]
    print(sortedzip(lists))
    print(sortedzip_tail(lists))


if __name__ == '__main__':
    main()
