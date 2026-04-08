def main():
    profession_data = {}

    with open("lab2-data.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split("|")
            profession = parts[3]
            rate = float(parts[4])

            if profession not in profession_data:
                profession_data[profession] = [0, 0.0]

            profession_data[profession][0] += 1
            profession_data[profession][1] += rate

    for profession in sorted(profession_data):
        count = profession_data[profession][0]
        total = profession_data[profession][1]
        average = total / count
        print(f"{profession} -> Average Rate: {average:.2f}")


if __name__ == "__main__":
    main()
    
    
    