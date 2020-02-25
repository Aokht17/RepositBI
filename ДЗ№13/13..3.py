class MorePositive(set):

    def __init__(self, inp):
        self.inp = inp
        self.seq = set()

        for i in self.inp:
            if i > 0:
                self.seq.add(i)

    def new_el(self, a):
        """
        adds a new positive element to the set
        """
        if a > 0:
            self.seq.add(a)
        else:
            raise ValueError


d = MorePositive([1, 6, -7, 96, 0])
MorePositive.new_el(d, 76)
print(d.seq)
MorePositive.new_el(d, 0)





