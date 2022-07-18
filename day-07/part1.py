from util.run import run


def solution(horizontals: list[int]) -> int:
    median = calc_median(horizontals)

    fuel_cost = calc_cost(horizontals, median)

    return fuel_cost


def calc_cost(horizontals: list[int], target: int):
    fuel_cost = 0

    for hor in horizontals:
        fuel_cost += abs(hor - target)
    return fuel_cost


def calc_median(nums: list[int]) -> int:
    nums = sorted(nums)
    mid_index = len(nums) // 2
    return nums[mid_index] if len(nums) % 2 != 0 else (
        nums[mid_index] + nums[mid_index - 1]) // 2


if __name__ == "__main__":
    run(solution)
