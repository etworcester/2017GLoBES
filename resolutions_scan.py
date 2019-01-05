#!/usr/bin/env python

import os
import math

#Set up exposure scan

#myexps = [1, 5, 10, 28, 50, 100, 200, 300, 400, 556, 600, 800, 984, 1000, 1250, 1500]
#myexps = [75, 150, 250, 350]
#myexps = [20, 40, 60, 70, 80]
myexps = [90, 110, 125, 175, 225, 275]

#Scale the power
power60 = 1.03
power80 = 1.07
power120 = 1.2

mass = 40

params_no = "-p\'0.5857,0.148,0.726,0.0,0.000075,0.002524\' "
paramse_no = "-E\'0.023,0.018,0.058,0.0,0.024,0.016\' "
params_no_first = "-p\'0.5857,0.148,0.726,"
params_no_last = ",0.000075,0.002524\' "

params_io = "-p\'0.5857,0.148,0.873,0.0,0.000075,-0.002439\' "
paramse_io = "-E\'0.023,0.018,0.048,0.0,0.024,0.016\' "

paramse_noconstr = "-E\'0.023,0.0,0.0,0.0,0.024,0.0\' "

params_no_q23lo = "-p\'0.5857,0.148,0.693,0.0,0.000075,0.002524\' "
params_no_q23lo_first = "-p\'0.5857,0.148,0.693,"
params_no_q23hi = "-p\'0.5857,0.148,0.785,0.0,0.000075,0.002524\' "
params_no_q23hi_first = "-p\'0.5857,0.148,0.785"

params_io_q23lo = "-p\'0.5857,0.148,0.838,0.0,0.000075,-0.002439\' "
params_io_q23hi = "-p\'0.5857,0.148,0.900,0.0,0.000075,-0.002439\' "

#Set for each config because it depends on power:
power = power80
for myexp in myexps:
    years = myexp/(power*2*mass)


#Nominal Delta CP resolution, dcp 0
    outfile = "data/resdcp0_optimized_long_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-100,100 -R200 "+params_no+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp0_optimized_long_no_noconstr_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-100,100 -R200 "+params_no+paramse_noconstr+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp0_optimized_long_q23lo_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-100,100 -R200 "+params_no_q23lo+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp0_optimized_long_q23hi_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-100,100 -R200 "+params_no_q23hi+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

#Syst 3pc Delta CP resolution, dcp 0
    outfile = "data/resdcp0_optimized_long_syst3pc_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-100,100 -R200 "+params_no+paramse_no+" -F dune_optimized_long_syst3pc.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp0_optimized_long_syst3pc_no_noconstr_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-100,100 -R200 "+params_no+paramse_noconstr+" -F dune_optimized_long_syst3pc.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp0_optimized_long_q23lo_syst3pc_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-100,100 -R200 "+params_no_q23lo+paramse_no+" -F dune_optimized_long_syst3pc.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp0_optimized_long_q23hi_syst3pc_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-100,100 -R200 "+params_no_q23hi+paramse_no+" -F dune_optimized_long_syst3pc.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

#Nominal Delta CP resolution, dcp 90
    outfile = "data/resdcp90_optimized_long_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-10,190 -R200 "+params_no_first+"1.570796"+params_no_last+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp90_optimized_long_no_noconstr_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-10,190 -R200 "+params_no_first+"1.570796"+params_no_last+paramse_noconstr+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp90_optimized_long_q23lo_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-10,190 -R200 "+params_no_q23lo_first+"1.570796"+params_no_last+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp90_optimized_long_q23hi_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-10,190 -R200 "+params_no_q23hi_first+"1.570796"+params_no_last+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

#Nominal Delta CP resolution, dcp -90
    outfile = "data/resdcp-90_optimized_long_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-190,10 -R200 "+params_no_first+"-1.570796"+params_no_last+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp-90_optimized_long_no_noconstr_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-190,10 -R200 "+params_no_first+"-1.570796"+params_no_last+paramse_noconstr+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp-90_optimized_long_q23lo_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-190,10 -R200 "+params_no_q23lo_first+"-1.570796"+params_no_last+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp-90_optimized_long_q23hi_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-190,10 -R200 "+params_no_q23hi_first+"-1.570796"+params_no_last+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 


#Syst3pc Delta CP resolution, dcp -90
    outfile = "data/resdcp-90_optimized_long_syst3pc_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-190,10 -R200 "+params_no_first+"-1.570796"+params_no_last+paramse_no+" -F dune_optimized_long_syst3pc.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp-90_optimized_long_syst3pc_no_noconstr_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-190,10 -R200 "+params_no_first+"-1.570796"+params_no_last+paramse_noconstr+" -F dune_optimized_long_syst3pc.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp-90_optimized_long_q23lo_syst3pc_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-190,10 -R200 "+params_no_q23lo_first+"-1.570796"+params_no_last+paramse_no+" -F dune_optimized_long_syst3pc.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

    outfile = "data/resdcp-90_optimized_long_q23hi_syst3pc_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A3 -X-190,10 -R200 "+params_no_q23hi_first+"-1.570796"+params_no_last+paramse_no+" -F dune_optimized_long_syst3pc.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    print call
    os.system(call) 

#Nominal th23 resolution, dcp0

    outfile = "data/resth23_optimized_long_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A2 -S0.2 -R200 "+params_no+" -E\'0.023,0.018,0.0,0.0,0.024,0.016\' -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    #print call
    #os.system(call) 

    outfile = "data/resth23_optimized_long_no_noconstr_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A2 -S0.2 -R200 "+params_no+paramse_noconstr+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    #print call
    #os.system(call) 

    outfile = "data/resth23_optimized_long_q23lo_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A2 -S0.2 -R200 "+params_no_q23lo+" -E\'0.023,0.018,0.0,0.0,0.024,0.016\' -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    #print call
    #os.system(call) 

    outfile = "data/resth23_optimized_long_q23hi_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A2 -S0.2 -R200 "+params_no_q23hi+" -E\'0.023,0.018,0.0,0.0,0.024,0.016\' -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    #print call
    #os.system(call) 

#Nominal th13 resolution, dcp=0

    outfile = "data/resth13_optimized_long_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A1 -X-1.5,-0.7 -R200 "+params_no+ " -E\'0.023,0.0,0.058,0.0,0.024,0.016\' -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    #print call
    #os.system(call) 

    outfile = "data/resth13_optimized_long_no_noconstr_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A1 -X-1.5,-0.7 -R200 "+params_no+paramse_noconstr+ " -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    #print call
    #os.system(call) 

    outfile = "data/resth13_optimized_long_q23lo_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A1 -X-1.5,-0.7 -R200 "+params_no_q23lo+ " -E\'0.023,0.0,0.058,0.0,0.024,0.016\' -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    #print call
    #os.system(call) 

    outfile = "data/resth13_optimized_long_q23hi_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A1 -X-1.5,-0.7 -R200 "+params_no_q23hi+ " -E\'0.023,0.0,0.058,0.0,0.024,0.016\' -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    #print call
    #os.system(call) 


# Nominal dmsq resolution, dcp=0

    outfile = "data/resdm_optimized_long_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A5 -S1.2e-4 -R200 "+params_no+" -E\'0.023,0.018,0.058,0.0,0.024,0.0\' -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    #print call
    #os.system(call) 

    outfile = "data/resdm_optimized_long_no_noconstr_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A5 -S1.2e-4 -R200 "+params_no+paramse_no+" -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    #print call
    #os.system(call) 

    outfile = "data/resdm_optimized_long_q23lo_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A5 -S1.2e-4 -R200 "+params_no_q23lo+" -E\'0.023,0.018,0.058,0.0,0.024,0.0\' -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    #print call
    #os.system(call) 

    outfile = "data/resdm_optimized_long_q23hi_no_exp"+str(myexp)
    call = "../cdr_testsetup/myacc -A5 -S1.2e-4 -R200 "+params_no_q23hi+" -E\'0.023,0.018,0.058,0.0,0.024,0.0\' -F dune_optimized_long.glb -d 0.02 -DNUTIME="+str(years)+" -DNUBARTIME="+str(years)+" "+outfile+" &"
    #print call
    #os.system(call) 
