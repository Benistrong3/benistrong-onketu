
class Fraction:
    def __init__(self, _numerateur, _denominateur):
        assert isinstance(_numerateur, int) and isinstance(_denominateur, int) and _denominateur > 0, "le dénominateur doit être un entier strictement positif"
        self._numerateur = _numerateur
        self._denominateur = _denominateur
        
    def __str__(self):
        if self._denominateur == 1:
            return str(self._numerateur)
        else:
            return f"{self._numerateur}/{self._denominateur}"
    
    def eq(self, other):
        return self._numerateur*other._denominateur == other._numerateur*self._denominateur

#test
if __name__ == '__main__':
    
    
    Fraction1 = Fraction(6, 8)
    Fraction2 = Fraction(-16, 2)
    Fraction3 = Fraction(4, 6)
    Fraction4 = Fraction(42, 56)
    
    
    print(Fraction1)
    print(Fraction2)
    print(Fraction3)
    print(Fraction4)
    
    
    print(Fraction1.eq(Fraction3)) 
    print(Fraction2.eq(Fraction4)) 
    print(Fraction1.eq(Fraction1))
    
