#!/usr/bin/env python

import sys
import shutil
import os
import itertools
from utils import *

##################

# - Grid of `shat` and `f`
shat_list = linspace(500, 10000, 2)
f_list    = linspace(750.0, 2000.0, 2)

tag  = sys.argv[1]
comp = sys.argv[2]



prog = './mg5_driver.py'


#################################################################

for shat, f in itertools.product(shat_list, f_list):

    cmd = '{} {} {} {} {}'.format(prog, tag, comp, shat, f)
    os.system(cmd)
