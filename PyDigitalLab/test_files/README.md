# Test_Files
These are the files in which the code done in Logic_files is tested and confirmed as valid/correct. Each file tests different things

## test_gates.py
This file is responsible for test all the gates (not, or, and, nand, nor, xor, xnor) implemented in Logic_files/gates.py
It does so by using standard assert statements and using dictionaries present in the file to compare the truth table logic.
Run the file to use it.

## test_latch_and_FF.py
This file contains all exhaustive test cases used to test and validate the functioning and correctness of D_Latch and D_FF classes which are in latch_and_FF.py in Logic_files

### Test cases of D_Latch
#### Test case 1: Basic initialization truth table implementation
These test the dlatch created for all the initial possibilities of configurations.

#### Test case 2: Checking whether it preserves it's earlier value (Holding of D_Latch)
These test cases check whether Q changes if E is switched off, and hence checking the holding property.

#### Test case 3: Transparency of D_Latch when enabled.
These test cases check whether Q properly follows D during the stages where E is active.

### Test cases for D_FlipFlop
#### Test case 1: Initialization
This checks whether the initial initialization of D FF works as intended.

#### Test case 2: Reset condition:
This checks whether the reset instance methods works as intended.

#### Test case 3: D_FlipFlop example functioning
These give an example demonstration and general function of D FF

#### Test case 4: Showing D_FlipFlop only changes with change in clock
This is a distinction case between D latch and D FF. D latch has level-sensitive transparency, whereas D FF edge-triggered sampling. This checks that.

#### Test case 5: Showing in DFF only transition state matters
D latch follows D as long as E is active and hence before conditions matter, whereas D FF only transmits during transition so before conditions or changes doesnt effect it. This check that