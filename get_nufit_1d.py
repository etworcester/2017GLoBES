#!/usr/bin/env python

import os
import sys

param = sys.argv[1]
chi2 = float(sys.argv[2])

file_no = "v30.release-data-NO.txt"
file_io = "v30.release-data-IO.txt"
filelist = [file_no, file_io]

if (param == "q23"):
    searchstring = "# T23 projection"

for myfile in filelist:
    f = open(myfile)
    lfirst = True
    lower = True
    th23val = 99.99
    chi2val = -99.99
    for line in f.readlines():
        if (lfirst and searchstring not in line):
            continue
        else:
            if lfirst:
                lfirst = False
                continue
            th23last = th23val
            chi2last = chi2val
            vals = line.split()
            th23val = float(vals[0])
            chi2val = float(vals[1])
            #print line
            if lower:
                if (chi2val < chi2):
                    frac = (chi2last-chi2)/(chi2last-chi2val)
                    myth23lo = frac*(th23val-th23last) + th23last
                    lower = False
                    #print "Found lower crossing"
                    #print myth23lo
            else:
                if (chi2val > chi2):
                    frac = (chi2last-chi2)/(chi2last-chi2val)
                    myth23hi = -1*frac*(th23last-th23val) + th23last
                    #print "Found upper crossing"
                    #print myth23hi
                    break

    print "Parameter (for critical value of "+str(chi2)+") is in range: "+str(myth23lo)+" : "+str(myth23hi)
                
            
        
        
