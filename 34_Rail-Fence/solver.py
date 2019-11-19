f = open("cipher.txt", "r")
s = f.read().rstrip()
for i in range(2, 101):
    print("check:", i)
    # lets make rail!!!
    rails = []
    ranges = list(range(i)) + list(range(i-2, 0, -1))
    for j in range(len(s)):
        rails.append(["!" if k == ranges[j%len(ranges)] else "." for k in range(i)])
    idx = 0
    for j in range(i):
        for k in range(len(rails)):
            if rails[k][j] == "!":
                rails[k][j] = s[idx]
                idx += 1

    # lets decrypt!!!
    c = ""
    for j in range(len(rails)):
        for k in range(i):
            if rails[j][k] != ".":
                c += rails[j][k]
    print(c)

