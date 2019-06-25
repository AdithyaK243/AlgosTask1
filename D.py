def main():
    c = []
    s = []
    i = 0
    n, r, x, y = map(int, input().split())
    c = list(map(int, input().split()))
    s = list(map(int, input().split()))
    rating = r
    for i in range(n):
        if c[i] == 1 and s[i] == 1:
            rating += x
        elif c[i] == 1 and s[i] == 0:
            rating -= y
    if rating > r:
        print("promoted")
    elif rating < r:
        print("demoted")
    else:
        print("no change")


if __name__ == "__main__":
    main()
