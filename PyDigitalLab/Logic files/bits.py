# This is the file containing the classes of different number representations - Bits

# We first have a class which takes value and bit size to create a bit vector.
class N_Bits(): #Takes a value and creates a BitVector for it.
    def __init__(self, value, width):
        self.value = value    
        self.width = width
        self.vector = [int(i) for i in bin(value)[2:]] # Extracts the binary code
        if len(self.vector) > width:
            raise ValueError(f"The given value can't be stored in {width} bits")
        else:
            for i in range(width - len(self.vector)):
                self.vector = [0] + self.vector  # Adds the remaining slots with 0 (to make the bitvector of required width)

    def __str__(self):
        return f"{self.vector}"
    
    def __getitem__(self, key):
        return self.vector[key]

    def __setitem__(self, key, value):
        self.vector[key] = value
        self.value = 0
        for b in self.vector:
            self.value = (self.value << 1) | b