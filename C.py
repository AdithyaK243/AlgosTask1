import collections


def arrayFinder(lists, l):
    arr = []
    count = collections.Counter(lists)
    c = collections.Counter(l)
    if 43 in lists:
        arr.append(43)
    if 7 in lists:
        arr.append(7)
    if 5 in lists:
        arr.append(10)
    if count[2] == 3 and not 5 in lists:
        arr.append(8)
    if count[2] == 4 and 5 in lists:
        arr.append(8)
    if count[2] == 4 and not 5 in lists:
        arr.append(16)
    if 3 in lists:
        arr.append(9)
    if count[2] == 7 and c[2] == 3:
        arr = [16, 8]
    if count[2] == 7 and c[2] == 4 and not 5 in c:
        arr = [8, 16]
    if count[2] == 7 and c[2] == 4 and 5 in c:
        arr = [16, 8]
    if count[2] == 7 and c[2] == 5:
        arr = [8, 16]
    return arr


def primeFact(n):
    primes = []
    i = 2
    while i*i <= n:
        while (n % i) == 0:
            primes.append(i)
            n //= i
        i += 1
    if n > 1:
        primes.append(n)

    return primes


def main():
    p = []
    q = []
    r = []
    s = []
    array = []
    print("1 2")
    x = int(input(""))
    p = primeFact(x)
    print("2 3")
    y = int(input(""))
    q = primeFact(y)
    array += arrayFinder(p, q)
    print("3 4")
    z = int(input(""))
    r = primeFact(z)
    array += arrayFinder(q, r)
    print("4 5")
    w = int(input(""))
    s = primeFact(w)
    array += arrayFinder(r, s)
    array += arrayFinder(s, s)

    if not 10 in array:
        array.append(10)
    if not 8 in array:
        array.append(8)
    if not 16 in array:
        array.append(16)
    if not 7 in array:
        array.append(7)
    if not 43 in array:
        array.append(43)
    if not 9 in array:
        array.append(9)

    array = list(dict.fromkeys(array))
    print(array)


if __name__ == "__main__":
    main()
