class Fractie:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return str(self.a) + "/" + str(self.b)

    def __add__(self, other):
        if self.b == other.b:
            new_a = self.a + other.a
            return Fractie(new_a, self.b)
        else:
            aux1 = self.b
            aux2 = other.b
            b1 = self.b * aux2
            a1 = self.a * aux2

            b2 = aux1 * other.b
            a2 = aux1 * other.a

            new_a = a1 + a2
            return Fractie(new_a, b1)

    def __sub__(self, other):
        if self.b == other.b:
            new_a = self.a - other.a
            return Fractie(new_a, self.b)
        else:
            aux1 = self.b
            aux2 = other.b
            b1 = self.b * aux2
            a1 = self.a * aux2

            b2 = aux1 * other.b
            a2 = aux1 * other.a

            new_a = a1 - a2
            return Fractie(new_a, b1)

    def inverse(self):
        aux = self.a
        self.a = self.b
        self.b = aux
        return Fractie(self.a, self.b)


f1 = Fractie(5, 2)
f2 = Fractie(3, 2)
print(f1 + f2)
print(f2 - f1)
