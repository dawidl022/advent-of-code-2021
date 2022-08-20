from enum import Enum


class Pixel(Enum):
    DARK = 0
    LIGHT = 1

    @staticmethod
    def fromSymbol(symbol: str) -> 'Pixel':
        if symbol == '#':
            return Pixel.LIGHT
        elif symbol == '.':
            return Pixel.DARK
        else:
            raise ValueError()

    @staticmethod
    def fromList(symbols: str) -> list['Pixel']:
        return [Pixel.fromSymbol(c) for c in symbols]

    @staticmethod
    def fromMatrix(matrix: list[str]) -> list[list['Pixel']]:
        return [Pixel.fromList(line) for line in matrix]
