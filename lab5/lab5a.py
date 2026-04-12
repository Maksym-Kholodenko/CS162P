import sys
from reversemath import ReverseFloat


def main():
    if len(sys.argv) != 3:
        print("Usage: lab5a.py <number1> <number2>")
        return

    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])

    a = ReverseFloat(num1)
    b = ReverseFloat(num2)

    print(f"a = {a}")
    print(f"b = {b}")
    print()

    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")


if __name__ == "__main__":
    main()


