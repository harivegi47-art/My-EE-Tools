from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent/ "Logic_files"))
from latch_and_FF import D_latch, D_FF
from clock import clock
clk = clock()
#Test cases of D_Latch:

dlatch = D_latch()
#Test case 1: Basic initialization truth table implementation
dlatchlist1 = {(0,1):0, (1,1):1, (0,0):0, (1,0):0} # here Q is taken 0 for E = 0 because D_Latch in our project is initialized with 0
assert(dlatch.read() == 0), "D_Latch Test case failing at initialization."
for i in range(2):
    for j in range(2):
        dlatch.update(j,i)
        assert(dlatch.read() == dlatchlist1[(j,i)]), f"D_Latch Test case failing at D = {j} and E = {i}"
#Test case 1.1: Reset Verification
dlatch.update(1,1)
dlatch.reset()
assert(dlatch.read() == 0), "D_Latch Reset test case of D_Latch failing."

#Test case 2: Checking whether it preserves it's earlier value (Holding of D_Latch)
dlatch.update(1,1) #Assigning Q = 1
dlatch.update(0,0)
assert(dlatch.read() == 1), "D_Latch Test case failed for D = 0 and E = 0"
dlatch.update(1,0)
assert(dlatch.read() == 1), "D_Latch Test case failed for D = 1 and E = 0"
dlatch.update(0,1)
dlatch.update(0,0)
assert(dlatch.read() == 0), "D_Latch Test case failed for D = 0 and E = 0"
dlatch.update(1,0)
assert(dlatch.read() == 0), "D_Latch Test case failed for D = 1 and E = 0"
dlatch.reset()

#Test case 3: Transparency of D_Latch when enabled.
dlatch.update(1,1) #Test case 3.1
assert(dlatch.read() == 1), "D_Latch Test case failed at 3.1"
dlatch.update(0,1) #Test case 3.2
assert(dlatch.read() == 0), "D_Latch Test case failed at 3.2"
dlatch.update(1,1) #Test case 3.3
assert(dlatch.read() == 1), "D_Latch Test case failed at 3.3"


#Test cases for D_FlipFlop
dff = D_FF(clk)
#Test case 1: Initialization
assert(dff.read() == 0), "DFF test case failing at initialization"

#Test case 2: Reset condition:
dff.update(1)
clk.tick()
dff.update(1)
clk.tick()
assert(dff.read() == 1), "DFF Test case 2: assigning 1 failed"
dff.reset()
assert(dff.read() == 0), "DFF Test case 2: reset failed"

clk.reset()

#Test case 3: D_FlipFlop example functioning
dff.update(1)
clk.tick()
dff.update(1)
clk.tick()
assert(clk.tally == 2), "DFF Test case 3: clock tally is incorrect at assigning Q = 1"
assert(dff.read() == 1), "DFF Test case 3: failed to assign Q = 1"
dff.update(0)
clk.tick()
dff.update(0)
clk.tick()
assert(dff.read() == 0), "DFF Test case 3: failed to assign Q = 0"
dff.reset()
clk.reset()

#Test case 4: Showing D_FlipFlop only changes with change in clock
assert(dff.read() == 0), "DFF Test case 4: Failed initializing"
dff.update(1)
assert(dff.read() == 0), "DFF Test case 4: Q changing without clock changing"
dff.update(1)
assert(dff.read() == 0), "DFF Test case 4: Q changing without clock changing"
clk.tick()
dff.update(1)
dff.update(0)
assert(dff.read() == 1), "DFF Test case 4: Q changing without clock changing"
dff.update(0)
assert(dff.read() == 1), "DFF Test case 4: Q changing without clock changing"
dff.reset()
clk.reset()

#Test case 5: Showing in DFF only transition state matters
assert(dff.read() == 0), "DFF Test case 5: Failed initializing"
dff.update(0)
dff.update(0)
dff.update(1)
clk.tick()
dff.update(0)
assert(dff.read() == 1), "DFF Test case 5: Functioning improperly"
print("All test cases passed.")