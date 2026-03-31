import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python linecount.py <filename>")
        return

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            line_count = sum(1 for line in file)

        print(f"Number of lines: {line_count}")
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()