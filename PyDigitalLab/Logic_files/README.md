# Logic files

These files contain the core logic for the project.

## bits.py

This file provides object types for number representation and conversion between different representations.

### class N_Bits

This class takes a numeric value and an intended bit-width, and stores it as a `BitVector` in the form of a Python list. If the given width is not sufficient to represent the value, a `ValueError` is raised.

Example:
```python
Bit = N_Bits(5, 4)
```

- Printing the object prints the bits string.  
  Example: `print(Bit)` → `0101`

- Each bit can be accessed using `obj[index]`.  
  Example: `Bit[1]` → `1`

- Any bit can be reassigned using `obj[index] = value`; the internal `value` attribute is automatically updated.  
  Example: `Bit[3] = 0` changes the bit pattern to `[0, 1, 0, 0]` and updates `Bit.value` to `4`.

### class BCD
This class takes a numerical value and converts it into BCD number representation. Each digit of the input value will be stored as a 4 bit nibble. This class supports 2 digit integers, and if something else is given as input, ValueError is raised. The BCD nibbles are stored as strings in a python array.

Example:
```python
bcd_num = BCD(25)
```
- Printing the object prints the array of BCD nibbles
  Example: `print(bcd_num)` → `['0010', '0101']`

- Each bit can be accessed using `obj[index]`.  
  Example: `bcd_num[1]` → `0101`

- Any bit can be reassigned using `obj[index] = value`; the internal `value` attribute is automatically updated.  (Input given as string)
  Example: `bcd_num[1] = 0` changes the nibble to `"0010"` and updates `bcd_num.value` to `22`.

### valid_width
This function takes the non negative integer value and positive width as input values and return True upon confirming that the given bits can be stored in the provided width measure.

Example
```python
valid_width(2,2)
```
for which the output will be `True`

```python
valid_width(2,1)
```
for which the output will be
`ValueError: Width_validation: The given bits can't be stored in the given width`

## gates.py
This is the file containing all the general gates (1 input and 2 input) which will be used further ahead in the project.

### NOT gate
It takes a single bit input and inverts it.
Example
```python
not_g(0)
```
#### Truth table:
`not_g(0)` → `1`
`not_g(1)` → `0`

### OR gate
It takes 2 bits as input and gives output high even if one of them is high
Example
```python
or_g(0,0)
```

#### Truth table
`or_g(0,0)` → `0`
`or_g(1,0)` → `1`
`or_g(0,1)` → `1`
`or_g(1,1)` → `1`

### AND gate
It takes 2 bits as input and gives output high only if both of them are high
Example
```python
and_g(0,0)
```

#### Truth table
`and_g(0,0)` → `0`
`and_g(1,0)` → `0`
`and_g(0,1)` → `0`
`and_g(1,1)` → `1`

### NAND gate
It takes 2 bits as input and gives inverted output of AND gate
Example
```python
nand_g(0,0)
```

#### Truth table
`nand_g(0,0)` → `1`
`nand_g(1,0)` → `1`
`nand_g(0,1)` → `1`
`nand_g(1,1)` → `0`

### NOR gate
It takes 2 bits as input and gives inverted output of OR gate
Example
```python
nor_g(0,0)
```

#### Truth table
`nor_g(0,0)` → `1`
`nor_g(1,0)` → `0`
`nor_g(0,1)` → `0`
`nor_g(1,1)` → `0`

#### XOR gate
It takes 2 bits as input and gives output of OR gate for unequal input and low for equal inputs
Example
```python
xor_g(0,0)
```

#### Truth table
`xor_g(0,0)` → `0`
`xor_g(1,0)` → `1`
`xor_g(0,1)` → `1`
`xor_g(1,1)` → `0`

### XNOR gate
It takes 2 bits as input and gives inverted output of XOR gate
Example
```python
xnor_g(0,0)
```

#### Truth table
`xnor_g(0,0)` → `1`
`xnor_g(1,0)` → `0`
`xnor_g(0,1)` → `0`
`xnor_g(1,1)` → `1`