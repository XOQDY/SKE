class Complex:
    def __init__(self, re, im):
        """Must check if re and im are of the same types"""
        self.re = re
        self.im = im

    def add(self, m):
        new_re = self.re + m.re
        new_im = self.im + m.im
        return Complex(new_re, new_im)

    def __add__(self, m):
        return self.add(m)

    def subtract(self, m):
        new_re = self.re - m.re
        new_im = self.im - m.im
        return Complex(new_re, new_im)
    
    def __sub__(self, m):
        return self.subtract(m)
    
    def multiply(self, n):
        new_re = (self.re * n.re) - (self.im * n.im)
        new_im = (self.re * n.im) + (self.im * n.re)
        return Complex(new_re, new_im)
    
    def __mul__(self, n):
        return self.multiply(n)
    
    def __str__(self):
        return str(self.re) + " + " + str(self.im) + "j"
