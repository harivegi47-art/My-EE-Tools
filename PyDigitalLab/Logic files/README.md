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

- Printing the object prints the underlying Python list.  
  Example: `print(Bit)` → `[0, 1, 0, 1]`

- Each bit can be accessed using `obj[index]`.  
  Example: `Bit[1]` → `1`

- Any bit can be reassigned using `obj[index] = value`; the internal `value` attribute is automatically updated.  
  Example: `Bit[3] = 0` changes the bit pattern to `[0, 1, 0, 0]` and updates `Bit.value` to `4`.