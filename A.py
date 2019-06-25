def average(length, binary):
    if binary[1:] > "0"*(length - 1) and binary < "1"*length:
        num = int(binary, 2)
        return bin(num-1)[2:] + " " + bin(num + 1)[2:]
    else:
        return -1


def main():
    length = int(input("enter the length of string:"))
    binary = input("enter the binary string:")
    print(average(length, binary))


if __name__ == "__main__":
    main()
