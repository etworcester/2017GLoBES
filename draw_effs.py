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
ROOT.gStyle.SetTitleX(0.5)
ROOT.gStyle.SetTitleAlign(23)
ROOT.gStyle.SetLineWidth(3)
ROOT.gStyle.SetLineColor(1)
ROOT.gStyle.SetTitleSize(0.03,"t")

#Need these for any analysis
efflist_nue = ["app_FHC_nue_sig", "app_FHC_nuebar_sig", "app_FHC_nue_bkg", "app_FHC_nuebar_bkg", "app_FHC_numu_bkg", "app_FHC_numubar_bkg", "app_FHC_nutau_bkg", "app_FHC_nutaubar_bkg", "app_FHC_NC_bkg", "app_FHC_aNC_bkg"]

efflist_anue = ["app_RHC_nue_sig", "app_RHC_nuebar_sig", "app_RHC_nue_bkg", "app_RHC_nuebar_bkg", "app_RHC_numu_bkg", "app_RHC_numubar_bkg", "app_RHC_nutau_bkg", "app_RHC_nutaubar_bkg", "app_RHC_NC_bkg", "app_RHC_aNC_bkg"]

efflist_numu = ["dis_FHC_numu_sig", "dis_FHC_numubar_sig", "dis_FHC_nutau_bkg", "dis_FHC_nutaubar_bkg", "dis_FHC_NC_bkg", "dis_FHC_aNC_bkg"]

efflist_anumu = ["dis_RHC_numu_sig", "dis_RHC_numubar_sig", "dis_RHC_nutau_bkg", "dis_RHC_nutaubar_bkg", "dis_RHC_NC_bkg", "dis_RHC_aNC_bkg"]

efflist = efflist_nue + efflist_anue + efflist_numu + efflist_anumu

filelist = ["GLB_app_FHC_eff.dat", "GLB_app_RHC_eff.dat", "GLB_dis_FHC_eff.dat", "GLB_dis_RHC_eff.dat"]

postbins=array('d',[0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1, 1.125, 1.25, 1.375, 1.5, 1.625, 1.75, 1.875, 2, 2.125, 2.25, 2.375, 2.5, 2.625, 2.75, 2.875, 3, 3.125, 3.25, 3.375, 3.5, 3.625, 3.75, 3.875, 4, 4.125, 4.25, 4.375, 4.5, 4.625, 4.75, 4.875, 5, 5.125, 5.25, 5.375, 5.5, 5.625, 5.75, 5.875, 6, 6.125, 6.25, 6.375, 6.5, 6.625, 6.75, 6.875, 7, 7.125, 7.25, 7.375, 7.5, 7.625, 7.75, 7.875, 8, 9, 10, 12, 14, 16, 18, 20])
n = len(postbins)-1

hlist = []

for file in filelist:
    f = open("eff/BothCut/"+file,"r")
    for line in f.readlines():
        if line.strip():
            cols = line.split()
            vals = [c.strip(',') for c in cols if c[0].isdigit()]
            name = line.split()[0][6:]
            h = ROOT.TH1D("eff","eff",n,postbins)
            for i in range(0,n):
                h.SetBinContent(i,float(vals[i]))
                #print i, float(vals[i])
            h.SetNameTitle(name,name)
            hlist.append(h)

hout = ROOT.TFile("root/cdrglobes_effs.root","RECREATE")
for h in hlist:
    h.Write()
hout.Close()
