class Monom:

    def __init__(self, coeff, value, power):
        self.coeff = coeff
        self.value = value
        self.power = power
        self.string = ''

    def __str__(self):
        if self.coeff > 1:
            self.string = '{}'.format(self.coeff)
        if self.power > 0:
            if self.coeff > 1:
                self.string += '*{}'.format(self.value)
            else:
                self.string += self.value
        if self.power > 1:
            self.string += '^{}'.format(self.power)
        return '{}'.format(self.string)

    def __add__(self, other):
        if self.value == other.value and self.power == other.power:
            return(self.coeff + other.coeff, self.value, self.power)
        else:
            print('Error -> {} is different from {}'.format(self, other))
    def __eq__(self, other):
        return self.value+str(self.power) == other.value+str(other.power)

    def __hash__(self):
        return hash(self.value+str(self.power))

    def derivative(self):
        if self.power > 0:
            self.coeff *= self.power
            self.power -= 1
        else:
            self.coeff = 0
            self.value = 0
            self.power = 0
        return(self.coeff, self.value, self.power)
