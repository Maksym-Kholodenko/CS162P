from rock import Rock


def main():
    rock1 = Rock("Granite", "Gray", 7)
    rock2 = Rock("Quartz", "White", 8)
    rock3 = Rock("Obsidian", "Black", 5)

    print("Original objects:")
    print(f"{rock1.name} - Color: {rock1.color}, Hardness: {rock1.hardness}")
    print(f"{rock2.name} - Color: {rock2.color}, Hardness: {rock2.hardness}")
    print(f"{rock3.name} - Color: {rock3.color}, Hardness: {rock3.hardness}")

    rock2.color = "Clear"
    rock3.hardness = 6

    print()
    print("Updated objects:")
    print(f"{rock1.name} - Color: {rock1.color}, Hardness: {rock1.hardness}")
    print(f"{rock2.name} - Color: {rock2.color}, Hardness: {rock2.hardness}")
    print(f"{rock3.name} - Color: {rock3.color}, Hardness: {rock3.hardness}")


if __name__ == "__main__":
    main()
    
    
    