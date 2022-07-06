class Road:
    _length = 0
    _width = 0

    def __init__(self, length: float = 0, width: float = 0):
        self._length = length
        self._width = width

    def calc(self, density: float, thickness: float) -> float:
        return self._length * self._width * density * thickness

road = Road(100,50)
print(road.calc(25,5))