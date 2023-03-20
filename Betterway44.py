class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms 
        self.voltage = 0
        self.current = 0
        
r1 = Resistor(50e3)
r1.ohms = 10e3
r1.ohms += 5e3

class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage
    
    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


r2 = VoltageResistance(1e3)
print(f'이전: {r2.current:.2f} 암페어')
r2.voltage = 10
print(f'이후: {r2.current:.2f} 암페어')

class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms
    
    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'저항 > 0 이어야 합니다. 실제 값: {ohms}')
        self._ohms = ohms

# r3 = BoundedResistance(1e3)
# r3.ohms = 0

# BoundedResistance(-5)

class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Ohms는 불변 객체입니다")
        self._ohms = ohms

r4 = FixedResistance(1e3)
r4.ohms = 2e3

