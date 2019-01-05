#!/usr/bin/env python

import sys
import math
import ROOT
from array import array

ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptFit()
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetTitleFillColor(0)
ROOT.gStyle.SetTitleBorderSize(0)
ROOT.gStyle.SetFrameBorderMode(0)
ROOT.gStyle.SetMarkerStyle(20)

dataname = sys.argv[1]

if ("dcp" in dataname):
    anatype = "noscale"
if ("th23" in dataname):
    anatype = "sinsq"
if ("th13" in dataname):
    anatype = "th13"
if ("dm" in dataname):
    anatype = "1e5"

explist = [1, 5, 10, 20, 28, 40, 50, 60, 70, 75, 80, 90, 100, 110, 125, 150, 175, 200, 225, 250, 275, 300, 350, 400, 556, 600, 800, 984, 1000, 1250, 1500]
uplist = []
downlist = []
reslist = []
minlist = []

for exp in explist:
    datafile = "data/"+dataname+"_exp"+str(exp)+".dat"
    f = open(datafile,'r')
    lines = f.readlines()

    par_list = []
    chi_list = []
    nsol = 0
    for line in lines:
        if (line[0] == '#'): continue
        if (len(line) == 0): continue
        if ((line[0] == '-') or (line[0] == '0') or (line[0] == '1')):
            if line[1] == '-':
                nsol += 1
                if nsol > 1:
                    break
            else:
                cols = line.split()
                if (float(cols[4]) > 0.00001):
                    par_list.append(float(cols[1]))
                    chi_list.append(float(cols[4]))


    minchi = min(chi_list)
    start = chi_list.index(minchi)
    minpar = par_list[start]
    minlist.append(minpar)

    #Scan up:
    i = 0
    nstep = len(chi_list) - start
    res = 9999.9
    resorig = abs(par_list[start+nstep-1]-par_list[start])
    print exp, start, nstep, par_list[start+nstep-1], par_list[start], resorig
    while i < nstep:
        thischi = chi_list[start+i]
        if thischi > 1.0:
            #Linear interpolation between points - probably ok for this
            thispar = par_list[start+i]
            lastpar = par_list[start+i-1]
            lastchi = chi_list[start+i-1]
            f = 1 - (thischi-1.0)/(thischi-lastchi)
            res =  abs(minpar - (lastpar + f*(thispar-lastpar)))
            uplist.append(res)
            break
        i += 1
    if (res == 9999.9):
        res = resorig
        uplist.append(res)

    #Scan down:
    i = 0
    res = 9999.9
    resorig = abs(par_list[start-nstep+1]-par_list[start])
    while i < start:
        thischi = chi_list[start-i]
        if thischi > 1.0:
            thispar = par_list[start-i]
            lastpar = par_list[start-i+1]
            lastchi = chi_list[start-i+1]
            f = 1 - (thischi-1.0)/(thischi-lastchi)
            res = abs(minpar - (lastpar - f*(lastpar-thispar)))
            downlist.append(res)
            break
        i += 1
    if (res == 9999.9):
        res = resorig
        downlist.append(res)

j = 0
while j < len(explist):
    res = 0.5*(uplist[j]+downlist[j])
    print explist[j], res
    mymin = minlist[j]
    if (anatype == "noscale"):
        resout = res
    elif (anatype == "sinsq"):
        resout = math.sin(mymin+res)*math.sin(mymin+res) - math.sin(mymin)*math.sin(mymin)
    elif (anatype == "th13"):
        resout = math.pow(10,mymin+res) - math.pow(10,mymin)
    elif (anatype == "1e5"):
        resout = 1e5*res
    else:
        print "Something is wrong!"
    reslist.append(resout)
    j += 1


n = len(explist)
explist = array('d',explist)
reslist = array('d',reslist)
resout = ROOT.TGraph(n,explist,reslist)
resout.SetName("Res")

outfile = "root/"+dataname+".root"
rootout = ROOT.TFile(outfile,"recreate")
resout.Write()
rootout.Close()

