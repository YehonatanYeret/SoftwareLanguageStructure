def add_3_dict(d1, d2, d3):
    # from all the keys make dict with key, tuple of set of values(only those are not None)
    return dict(map(lambda x: (x, tuple(set(filter(None, map(lambda d: d.get(x), (d1, d2, d3)))))),
                    set(d1) | set(d2) | set(d3)))



