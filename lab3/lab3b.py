import sys


def is_palindrome(char_list):
    if len(char_list) <= 1:
        return True

    if len(char_list) == 2:
        return char_list[0] == char_list[1]

    if char_list[0] == char_list[-1]:
        return is_palindrome(char_list[1:len(char_list) - 1])

    return False


def main():
    if len(sys.argv) != 2:
        print("Usage: lab3b.py <string>")
        return

    text = sys.argv[1]
    char_list = list(text)

    if is_palindrome(char_list):
        print("Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()
    
    
    