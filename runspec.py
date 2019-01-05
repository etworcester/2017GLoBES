#!/usr/bin/env python

#556 kt-mW-years = 10 years staged

import os
import math

years = 6.5

mass = 40

params_no = "-p\'0.5857,0.148,0.726,0.0,0.000075,0.002524\' "

params_io = "-p\'0.5857,0.148,0.873,0.0,0.000075,-0.002439\' "

#Normal Ordering
outfile = "data/spec_nu_no_5years.dat"
call = "globes -s "+params_no+" dune_optimized_long.glb -DNUTIME="+str(years)+" -DNUBARTIME=0 > "+outfile
print call
os.system(call) 

outfile = "data/spec_anu_no_5years.dat"
call = "globes -s "+params_no+" dune_optimized_long.glb -DNUBARTIME="+str(years)+" -DNUTIME=0 > "+outfile
print call
os.system(call) 

