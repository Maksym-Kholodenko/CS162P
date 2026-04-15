class Pascal:
    def __init__(self):
        self.data = {}

    def get_value(self, row, col):
        if (row, col) in self.data:
            return self.data[(row, col)]

        if col == 0 or col == row:
            value = 1
        else:
            value = self.get_value(row - 1, col - 1) + self.get_value(row - 1, col)

        self.data[(row, col)] = value
        return value

    def display(self, lines):
        for row in range(lines):
            for col in range(row + 1):
                print(self.get_value(row, col), end=" ")
            print()


def main():
    triangle = Pascal()
    triangle.display(6)


if __name__ == "__main__":
    main()


