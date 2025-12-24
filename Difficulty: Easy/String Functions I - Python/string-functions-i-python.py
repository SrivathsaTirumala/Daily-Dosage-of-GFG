def trim(s):
    return s.strip()


def exists(s, x):
    if x in s:
        return s.find(x)
    return -1


def titleIt(s):
    return s.title()


def casesSwap(s):
    return s.swapcase()
