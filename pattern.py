__author__ = 'jqly'


def pattern(n):
    pat = list(map(str, range(1, n+1)))
    return "\n".join("".join(pat[i:]) for i in range(n))

print(pattern(6))

