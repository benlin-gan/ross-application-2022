def next(input, modulus):
    return input * 2 % modulus
def list(iters, modulus):
    k = 2
    for i in range(iters):
        print(k)
        k = next(k, modulus)
def repeat(input, modulus, times):
    for i in range(times):
        input = next(input, modulus)
    return input
def period(modulus):
    start = repeat(2, modulus, 2 * modulus)
    k = next(start, modulus) 
    for i in range(modulus):
        if(k == start):   
            return i + 1
        k = next(k, modulus)
if __name__ == "__main__":
    print(period(int(input("Input Positive Integer: "))))
