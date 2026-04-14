import sys
from shapes import Point, Triangle, Diamond, Rectangle, Square


def main():
    if len(sys.argv) != 2:
        print("Usage: lab6.py <datafile>")
        return

    filename = sys.argv[1]
    shape_list = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split()
                shape_type = parts[0]
                symbol = parts[1]

                if shape_type == "P":
                    shape = Point(symbol)

                elif shape_type == "S":
                    size = int(parts[2])
                    shape = Square(symbol, size)

                elif shape_type == "T":
                    size = int(parts[2])
                    shape = Triangle(symbol, size)

                elif shape_type == "D":
                    size = int(parts[2])
                    shape = Diamond(symbol, size)

                elif shape_type == "R":
                    width = int(parts[2])
                    height = int(parts[3])
                    shape = Rectangle(symbol, width, height)

                else:
                    continue

                shape_list.append(shape)

        for shape in shape_list:
            shape.draw()
            print()

    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()


