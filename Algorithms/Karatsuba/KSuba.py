def simple_mul(x, y, B=10):
    m = max(len(str(x)), len(str(y))) >> 1

    if x < 10: return x * y

    x1 = x // B ** m
    x0 = x % B ** m

    y1 = y // B ** m
    y0 = y % B ** m

    z2 = simple_mul(x1, y1)
    z1 = simple_mul(x1, y0) + simple_mul(x0, y1)
    z0 = simple_mul(x0, y0)

    return z2 * (B ** (2 * m)) + z1 * (B ** m) + z0

def kar_mul(x, y, B=10):
    m = max(len(str(x)), len(str(y))) >> 1

    if x < 10: return x * y

    x1 = x // B ** m
    x0 = x % B ** m

    y1 = y // B ** m
    y0 = y % B ** m

    z2 = kar_mul(x1, y1)
    z0 = kar_mul(x0, y0)
    z1 = kar_mul((x1 + x0), (y1 + y0)) - z2 - z0

    return z2 * (B ** (2 * m)) + z1 * (B ** m) + z0
