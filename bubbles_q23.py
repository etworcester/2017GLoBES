#!/usr/bin/env python

import os

params_no_first = " -p\'0.5857,0.148,"
params_no_last = ",0.000075,0.002524\'"
paramse_no = "-E\'0.023,0.018,0.0,0.0,0.024,0.016\' "

#Set up exposure scan

myexps = [300, 556, 984]

mass = 40

dcpvals = [-1.570796, 0, 1.570796]
q23vals = [0.670,0.7261,0.785,0.922]
dcptext = ["dcp-90","dcp0","dcp+90"]
q23text = ["q23lo", "q23nom", "q23max", "q23hi"]

#Set for each config because it depends on power:
for myexp in myexps:
    years = myexp/(1.07*mass*2)

    dcpcount = 0
    for dcp in dcpvals:
        q23count = 0
        for q23 in q23vals:
            outfile = "data/bubble_q23_optimized_long_"+dcptext[dcpcount]+"_"+q23text[q23count]+"_exp"+str(myexp)
            call = "../cdr_testsetup/mydth -c -B -X30,60 -Y-210,210 -R200,200"+params_no_first+str(q23)+","+str(dcp)+params_no_last+" -E\'0.023,0.025,0.0,0.0,0.024,0.020\' -d0.02 -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
            print call
            os.system(call)

            q23count += 1
        dcpcount += 1
        



