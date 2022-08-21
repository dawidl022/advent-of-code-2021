from abc import abstractmethod, ABC
from util.run import run


def memoize(func):
    memoized = {}

    def wrapper(*args):
        if (mem := memoized.get(args)) is not None:
            return mem
        result = func(*args)
        memoized[args] = result
        return result

    return wrapper


ROLLS = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1
}
"""
    For each turn, there are a total of 3^3 (27) variations (with repetitions) of dice throws.
    If we draw them out and count how many times each sum of dice throws appears, we get the
    mapping of dice throw sum to count of occurrence.

    This is the third time in this advent of code when an exponential problem can be optimised
    by grouping things together and multiplying by their count.
"""

WINNING_SCORE = 21


class Simulator(ABC):
    @abstractmethod
    def p1_increment(self) -> int:
        """The amount to increment the number of universes by when player 1 wins the game"""
        pass

    @abstractmethod
    def p2_increment(self) -> int:
        """The amount to increment the number of universes by when player 2 wins the game"""
        pass

    @memoize
    def simulate(self, p1_pos: int, p1_score: int, p2_pos: int, p2_score: int, p1_to_move: bool) -> int:
        """Pos is 0 based to make calculations easier, pos + 1 is therefore added to the score"""
        if p1_score >= WINNING_SCORE:
            return self.p1_increment()
        elif p2_score >= WINNING_SCORE:
            return self.p2_increment()

        if p1_to_move:
            pos = [(p1_pos + roll) % 10 for roll in ROLLS]
            return sum(
                self.simulate(pos[i], p1_score + pos[i] +
                              1, p2_pos, p2_score, False)
                * ROLLS[roll] for i, roll in enumerate(ROLLS))
        else:
            pos = [(p2_pos + roll) % 10 for roll in ROLLS]
            return sum(
                self.simulate(p1_pos, p1_score,
                              pos[i], p2_score + pos[i] + 1, True)
                * ROLLS[roll] for i, roll in enumerate(ROLLS))


class SimulatorP1(Simulator):
    """Counts the number of universes where Player 1 won"""

    def p1_increment(self) -> int:
        return 1

    def p2_increment(self) -> int:
        return 0


class SimulatorP2(Simulator):
    """Counts the number of universes where Player 2 won"""

    def p1_increment(self) -> int:
        return 0

    def p2_increment(self) -> int:
        return 1


def solution(p1_start: int, p2_start: int) -> int:
    args = (p1_start - 1, 0, p2_start - 1, 0, True)
    return max(SimulatorP1().simulate(*args), SimulatorP2().simulate(*args))


if __name__ == "__main__":
    run(solution)
