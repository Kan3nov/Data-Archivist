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
    pass


if __name__ == "__main__":
    main()
