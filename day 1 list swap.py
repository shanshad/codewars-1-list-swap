def exchange_with(a, b):
    c = a[::-1]
    a[:] = b[::-1]
    b[:] = c