s = 'agatacaca'
s1 = s[::-1]  # 1
print(s1)
text1 = ''.join(reversed(s))  # 2
print(text1)


def perevorot(d):  # 3
    tr = str()
    for i in range(len(d)):
        tr += (d[len(d) - i - 1])
    return (tr)


print(perevorot(s))


def reverse(r):  # 4
    if len(r) == 2:
        return r[-1] + r[0]
    if len(r) == 1:
        return r[0]
    return r[-1] + reverse(r[1:len(r) - 1]) + r[0]


print(reverse(s))


def rev(t):  # 5
    i = list(t)
    o = list()
    while len(i) > 0:
        o.append(i.pop())
    return ''.join(o)


print(rev(s))
