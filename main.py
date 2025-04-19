def process():
    b = 99
    c = b
    # Equivalent to 'jnz a 2' and 'jnz 1 5'
    # Since 'a' is not initialized and 'jnz 1 5' always jumps, it effectively starts here:
    b *= 100
    b += 100000
    c = b
    c += 17000
    h = 0

    while True:
        f = 1
        d = 2
        while d * d <= b:  # Optimization: check divisors up to the square root of 'b'
            if b % d == 0:  # Checking if 'b' is divisible
                f = 0
                break
            d += 1
        if f == 0:
            h += 1
        if b == c:
            break
        b += 17

    return h

print(process())
