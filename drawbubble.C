#include<iostream>
#include <TH2.h>
#include <TGraph.h>
void makeplot(TString exp) {

  gStyle->SetOptStat(0);
  gStyle->SetCanvasColor(0);
  gStyle->SetTitleFillColor(0);
  gStyle->SetTitleBorderSize(0);
  gStyle->SetFrameBorderMode(0);
  gStyle->SetTitleX(0.1f);
  gStyle->SetTitleY(.97f);


  TString filename = "chi2maps_Bubbles_exp";
  filename += exp;
  filename += ".root";
  TFile *f = new TFile(filename);
  TH2D *idcp01sig = (TH2D*)f->Get("Chi2Map_0");
  TH2D *idcppos1sig = (TH2D*)f->Get("Chi2Map_1");
  TH2D *idcpneg1sig = (TH2D*)f->Get("Chi2Map_2");

  int nbinsx = idcp01sig->GetNbinsX();
  double xwidth = idcp01sig->GetBinWidth(1);
  double lox = idcp01sig->GetBinLowEdge(1);
  double hix = idcp01sig->GetBinLowEdge(nbinsx) + xwidth;
  double newlo = pow(10,lox);
  double newhi = pow(10,hix);

  int nbinsy = idcp01sig->GetNbinsY();
  double ywidth = idcp01sig->GetYaxis()->GetBinWidth(1);
  double loy = idcp01sig->GetYaxis()->GetBinLowEdge(1);
  double hiy = idcp01sig->GetYaxis()->GetBinLowEdge(nbinsy) + ywidth;

  const int nx = nbinsx + 1;
  double bounds[nx];
  bounds[0] = newlo;
  for (int xbin=0; xbin<nbinsx; ++xbin) {
    double thislox = idcp01sig->GetBinLowEdge(xbin);
    double thishix = thislox + xwidth;
    double bound = pow(10,thishix);
    bounds[xbin+1] = bound;
    cout << xbin << " " << thislox << " " << thishix << " " << bound << endl;
  } 


  TH2D *dcp01sig = new TH2D("dcp01sig","dcp01sig",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *dcppos1sig = new TH2D("dcppos1sig","dcppos1sig",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *dcpneg1sig = new TH2D("dcpneg1sig","dcpneg1sig",nbinsx,bounds,nbinsy,loy,hiy);

  fillit(nbinsx,nbinsy,idcp01sig,dcp01sig);
  fillit(nbinsx,nbinsy,idcppos1sig,dcppos1sig);
  fillit(nbinsx,nbinsy,idcpneg1sig,dcpneg1sig);

  TString outfile = "root/Bubbles_exp";
  outfile += exp;
  outfile += ".root";
  TFile *out = new TFile(outfile,"recreate");
  dcp01sig->Write();
  dcppos1sig->Write();
  dcpneg1sig->Write();
  out->Close();
}

void plotit(TH2D *myhist, Color_t color, double cont) {
  myhist->SetContour(1);
  myhist->SetContourLevel(0,cont);
  myhist->SetLineWidth(2);
  myhist->SetLineColor(color);
  myhist->Draw("cont3 same");
}

void fillit(int nbinsx, int nbinsy, TH2D *myhist, TH2D *mynewhist) {
  for (int xbin=0; xbin < nbinsx+2; ++xbin) {
    double xval = myhist->GetXaxis()->GetBinCenter(xbin);
    double newxval = pow(10,xval);
    for (int ybin=0; ybin < nbinsy+2; ++ ybin) {
      double yval = myhist->GetYaxis()->GetBinCenter(ybin);
      double bincontent = myhist->GetBinContent(xbin,ybin);
      mynewhist->Fill(newxval,yval,bincontent);
    }
  }
}


