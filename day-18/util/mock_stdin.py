# mock turned out to be not useful, but decided to keep it in source control anyways

class MockStdin:
    def __init__(self, lines: list[str]) -> None:
        self.index = 0
        self.lines = lines

    def __call__(self):
        if self.index >= len(self.lines):
            raise EOFError()

        res = self.lines[self.index]
        self.index += 1
        return res
