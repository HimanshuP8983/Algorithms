from math import ceil, floor

def karatsuba(x,y):
    if x<10 and y<10:
        return x * y

    n = max(len(str(x)),len(str(y)))
    m = ceil(n/2)

    x_H = floor(x/10**m)
    x_L = x % (10**m)

    y_H = floor(y/10**m)
    y_L = y % (10**m)


    #recursive steps
    a = karatsuba(x_H,y_H)
    d = karatsuba(x_L,y_L)
    e = karatsuba(x_H + x_L,y_H + y_L) - a - d

    return int(a*(10**(m*2)) + e*(10**m) + d)

if __name__ == "__main__":
    print(karatsuba(3,2))