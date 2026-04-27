import sys


def main():
    args = sys.argv
    if (len(args) == 1):
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    file_name = args[1]
    print(f"Accessing file '{file_name}'")
    try:
        content = ""
        file = open(file_name)
        print("---")
        print()
        content = file.read()
        print(content)
        print("---")
        file.close()
        print(f"file '{file_name}' is closed.")
        print()
    except Exception as e:
        print(f"[STDERR] Error opening file '{file_name}'", e, file=sys.stderr)
        return
    print("Transform data:")
    new_content = ""
    for char in content:
        if (char == "\n"):
            new_content += "#"
        new_content += char
    print("---")
    print()
    print(new_content)
    print("---")
    try:
        print("Enter new file name (or empty): ", end="", flush=True)
        new_name = sys.stdin.readline().rstrip("\n")
        if (new_name.strip('\n') == ""):
            print("Not saving data.")
            return
        print(f"Saving data to '{new_name}'")
        new_file = open(new_name, "w")
        new_file.write(new_content)
        new_file.close()
        print(f"Data saved in file '{new_name}'.")
    except Exception as e:
        print(f"[STDERR] Error writing to file '{new_name}':", e,
              file=sys.stderr)
        print("Data not saved.")


if __name__ == '__main__':
    main()
