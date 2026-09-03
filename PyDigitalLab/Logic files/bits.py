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
            padding = [0] * (width - len(bin(value)[2:]))
            self.vector = padding + self.vector  # Adds the remaining slots with 0 (to make the bitvector of required width)

    def __str__(self):
        return f"{self.vector}"
    
    def __getitem__(self, key):
        return self.vector[key]

    def __setitem__(self, key, value):
        self.vector[key] = value
        self.value = 0
        for b in self.vector:
            self.value = (self.value << 1) | b

#Then we have BCD Representation of numbers.
class BCD:     #basic implementation done, check for methods.
    def __init__(self, value):
        try:
            num = int(value)
        except (ValueError, TypeError):
            raise ValueError("Invalid BCD: Input for BCD can only be an integer")
        if num < 0 or num > 99:
            raise ValueError("Class BCD only supports 2 digit integers.")
        self.value = num
        self.digits = [int(i) for i in str(num)]
        if len(self.digits) < 2:
            self.digits = [0]*(2-len(self.digits)) + self.digits
        self.bcd = [(str(bin(i)[2:])).zfill(4) for i in self.digits]

    def __str__(self):
        return f"{self.bcd}"

    def __getitem__(self, key):
        return self.bcd[key]

    def __setitem__(self, key, val):
        if len(val) != 4 or not all(a in '01' for a in val):
            raise ValueError("Invalid value: Value should be a 4-digit integer")
        self.bcd[key] = val
        if int(val, 2) > 9:
            raise ValueError("Invalid BCD Digit: Value must be between 1001 and 0000 inclusive")
        self.digits[key] = int(val,2)
        self.value = self.digits[0]*10 + self.digits[1]