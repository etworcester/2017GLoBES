#!/usr/bin/env python

import os

params_no_dcp0 = "-p\'0.5857,0.148,0.726,0.0,0.000075,0.002524\' "
params_no_dcpneg = "-p\'0.5857,0.148,0.726,-1.570796,0.000075,0.002524\' "
params_no_dcppos = "-p\'0.5857,0.148,0.726,1.570796,0.000075,0.002524\' "

paramse_no = "-E\'0.023,0.0,0.058,0.0,0.024,0.016\' "

#Set up exposure scan

exps = [300, 556, 984]

mass = 40

#Set for each config because it depends on power:
for myexp in exps:
    years = myexp/(2*mass*1.07)

#Bubble, dcp0
    outfile = "data/bubble_optimized_long_dcp0_exp"+str(myexp)
    call = "../cdr_testsetup/mydth -c -X-1.5,-0.7 -Y-210,210 -R200,200 "+params_no_dcp0+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

#Bubble, dcp90
    outfile = "data/bubble_optimized_long_dcp90_exp"+str(myexp)
    call = "../cdr_testsetup/mydth -c -X-1.5,-0.7 -Y-210,210 -R200,200 "+params_no_dcppos+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

#Bubble, dcp-90
    outfile = "data/bubble_optimized_long_dcp-90_exp"+str(myexp)
    call = "../cdr_testsetup/mydth -c -X-1.5,-0.7 -Y-210,210 -R200,200 "+params_no_dcpneg+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 




