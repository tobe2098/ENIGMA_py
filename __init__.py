import core
import cli
import gui

## IMPORTANT TO SET TIMEOUTS IN ALL FILE I/O
## ADD MAx DEPTH for recursive calls
## Add configuration of bools for safety and clarity screen clearance, MAX NOTCHES (configuration.something?)
# Move constants somewhere that is not utils? If I can make them static somehow (or constants.py file)
# Introduce Type_sth class for string printing? Lowecase, uppercase, plural and singular.
# Move all annotations here
# Just put the typename in all permutations as member variables, so a call to the ref will be easy (maybe as functions?)
# Do type checking before encryption
# Add waiting when clearing the screen
# Put exceptions for every core function that manipulates the objects. ARGUMENT CHECKING SHOULD BE A SINGLE FUNCTION INSIDE THE CORE

if __name__ == "__main__":
    import sys

    # Extract args
    # Run client or gui
