from util.run import run


class PlayerStats:
    def __init__(self, position: int):
        self._position = position - 1
        self.score = 0

    @property
    def position(self) -> int:
        return self._position + 1

    def advance(self, spaces: int) -> None:
        self._position = (self._position + spaces) % 10
        self.score += self.position


class Dice:
    def __init__(self, sides: int):
        self.sides = sides
        self.current = -1

    @property
    def roll_count(self) -> int:
        return self.current + 1

    def roll_deterministically_three_times(self) -> int:
        self.current += 3
        return self.current * 3


WINNING_SCORE = 1000
DICE_SIDES = 100


def solution(p1_start: int, p2_start: int) -> int:
    p1 = PlayerStats(p1_start)
    p2 = PlayerStats(p2_start)
    die = Dice(DICE_SIDES)

    turn = 0

    while p1.score < WINNING_SCORE and p2.score < WINNING_SCORE:
        roll = die.roll_deterministically_three_times()
        if turn % 2 == 0:
            p1.advance(roll)
        else:
            p2.advance(roll)
        turn += 1

    return min(p1.score, p2.score) * die.roll_count


if __name__ == "__main__":
    run(solution)
