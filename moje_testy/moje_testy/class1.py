#%%
class AlwaysPos:
    def __init__(self, number):
        self.nnn = number

    def __add__(self, other):
        return abs(self.nnn + other.nnn)

    def __sub__(self, other1):
        return abs(self.nnn - other1.nnn)

    def __mul__(self, other2):
        return (self.nnn * other2.nnn)/1000

x = AlwaysPos(-20)
y = AlwaysPos(10)

print(x + y)
print(x * y)
print(x - y)

