def invMod(x, p):
    return pow(x, p-2, p)

def addECC(x1, y1, x2, y2, a, b, p):
    # 2^20 of P addition, so P = Q
    s = (invMod(2*y1, p) * (3*x1*x1 + a)) % p
    x3 = (s*s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return x3, y3

def scalar(n, x, y, a, b, p):
    #it has a limit that can only calculate when n = 2, 4 ,6 ... 2**20, ...
    while n != 1:
        x, y = addECC(x, y, x, y, a, b, p)
        n/=2
        '''
        every two P(x, y) can calculate one R(x3, y3), and now there're 2**19 of R; every two R can produce one R'(x4, y4), and there are only 2**18 of R'. And repeat those procedures until there is only 2**0 (one) result.
        '''
    return x ,y