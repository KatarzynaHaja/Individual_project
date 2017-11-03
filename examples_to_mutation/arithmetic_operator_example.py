def arithemtic(a,b):
    c = a*b
    d = c+a
    e = a**d
    if e < c:
        return 2
    else:
        c += 3
    if c != a*b:
        return 10