def add_3_dict(d1, d2, d3):
    # from all the keys make dict with key, tuple of set of values(only those are not None)
    return dict(map(lambda x: (x, tuple(set(filter(None, map(lambda d: d.get(x), (d1, d2, d3)))))), list(d1.keys()) + list(d2.keys()) + list(d3.keys())))


