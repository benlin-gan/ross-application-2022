import csv
def nxt(inp, modulus):
    return inp * 2 % modulus
def list(iters, modulus):
    k = 2
    for i in range(iters):
        print(k)
        k = nxt(k, modulus)
def repeat(inp, modulus, times):
    for i in range(times):
        inp = nxt(inp, modulus)
    return inp
def period(modulus):
    start = repeat(2, modulus, 2 * modulus)
    k = nxt(start, modulus) 
    for i in range(modulus):
        if(k == start):   
            return i + 1
        k = nxt(k, modulus)
if __name__ == "__main__":
    data = [];
    for i in range(7):
        data.append([['m', 'o(m)']])
        for j in range(40):
            num = j + i * 40 + 1
            data[i].append([num, period(num)])
    for i in range(7):
        with open('periods{}.csv'.format(i+1), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data[i])
