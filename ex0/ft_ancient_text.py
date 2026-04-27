import sys


def main():
    args = sys.argv
    if (len(args) == 1):
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    file_name = args[1]
    print(f"Accessing file '{file_name}'")
    try:
        file = open(file_name)
        print("---")
        print()
        print(file.read())
        print()
        print("---")
        file.close()
        print(f"file '{file_name}' is closed.")
    except Exception as e:
        print(f"Error opening file '{file_name}'", e)


if __name__ == '__main__':
    main()
