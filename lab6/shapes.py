class Point:
    def __init__(self, symbol="."):
        self.symbol = symbol

    def setSymbol(self, symbol):
        self.symbol = symbol

    def draw(self):
        print(self.symbol)


class Triangle(Point):
    def __init__(self, symbol="*", size=1):
        super().__init__(symbol)
        self.size = size

    def draw(self):
        for i in range(1, self.size + 1):
            print(self.symbol * i)


class Diamond(Point):
    def __init__(self, symbol="*", size=1):
        super().__init__(symbol)
        self.size = size

    def draw(self):
        for i in range(1, self.size + 1):
            spaces = " " * (self.size - i)
            chars = self.symbol * (2 * i - 1)
            print(spaces + chars)

        for i in range(self.size - 1, 0, -1):
            spaces = " " * (self.size - i)
            chars = self.symbol * (2 * i - 1)
            print(spaces + chars)


class Rectangle(Point):
    def __init__(self, symbol="*", width=1, height=1):
        super().__init__(symbol)
        self.width = width
        self.height = height

    def draw(self):
        for _ in range(self.height):
            print(self.symbol * self.width)


class Square(Rectangle):
    def __init__(self, symbol="*", size=1):
        super().__init__(symbol, size, size)


