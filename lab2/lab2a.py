def main():
    people = []

    with open("lab2-data.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split("|")
            name = parts[1]
            age = int(parts[2])

            people.append(f"{age}|{name}")

    people.sort()

    for item in people:
        parts = item.split("|")
        age = parts[0]
        name = parts[1]
        print(f"{name} - Age {age}")


if __name__ == "__main__":
    main()
    
    
    