def main():
    age_counts = {}

    with open("lab2-data.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            parts = line.split("|")
            age = int(parts[2])

            if age in age_counts:
                age_counts[age] += 1
            else:
                age_counts[age] = 1

    for age in sorted(age_counts):
        print(f"Age: {age} -> Count: {age_counts[age]}")


if __name__ == "__main__":
    main()
    
    
    