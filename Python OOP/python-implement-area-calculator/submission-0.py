import math

class AreaCalc:
    # TODO: Implement calculate method
    # pass
    def calculate(self, length, width=None):
        # Calculate circle area
        if width == None:
            return round((math.pi) * pow(length, 2), 2)
        else:
            return length * width
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
