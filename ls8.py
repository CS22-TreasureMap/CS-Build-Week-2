#!/usr/bin/env python3

"""Main."""

import sys
from cpu2 import *

def run_ls8():

    cpu = CPU()

    cpu.load('hinter.ls8')
    cpu.run()

# cpu = CPU()

# cpu.load('hinter2.ls8')
# cpu.run()

# run_ls8()