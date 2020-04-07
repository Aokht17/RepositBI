class MorePositive(set):

    def __init__(self, inp):
        super().__init__()
        self.inp = inp

        for i in self.inp:
            if i > 0:
                super().add(i)

    def add(self, a):
        """
        adds a new positive element to the set
        """
        if a > 0:
            super().add(a)
       


d = MorePositive([1, 6, -7, 96, 0])


print(d)
d = MorePositive([1, 6, -7, 96, 0])
MorePositive.add(d, 76)
d.add(90)
print(d)
print(d.difference([1, 2]))
