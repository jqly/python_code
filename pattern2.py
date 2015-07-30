__author__ = 'jqly'


def pattern2(n):
    # Happy Coding ^_^
    if n <= 0 or n > 100:
        return ""
    blank = " "*(n-1)
    num_seq = ("1234567890"*10)[:n]
    return "\n".join([blank[:i] + num_seq + blank[i:] for i in range(n-1, -1, -1)])

print(pattern2(10))

