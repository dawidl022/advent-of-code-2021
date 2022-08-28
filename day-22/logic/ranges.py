def combine_ranges(a: range, b: range) -> range:
    if a.stop < b.start or b.stop < a.start:
        raise DisjointRangesError
    return range(min(a.start, b.start), max(a.stop, b.stop))


class DisjointRangesError(ValueError):
    pass
