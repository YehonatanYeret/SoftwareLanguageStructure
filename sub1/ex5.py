def add_3_dict(d1, d2, d3):
    # from all the keys make dict with key, tuple of set of values(only those are not None)
    # we sort the set(in both sets) because set add the values in order that depend at stuff that
    # can change and we need determinism for pure functional
    return dict(map(lambda x: (x, tuple(sorted(set(filter(None, map(lambda d: d.get(x), (d1, d2, d3))))))),
                    sorted(set(d1) | set(d2) | set(d3))))

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = {'a': 1, 'c': 5, 'd': 6}

print(add_3_dict(d2, d1, d3))




