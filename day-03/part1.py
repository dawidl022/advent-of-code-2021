from util.run import run


def solution(numbers: list[int], bin_digit_count: int) -> int:
    # use bitwise AND to get individual bit (&)
    # and use bitwise shift left (<<) to iterate through bits in number

    mask = 0b1
    gamma = 0
    epsilon = 0

    for _ in range(bin_digit_count):
        one_count = 0

        for num in numbers:
            if num & mask != 0:
                one_count += 1

        if one_count > len(numbers) // 2:
            gamma += mask
        else:
            epsilon += mask

        mask <<= 1

    return gamma * epsilon


if __name__ == "__main__":
    run(solution)
