#!/usr/bin/env python

import os
import sys
import math
import ROOT
from array import array

param1 = sys.argv[1]

file_no = "v30.release-data-NO.txt"
file_io = "v30.release-data-IO.txt"
filelist = [file_no, file_io]
#filelist = [file_no]

if (param1 == "dcpvq13"):
    searchstring = "# T13/DCP projection"

filenum = 0
for myfile in filelist:
    filenum += 1
    dcp = []
    s22th13 = []
    chi2 = []
    xbins = []
    ybins = []

    lfirst = True

    f = open(myfile)
    for line in f.readlines():
        if (lfirst and searchstring not in line):
            continue
        else:
            if lfirst:
                lfirst = False
                continue
        if not line.strip():
            break
        vals = line.split()
        th13val = float(vals[0])
        dcpval = float(vals[1])
        chi2val = float(vals[2])
        dcp.append(dcpval)
        myth13val = math.sin(2*math.asin(math.sqrt(th13val)))*math.sin(2*math.asin(math.sqrt(th13val)))
        s22th13.append(myth13val)
        chi2.append(chi2val)
        if (th13val==0.0):
            ybins.append(dcpval-2.5)
        if (dcpval==-180.):
            xbins.append(myth13val-0.0001)
        if (myth13val > 0.071 and myth13val < 0.076):
            print th13val, myth13val, chi2val

    xbins.append(myth13val+0.001)
    ybins.append(dcpval+2.5)            
    n = len(dcp)        
    nx = len(xbins)-1
    ny = len(ybins)-1
    xbins = array('d', xbins)
    ybins = array('d', ybins)
    if (filenum == 1):
        h_no = ROOT.TH2D("h_no","dcpvs22th13", ny, ybins, nx, xbins)
    elif (filenum == 2):
        h_io = ROOT.TH2D("h_io","dcpvs22th13", ny, ybins, nx, xbins)
        
    i=0
    while i<n:
        if (filenum == 1):
            h_no.Fill(dcp[i],s22th13[i],chi2[i])
        elif (filenum == 2):
            h_io.Fill(dcp[i],s22th13[i],chi2[i])
        i += 1

outfile = "root/nufit_dcpvq13_contours_rotate.root"
fout = ROOT.TFile(outfile,"RECREATE")
h_no.Write()
h_io.Write()
fout.Close()


