class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def reduce(self):
        """Returns a reduced form of this fraction
        """
        import math
        g = math.gcd(self.num, self.den)
        return Fraction(self.num//g, self.den//g)

    def add(self, m):
        """Returns a new fraction in reduced form that results from adding this fraction with the m fraction
        """ 
        f_num = self.num*m.den + m.num*self.den
        f_den = self.den*m.den
        f = Fraction(f_num, f_den)
        return f.reduce()

    def negate(self):
        return Fraction(-self.num, self.den)

    def subtract(self, m):
        """Returns a new fraction in reduced form that results from subtracting this fraction with the m fraction
        """ 
        f = m.negate()
        return self.add(f)
    
    def multiply(self, n):
        """Returns a new fraction in reduced form that results from multiplying this fraction with the n fraction
        """         
        f_num = self.num*n.num
        f_den = self.den*n.den
        f = Fraction(f_num, f_den)
        return f.reduce()
    
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        return self.add(other)
    
    def __mul__(self, other):
        return self.multiply(other)
    
    def __sub__(self, other):
        return self.subtract(other)

    def __eq__(self, other):
        reduce_self = self.reduce()
        reduce_other = other.reduce()
        return (reduce_self.num == reduce_other.num) and (reduce_self.den == reduce_other.den)
