from random import *

class RSAgenerator:
    def __init__(self):
        self.p = self.getPQ()
        self.q = self.getPQ(self.p)
        self.n = self.p * self.q
        self.phi = (self.p - 1)*(self.q - 1)
        self.e = self.getE()
        self.d = self.getD()
    
    def getPQ(self, p = 0):
        r = randint(1000, 9999 - 1)
        while not self.isPrime(r) or r == p:
            r = randint(1000, 9999 - 1)
        return r

    def isPrime(self, n):
        for x in range(2,n-1):
            if n % x == 0:
                return False
        return True

    def nwd(self, a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    
    def getE(self):
        e = 2
        res = self.nwd(self.phi, e)
        while res != 1 and self.isPrime(e):
            e += 1
            res = self.nwd(self.phi, e)
        return e    
    
    def getD(self):
        d = 1
        res = self.e * d - 1
        while res % self.phi != 0:
            d += 1
            res = self.e * d - 1
        return d

    def privateKey(self):
        return (self.d, self.n)

    def publicKey(self):
        return (self.e, self.n)
    
    @staticmethod
    def formula(x, y, p):
        res = 1
        x = x % p
        while (y > 0):
            if ((y & 1) == 1):
                res = (res * x) % p
            y = y >> 1
            x = (x * x) % p
        return res

