from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent/ "Logic_files"))
import gates
notlist = {0:1, 1:0}
andlist = {(0,0):0, (0,1):0, (1,0):0, (1,1):1}
orlist = {(0,0):0, (0,1):1, (1,0):1, (1,1):1}
nandlist = {(0,0):1, (0,1):1, (1,0):1, (1,1):0}
norlist = {(0,0):1, (0,1):0, (1,0):0, (1,1):0}
xorlist = {(0,0):0, (0,1):1, (1,0):1, (1,1):0}
xnorlist = {(0,0):1, (0,1):0, (1,0):0, (1,1):1}
print("Testing all gates:") #Run the code to test
for i in range(2): #NOT gate
    assert gates.not_g(i) == notlist[i], f"Testing failed at NOT gate input {i}"

for i in range(2): #AND gate
    for j in range(2): 
        assert gates.and_g(i,j) == andlist[(i,j)], f"Testing failed at AND gate input ({i},{j})"

for i in range(2): #OR gate
    for j in range(2): 
        assert gates.or_g(i,j) == orlist[(i,j)], f"Testing failed at OR gate input ({i},{j})"

for i in range(2): #NAND gate
    for j in range(2): 
        assert gates.nand_g(i,j) == nandlist[(i,j)], f"Testing failed at NAND gate input ({i},{j})"

for i in range(2): #NOR gate
    for j in range(2): 
        assert gates.nor_g(i,j) == norlist[(i,j)], f"Testing failed at NOR gate input ({i},{j})"

for i in range(2): #XOR gate
    for j in range(2): 
        assert gates.xor_g(i,j) == xorlist[(i,j)], f"Testing failed at XOR gate input ({i},{j})"

for i in range(2): #XNOR gate
    for j in range(2): 
        assert gates.xnor_g(i,j) == xnorlist[(i,j)], f"Testing failed at XNOR gate input ({i},{j})"
print("All gates are giving intended outputs")