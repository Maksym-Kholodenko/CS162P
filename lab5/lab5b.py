from gadget import Gadget


def main():
    gadget1 = Gadget("Tablet", 299.99)
    gadget2 = Gadget("Headphones", 89.50)

    print("Original values:")
    print(f"Gadget 1: {gadget1.name}, ${gadget1.price:.2f}")
    print(f"Gadget 2: {gadget2.name}, ${gadget2.price:.2f}")
    print()

    gadget1.name = "Laptop"
    gadget1.price = 799.99

    gadget2.name = "Speaker"
    gadget2.price = 129.95

    print("Updated values:")
    print(f"Gadget 1: {gadget1.name}, ${gadget1.price:.2f}")
    print(f"Gadget 2: {gadget2.name}, ${gadget2.price:.2f}")


if __name__ == "__main__":
    main()


