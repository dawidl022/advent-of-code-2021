from util.constants import ADULT_TIMER, CHILD_TIMER
from util.run import run

SIMULATION_TIME = 80


def solution(fish_timers: list[int], simulation_days: int) -> int:
    for _ in range(simulation_days):
        for i in range(len(fish_timers)):
            if fish_timers[i] == 0:
                fish_timers[i] = ADULT_TIMER
                fish_timers.append(CHILD_TIMER)
            else:
                fish_timers[i] -= 1

    return len(fish_timers)


if __name__ == "__main__":
    run(solution, SIMULATION_TIME)
