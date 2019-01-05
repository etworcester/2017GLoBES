#!/usr/bin/env python

import os

explist = [300, 556, 984]
power = 1.07
mass = 40

params_no = "-p\'0.5857,0.148,0.726,0.0,0.000075,0.002524\' "
paramse_no = "-E\'0.023,0.018,0.0,0.0,0.024,0.016\' "

params_io = "-p\'0.5857,0.148,0.873,0.0,0.000075,-0.002439\' "
paramse_io = "-E\'0.023,0.018,0.0,0.0,0.024,0.016\' "


for exp in explist:

    years = exp/(power*2*mass)


    outfile = "data/octant_optimized_long_no_exp"+str(exp)
    call = "../cdr_testsetup/octant_fixth13 "+params_no+paramse_no+" dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call)

    outfile = "data/octant_optimized_long_io_exp"+str(exp)
    call = "../cdr_testsetup/octant_fixth13 "+params_io+paramse_io+" dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call)


