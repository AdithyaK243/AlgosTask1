def degOfSymmetry(length, string):
    if length // 2 == 0:
        return 0
    else:
        if string[:length // 2] == string[length // 2:]:
            return 1 + degOfSymmetry(length // 2, string[:length // 2])
        else:
            return 0


def main():
    length = int(input(""))
    string = input("")
    print(degOfSymmetry(length, string))


if __name__ == "__main__":
    main()
