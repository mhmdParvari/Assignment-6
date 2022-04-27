def GreatestCommonDivisor(num1,num2):
    if num2<0: num2 *= -1
    if num1 < 0 : num1*=-1
    if num1<num2: num2,num1=num1,num2
    if num2==0: return num1
    while num1%num2>0:
        temp=num2
        num2=num1%num2
        num1 = temp
    return num2
	
class Rational:
    def __init__(self,num,den):
        self.numerator=num
        self.denominator=den
    
    def simplify(self):
        GCD=GreatestCommonDivisor(self.numerator,self.denominator)
        self.numerator = int(self.numerator/GCD)
        self.denominator = int(self.denominator/GCD)
    
    def show(self):
        print("(",end='')
        print(self.numerator,end='')
        print("/",end='')
        print(self.denominator,end='')
        print(")")

    def __add__(self,op2):
        return Rational(self.numerator*op2.denominator+self.denominator*op2.numerator,self.denominator*op2.denominator)
    
    def __sub__(self,op2):
        return Rational(self.numerator*op2.denominator-self.denominator*op2.numerator,self.denominator*op2.denominator)

    def __mul__(self,op2):
        return Rational(self.numerator*op2.numerator,self.denominator*op2.denominator)

    def __truediv__(self,op2):
        return Rational(self.numerator*op2.denominator,self.denominator*op2.numerator)

a=Rational(1,2)
b=Rational(2,6)
c=a+b
c.show()
c.simplify()
c.show()