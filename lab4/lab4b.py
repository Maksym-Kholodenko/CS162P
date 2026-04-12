class MyMath:
    def absolute(self, number):
        if number < 0:
            return -number
        return number

    def average(self, numbers):
        total = 0
        count = 0

        for number in numbers:
            total += number
            count += 1

        if count == 0:
            return 0

        return total / count


def main():
    math_obj = MyMath()

    print("Absolute value tests:")
    print(f"absolute(-8) = {math_obj.absolute(-8)}")
    print(f"absolute(12) = {math_obj.absolute(12)}")
    print(f"absolute(0) = {math_obj.absolute(0)}")

    print()
    print("Average tests:")
    print(f"average([2, 4, 6, 8]) = {math_obj.average([2, 4, 6, 8])}")
    print(f"average([10, 15, 20]) = {math_obj.average([10, 15, 20])}")
    print(f"average([5]) = {math_obj.average([5])}")


if __name__ == "__main__":
    main()


