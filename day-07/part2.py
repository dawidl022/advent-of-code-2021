from util.run import run


def solution(horizontals: list[int]) -> int:
    start = 0
    end = max(horizontals)
    mid = calc_average(horizontals)  # good starting approximation
    h = tuple(horizontals)

    # binary search until global minimum is found
    while exists_cheaper_neighbour(h, mid):
        if fuel_cost(h, mid - 1) < fuel_cost(h, mid + 1):
            end = mid - 1
        else:
            start = mid + 1

        mid = (start + end) // 2

    return fuel_cost(h, mid)


def exists_cheaper_neighbour(h: tuple[int, ...], p: int) -> bool:
    return fuel_cost(h, p - 1) < fuel_cost(h, p) \
        or fuel_cost(h, p + 1) < fuel_cost(h, p)


def calc_average(nums: list[int]) -> int:
    return round(sum(nums) / len(nums))


def memoize(func):
    # TODO write a proper memoization decorator
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result

        return result

    return wrapper


@memoize
def fuel_cost(horizontals: tuple[int, ...], target: int) -> int:
    fuel_cost = 0
    for hor in horizontals:
        fuel_cost += calc_arithmetic_series_sum(1, abs(hor - target))

    return fuel_cost


@memoize
def calc_arithmetic_series_sum(a1: int, n: int, diff: int = 1) -> int:
    return (2 * a1 + diff * (n - 1)) * n // 2


if __name__ == "__main__":
    run(solution)
