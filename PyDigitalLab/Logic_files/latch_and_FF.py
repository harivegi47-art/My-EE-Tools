#This is the file where we start building the actual logic components built over gates using the gates we made in gates.py
from gates import not_g, nand_g
from clock import clock
class D_latch:
    def __init__(self):
        self.Q = 0

    def update(self, D, E):
        if (D not in (0,1)):
            raise ValueError(f"D-Latch {self} n: D-Latch should receive D 0/1 but received {D}")
        if (E not in (0,1)):
            raise ValueError(f"D-Latch {self} n: D-Latch should receive E 0/1 but received {E}")
        intermediate_1 = nand_g(D,E)
        intermediate_2 = nand_g(not_g(D),E)
        self.Q = (nand_g(intermediate_1, nand_g(intermediate_2, self.Q)))

    def read(self):
        return self.Q


class D_FF:
    def __init__(self, input_clock):
        self.Q = 0
        self.clock = input_clock
        self.dlatch1 = D_latch()
        self.dlatch2 = D_latch()
    
    def update(self, D):
        if (D not in (0,1)):
            raise ValueError(f"D-FlipFlop {self} n: D-FlipFlop should receive D 0/1 but received {D}")
        self.dlatch1.update(D, not_g(self.clock.state))
        intermediate1 = self.dlatch1.read()
        self.dlatch2.update(intermediate1, self.clock.state)
        self.Q = self.dlatch2.read()

    def read(self):
        return self.Q