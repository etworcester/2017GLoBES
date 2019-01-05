#!/usr/bin/env python

import sys
import math
import ROOT
from array import array

def filldiff(up,down):
  n = up.GetN()
  diffgraph = ROOT.TGraph(2*n);
  i = 0
  xup = ROOT.Double(-9.9)
  yup = ROOT.Double(-9.9)
  xlo = ROOT.Double(-9.9)
  ylo = ROOT.Double(-9.9)  
  while i<n:
    up.GetPoint(i,xup,yup);
    down.GetPoint(n-i-1,xlo,ylo);
    diffgraph.SetPoint(i,xup,yup);
    diffgraph.SetPoint(n+i,xlo,ylo);
    i += 1
  return diffgraph;

ROOT.gROOT.SetStyle("Plain")
ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptFit()
ROOT.gStyle.SetCanvasColor(0)
ROOT.gStyle.SetTitleFillColor(0)
ROOT.gStyle.SetTitleBorderSize(0)
ROOT.gStyle.SetFrameBorderMode(0)
ROOT.gStyle.SetMarkerStyle(20)

datafile = sys.argv[1]
#notes = sys.argv[2]
notes = ""

f = open(datafile,'r')
lines = f.readlines()

limit90 = 2.71
limit3sig = 9
limit5sig = 25

first = 1
count90_nh = 0
count90_both = 0
count3sig_nh = 0
count3sig_ih = 0
count3sig_both = 0
count5sig_both = 0
count5sig_nh = 0
count5sig_ih = 0
count_total = 0
chi2min = 1000.
chi2min_ih = 1000.
chi2min_nh = 1000.
chi2max = 0.
chi2max_ih = 0.
chi2max_nh = 0.

th23vals = []
chi2vals = []
frac90 = []
frac3sig = []
frac5sig = []
frac3sig_nh = []
frac3sig_ih = []
frac5sig_nh = []
frac5sig_ih = []
chi2maxvals = []
chi2minvals = []
chi2maxvals_ih = []
chi2minvals_ih = []
chi2maxvals_nh = []
chi2minvals_nh = []
chi2_10 = []
chi2_90 = []

for line in lines:
    if line[0:3] == 'nom':
        cols = line.split()
        th23 = float(cols[1])*180/math.pi
        chi2_nh = float(cols[3])
        chi2_ih = float(cols[4])
        chi2_both = min(chi2_nh,chi2_ih)
        if first:
            th23_current = th23
            first = 0
            thischi2list = []
        if (th23 != th23_current):
            #Write out old stuff
            print th23_current, count5sig_both, count5sig_nh, count5sig_ih
            th23vals.append(th23_current)
            chi2vals.append(thischi2list)
            frac90.append(float(count90_both)/count_total)
            frac3sig.append(float(count3sig_both)/count_total)
            frac5sig.append(float(count5sig_both)/count_total)
            frac3sig_nh.append(float(count3sig_nh)/count_total)
            frac3sig_ih.append(float(count3sig_ih)/count_total)
            frac5sig_nh.append(float(count5sig_nh)/count_total)
            frac5sig_ih.append(float(count5sig_ih)/count_total)            
            chi2maxvals.append(chi2max)
            chi2minvals.append(chi2min)
            chi2maxvals_ih.append(chi2max_ih)
            chi2minvals_ih.append(chi2min_ih)
            chi2maxvals_nh.append(chi2max_nh)
            chi2minvals_nh.append(chi2min_nh)
            count90_nh = 0
            count90_both = 0
            count3sig_nh = 0
            count3sig_ih = 0
            count3sig_both = 0
            count5sig_both = 0
            count5sig_nh = 0
            count5sig_ih = 0
            chi2min = 1000.
            chi2min_ih = 1000.
            chi2min_nh = 1000.
            chi2max = 0.
            chi2max_ih = 0.
            chi2max_nh = 0.
            count_total = 0
            th23_current = th23
            thischi2list = []
        if (th23 == th23_current):
            if (chi2_nh > limit90):
                count90_nh += 1
            if (chi2_both > limit90):
                count90_both += 1
            if (chi2_nh > limit3sig):
                count3sig_nh += 1
            if (chi2_ih > limit3sig):
                count3sig_ih += 1                
            if (chi2_both > limit3sig):
                count3sig_both += 1
            if (chi2_nh > limit5sig):
                count5sig_nh += 1
            if (chi2_ih > limit5sig):
                count5sig_ih += 1                
            if (chi2_both > limit5sig):
                count5sig_both += 1
            count_total += 1
            if (chi2_both < chi2min):
                chi2min = chi2_both
            if (chi2_both > chi2max):
                chi2max = chi2_both
            if (chi2_ih < chi2min_ih):
                chi2min_ih = chi2_ih
            if (chi2_ih > chi2max_ih):
                chi2max_ih = chi2_ih
            if (chi2_nh < chi2min_nh):
                chi2min_nh = chi2_nh
            if (chi2_nh > chi2max_nh):
                chi2max_nh = chi2_nh                               
            thischi2list.append(chi2_both)
#Write out last line
print th23_current, count5sig_both, count5sig_nh, count5sig_ih
th23vals.append(th23_current)
chi2vals.append(thischi2list)
frac90.append(count90_both/count_total)
frac3sig.append(count3sig_both/count_total)
frac5sig.append(count5sig_both/count_total)
frac3sig_nh.append(float(count3sig_nh)/count_total)
frac3sig_ih.append(float(count3sig_ih)/count_total)
frac5sig_nh.append(float(count5sig_nh)/count_total)
frac5sig_ih.append(float(count5sig_ih)/count_total)            
chi2maxvals.append(chi2max)
chi2minvals.append(chi2min)
chi2maxvals_ih.append(chi2max_ih)
chi2minvals_ih.append(chi2min_ih)
chi2maxvals_nh.append(chi2max_nh)
chi2minvals_nh.append(chi2min_nh)

i = 0
for chi2list in chi2vals:
  chi2sorted = sorted(chi2list)
  nchi2 = len(chi2list)
  p1 = int(0.1*nchi2)
  p2 = int (0.9*nchi2)
#  print th23vals[i], nchi2, p1, p2, chi2sorted[p1], chi2sorted[p2] 
  chi2_10.append(chi2sorted[p1])
  chi2_90.append(chi2sorted[p2])
  i+=1
                 
n = len(th23vals)
th23vals = array('f',th23vals)
frac90 = array('f',frac90)
frac3sig = array('f',frac3sig)
frac5sig = array('f',frac5sig)
frac3sig_nh = array('f',frac3sig_nh)
frac3sig_ih = array('f',frac3sig_ih)
frac5sig_nh = array('f',frac5sig_nh)
frac5sig_ih = array('f',frac5sig_ih)
chi2maxvals = array('f',chi2maxvals)
chi2minvals = array('f',chi2minvals)
chi2maxvals_ih = array('f',chi2maxvals_ih)
chi2minvals_ih = array('f',chi2minvals_ih)
chi2maxvals_nh = array('f',chi2maxvals_nh)
chi2minvals_nh = array('f',chi2minvals_nh)
chi2_10 = array('f',chi2_10)
chi2_90 = array('f',chi2_90)

graph90 = ROOT.TGraph(n,th23vals,frac90)
graph3sig = ROOT.TGraph(n,th23vals,frac3sig)
graph5sig = ROOT.TGraph(n,th23vals,frac5sig)
graph3sig_nh = ROOT.TGraph(n,th23vals,frac3sig_nh)
graph3sig_ih = ROOT.TGraph(n,th23vals,frac3sig_ih)
graph5sig_nh = ROOT.TGraph(n,th23vals,frac5sig_nh)
graph5sig_ih = ROOT.TGraph(n,th23vals,frac5sig_ih)
graph_chi2max = ROOT.TGraph(n,th23vals,chi2maxvals)
graph_chi2min = ROOT.TGraph(n,th23vals,chi2minvals)
graph_chi2max_ih = ROOT.TGraph(n,th23vals,chi2maxvals_ih)
graph_chi2min_ih = ROOT.TGraph(n,th23vals,chi2minvals_ih)
graph_chi2max_nh = ROOT.TGraph(n,th23vals,chi2maxvals_nh)
graph_chi2min_nh = ROOT.TGraph(n,th23vals,chi2minvals_nh)
graph_chi210 = ROOT.TGraph(n,th23vals,chi2_10)
graph_chi290 = ROOT.TGraph(n,th23vals,chi2_90)

graph_chi2range = filldiff(graph_chi2max,graph_chi2min)
graph_chi2range_ih = filldiff(graph_chi2max_ih,graph_chi2min_ih)
graph_chi2range_nh = filldiff(graph_chi2max_nh,graph_chi2min_nh)
graph_chi2range1090 = filldiff(graph_chi290,graph_chi210)

c1 = ROOT.TCanvas("c1","c1",800,800)
h1 = c1.DrawFrame(34.99, 0.0, 55.01, 1.0)
h1.SetTitle("Octant Sensitivity")
h1.GetXaxis().SetTitle("true #theta_{23} [#circ]")
h1.GetXaxis().SetTitleSize(0.03)
h1.GetXaxis().SetLabelSize(0.02)
h1.GetYaxis().SetTitle("Fraction of #delta_{CP} values")
h1.GetYaxis().SetTitleSize(0.03)
h1.GetYaxis().SetLabelSize(0.02)

graph90.SetLineColor(3)
graph90.SetLineWidth(3)
graph90.Draw("Lsame")
#graph90.Print()

graph3sig.SetLineColor(4)
graph3sig.SetLineWidth(3)
graph3sig.Draw("Lsame")
#graph3sig.Print()

graph5sig.SetLineColor(6)
graph5sig.SetLineWidth(3)
graph5sig.Draw("Lsame")
#graph5sig.Print()

l1 = ROOT.TLegend(0.11,0.79,0.3,0.89)
l1.AddEntry(graph90, "90% CL", "l")
l1.AddEntry(graph3sig, "3#sigma CL","l")
l1.AddEntry(graph5sig, "5#sigma CL","l")
l1.SetFillColor(0)
l1.SetBorderSize(0)
l1.Draw("same")

t1 = ROOT.TPaveText(0.11,0.4,0.3,0.7,"NDC")
t1.AddText("Octant is determined for")
t1.AddText("fraction of #delta_{CP} values shown")
t1.SetTextAlign(12)
t1.SetFillColor(0)
t1.SetBorderSize(0)
#t1.Draw("same")

#outname = label+".eps"
#c1.SaveAs(outname)
    
c2 = ROOT.TCanvas("c2","c2",800,800)
h2 = c2.DrawFrame(34.99, 0.0, 55.01, 60.0)
h2.SetTitle("Octant Sensitivity")
h2.GetXaxis().SetTitle("true #theta_{23} [#circ]")
h2.GetXaxis().SetTitleSize(0.03)
h2.GetXaxis().SetLabelSize(0.02)
h2.GetYaxis().SetTitle("#Delta#chi^{2}")
h2.GetYaxis().SetTitleSize(0.03)
h2.GetYaxis().SetLabelSize(0.02)

t2 = ROOT.TPaveText(0.11,0.8,0.7,0.89,"NDC")
t2.AddText(notes)
t2.AddText("With of band is due to the unknown CP phase")
t2.SetFillColor(0)
t2.SetBorderSize(0)
t2.SetTextAlign(12)
t2.Draw()

graph_chi2range_nh.SetFillColor(2)
graph_chi2range_nh.Draw("Fsame")
graph_chi2max_nh.Draw("same")
graph_chi2min_nh.Draw("same")

graph_chi2range_ih.SetFillColor(4)
graph_chi2range_ih.Draw("Fsame")
graph_chi2max_ih.Draw("same")
graph_chi2min_ih.Draw("same")

graph_chi2range.SetFillColor(3)
graph_chi2range.Draw("Fsame")
graph_chi2max.Draw("same")
graph_chi2min.Draw("same")

leg1 = ROOT.TLegend(0.4,0.6,0.6,0.7)
leg1.AddEntry(graph_chi2range, "Both Hierarchies", "F")
leg1.AddEntry(graph_chi2range_nh, "NH", "F")
leg1.AddEntry(graph_chi2range_ih, "IH", "F")
leg1.SetFillColor(0)
leg1.SetBorderSize(0)
leg1.Draw("same")

l1 = ROOT.TLine(35.0,9.,55.0,9.0)
l1.SetLineWidth(3)
l1.SetLineStyle(2)
l1.Draw()

l2 = ROOT.TLine(35.0,25.,55.0,25.0)
l2.SetLineWidth(3)
l2.SetLineStyle(2)
l2.Draw()

t3sig = ROOT.TPaveText(36,9.2,37,12)
t3sig.AddText("3#sigma")
t3sig.SetFillColor(0)
t3sig.SetBorderSize(0)
t3sig.Draw()

t5sig = ROOT.TPaveText(36,25.2,37,28)
t5sig.AddText("5#sigma")
t5sig.SetFillColor(0)
t5sig.SetBorderSize(0)
t5sig.Draw()

graph_chi2range.SetName("chi2range")
graph_chi2range1090.SetName("chi2_10to90")
graph_chi2min.SetName("chi2min")
graph3sig.SetName("threesigma_both")
graph3sig_nh.SetName("threesigma_nh")
graph3sig_ih.SetName("threesigma_ih")
graph5sig.SetName("fivesigma_both")
graph5sig_nh.SetName("fivesigma_nh")
graph5sig_ih.SetName("fivesigma_ih")
label = datafile[5:]
label = label.strip(".dat")
outfile = "root/sens_"+label+".root"
f1 = ROOT.TFile(outfile,"RECREATE")
graph_chi2range.Write()
graph_chi2range1090.Write()
graph_chi2min.Write()
graph3sig.Write()
graph3sig_nh.Write()
graph3sig_ih.Write()
graph5sig.Write()
graph5sig_nh.Write()
graph5sig_ih.Write()
f1.Close()




    
