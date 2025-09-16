from tail_recurse import tail_call_optimized


# Zip the inner lists with * after sort the recursively
def sortedzip(l):
    def sortedlists(l):
        if len(l) == 1:
            return sorted(l)
        return [sorted(l[0])] + sortedlists(l[1:])

    return list(zip(*sortedlists(l)))


# The same, but now we send the sorted part in parameter, so we get a tail
def sortedzip_tail(l):
    @tail_call_optimized
    def sortedlists(l, sl):
        if len(l) == 1:
            return sl + sorted(l)
        return sortedlists(l[1:], sl + [sorted(l[0])])

    return list(zip(*sortedlists(l, [])))


def main():
    lists = [[3, 1, 2], [5, 6, 4], ['a', 'b', 'c']]
    # print(sortedzip(lists))
    print(sortedzip_tail(lists))


if __name__ == '__main__':
    main()
