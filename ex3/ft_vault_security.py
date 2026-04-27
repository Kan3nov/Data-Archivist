def secure_archive(file_name: str,
                   acc_perm: str = "r",
                   content: str = "meow\n") -> tuple[bool, str]:
    if (acc_perm != "r" and acc_perm != "w"):
        return (False, "Invalid access permission")
    try:
        with open(file_name, acc_perm) as f:
            if (acc_perm == "w"):
                f.write(content)
                return (True, "Content succssfully written fo file")
            else:
                content = f.read()
                return (True, content)
    except Exception as e:
        return (False, str(e))


def main():
    print("=== Cyber Archives Security ===")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("non-existing"))
    print()
    print("Using 'secure_archive' to read from an inaccessable file:")
    print(secure_archive("inaccessable"))
    print()
    print("Using 'secure_archive' to read from a regular file:")
    Boolean, content = secure_archive("meow")
    print((Boolean, content))
    print()
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file", "w", content))


if __name__ == "__main__":
    main()
