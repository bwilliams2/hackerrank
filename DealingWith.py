#Classes: Dealing with Complex Numbers
#https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers

class Complex:
    #initial definition of complex number
    def __init__(self,full):
        [r, i] = full.split(" ")
        self.realpart = float(r)
        self.imagpart = float(i)
    
    #addition of two complex numbers
    def __add__(self,other):
        bothreal = self.realpart + other.realpart
        bothimag = self.imagpart + other.imagpart
        return Complex('{} {}'.format(bothreal,bothimag))
    
    #subtraction of two complex numbers
    def __sub__(self,other):
        bothreal = self.realpart - other.realpart
        bothimag = self.imagpart - other.imagpart
        return Complex('{} {}'.format(bothreal,bothimag))
    
    #multiplication of two complex numbers
    def __mul__(self,other):
        first = self.realpart * other.realpart
        second = self.realpart * other.imagpart
        third = self.imagpart * other.realpart
        fourth = self.imagpart * other.imagpart
        bothreal = first - fourth
        bothimag = second + third
        return Complex('{} {}'.format(bothreal,bothimag))
    
    #division of two complex numbers
    def __truediv__(self,other):
        conj = Complex('{} {}'.format(other.realpart,-other.imagpart))
        denom = other * conj
        numer = self * conj
        bothreal = numer.realpart / denom.realpart
        bothimag = numer.imagpart / denom.realpart
        return Complex('{} {}'.format(bothreal,bothimag))
    
    #modulus of complex number
    def mod(self):
        first = self.realpart**2
        second = self.imagpart**2
        return Complex('{} {}'.format((first+second)**0.5,0))
    
    #string definition of complex number
    def __str__(self):
        if self.imagpart >= 0:
            prei = '+'
        else:
            prei=''
            
        return '{:.2f}{}{:.2f}i'.format(self.realpart,prei,self.imagpart)
        
A = Complex(input())
B = Complex(input())

print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A.mod())
print(B.mod())
        
