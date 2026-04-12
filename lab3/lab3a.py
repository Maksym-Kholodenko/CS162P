import sys


def factorial1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial2(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial2(n - 1)


def main():
    if len(sys.argv) != 3:
        print("Usage: lab3a.py <iterative|recursive> <integer>")
        return

    method = sys.argv[1].lower()
    number = int(sys.argv[2])

    if number < 0:
        print("Factorial is not defined for negative integers.")
        return

    if method == "iterative":
        result = factorial1(number)
    elif method == "recursive":
        result = factorial2(number)
    else:
        print("Invalid method. Use iterative or recursive.")
        return

    print(f"{number}! = {result}")


if __name__ == "__main__":
    main()
    
    
    