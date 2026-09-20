# This is the file containing the classes of different number representations - Bits

# We first have a class which takes value and bit size to create a bit vector.
class N_Bits(): #Takes a value and width and creates a BitVector for it.
    def __init__(self, value, width):
        if not isinstance(value, int) or isinstance(value, bool): #checks for value not being integer or boolean
            raise TypeError("value must be a non-negative integer")
        if not isinstance(width, int) or isinstance(width, bool): #checks for width not being integer or boolean
            raise TypeError("width must be a positive integer")
        if value < 0:                                             #checks whether value is non-negative or not
            raise ValueError("value must be non-negative")
        if width <= 0:                                            #checks whether width is positive or not
            raise ValueError("width must be positive")
        self.value = value    #assigns the respective values
        self.width = width
        self.vector = [int(i) for i in bin(value)[2:]] # Extracts the binary code
        if len(self.vector) > width:
            raise ValueError(f"The given value can't be stored in {width} bits")
        else:
            padding = [0] * (width - len(self.vector))
            self.vector = padding + self.vector  # Adds the remaining slots with 0 (to make the bitvector of required width)

    def __str__(self): #defines string attribute of N_Bits
        return "".join(map(str, self.vector))
    
    def __getitem__(self, key):  #defines what is obtained when N_Bits is accessed through a key
        return self.vector[key]

    def __setitem__(self, key, value):  #defines what is assigned value when key is being accessed and assigned a value
        if value not in (0, 1, False, True):
            raise ValueError("A bit must be 0 or 1")
        self.vector[key] = value  
        self.value = 0                  #updates the value of N_Bits (since BitVector changed, value also changes)
        for b in self.vector:
            self.value = (self.value << 1) | b

#Then we have BCD Representation of numbers.
class BCD:     
    def __init__(self, value):
        try:
            num = int(value)
        except (ValueError, TypeError):   #raises error in case of non-integer value
            raise ValueError("Invalid BCD: Input for BCD can only be an integer")
        if num < 0 or num > 99:           #reinforces the 2-digit availability
            raise ValueError("Class BCD only supports 2 digit integers.")
        self.value = num                  #assigns value attribute with the value
        self.digits = [int(i) for i in str(num)]
        if len(self.digits) < 2:          #assigns digits attribute with required padding
            self.digits = [0]*(2-len(self.digits)) + self.digits
        self.bcd = [(str(bin(i)[2:])).zfill(4) for i in self.digits]

    def __str__(self):                    #defines how string is accessed
        return f"{self.bcd}"

    def __getitem__(self, key):           #defines what is accessed via key
        return self.bcd[key]

    def __setitem__(self, key, val):      #defines how value at an index is changed
        if len(val) != 4 or not all(a in '01' for a in val): #raises error if value attempting to be changed is invalid
            raise ValueError("Invalid value: Value should be a 4-digit integer")
        if int(val, 2) > 9:
            raise ValueError("Invalid BCD Digit: Value must be between 1001 and 0000 inclusive")
        self.bcd[key] = val
        self.digits[key] = int(val,2)
        self.value = self.digits[0]*10 + self.digits[1]      #updates with the newly changed value for BCD

#Now we go for general utility functions:
def valid_width(value, width):
    if not isinstance(value,int) or isinstance(value,bool):     #raises error for non - integer value
        raise ValueError("Value: it should be integer")
    if not isinstance(width,int) or isinstance(width,bool):     #raises error for non - integer width
            raise ValueError("Width: it should be integer")
    if value < 0:                                               #raises error for negative integer
        raise ValueError("Value should be a non-negative integer")
    if width <= 0:                                              #raises error for non-positive integer
        raise ValueError("Width should be a positive integer")
    if pow(2,width) > value: #main logic for width validation
        return True
    else:
        raise ValueError("Width_validation: The given bits can't be stored in the given width")