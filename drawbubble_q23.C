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

  const double pi = 3.1415926535897;

  TString filename = "root/chi2maps_Bubbles_q23_exp";
  filename+=exp;
  filename+=".root";
  TFile *f = new TFile(filename);
  TH2D *Chi2Map_0 = (TH2D*)f->Get("Chi2Map_0");
  TH2D *Chi2Map_1 = (TH2D*)f->Get("Chi2Map_1");
  TH2D *Chi2Map_2 = (TH2D*)f->Get("Chi2Map_2");
  TH2D *Chi2Map_3 = (TH2D*)f->Get("Chi2Map_3");
  TH2D *Chi2Map_4 = (TH2D*)f->Get("Chi2Map_4");
  TH2D *Chi2Map_5 = (TH2D*)f->Get("Chi2Map_5");
  TH2D *Chi2Map_6 = (TH2D*)f->Get("Chi2Map_6");
  TH2D *Chi2Map_7 = (TH2D*)f->Get("Chi2Map_7");
  TH2D *Chi2Map_8 = (TH2D*)f->Get("Chi2Map_8");
  TH2D *Chi2Map_9 = (TH2D*)f->Get("Chi2Map_9");
  TH2D *Chi2Map_10 = (TH2D*)f->Get("Chi2Map_10");
  TH2D *Chi2Map_11 = (TH2D*)f->Get("Chi2Map_11");


  int nbinsx = Chi2Map_0->GetNbinsX();
  double xwidth = Chi2Map_0->GetBinWidth(1);
  double lox = Chi2Map_0->GetBinLowEdge(1);
  double hix = Chi2Map_0->GetBinLowEdge(nbinsx) + xwidth;
  double newlo = sin(lox*pi/180)*sin(lox*pi/180);
  double newhi = sin(hix*pi/180)*sin(hix*pi/180);

  int nbinsy = Chi2Map_0->GetNbinsY();
  double ywidth = Chi2Map_0->GetYaxis()->GetBinWidth(1);
  double loy = Chi2Map_0->GetYaxis()->GetBinLowEdge(1);
  double hiy = Chi2Map_0->GetYaxis()->GetBinLowEdge(nbinsy) + ywidth;

  const int nx = nbinsx + 1;
  double bounds[nx];
  bounds[0] = newlo;
  for (int xbin=0; xbin<nbinsx; ++xbin) {
    double thislox = Chi2Map_0->GetBinLowEdge(xbin);
    double thishix = thislox + xwidth;
    double bound = sin(thishix*pi/180)*sin(thishix*pi/180);
    bounds[xbin+1] = bound;
    cout << xbin << " " << thislox << " " << thishix << " " << bound << endl;
  } 

  TH2D *New_Chi2Map_0 = new TH2D("Chi2Map_0","Chi2Map_0",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *New_Chi2Map_1 = new TH2D("Chi2Map_1","Chi2Map_1",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *New_Chi2Map_2 = new TH2D("Chi2Map_2","Chi2Map_2",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *New_Chi2Map_3 = new TH2D("Chi2Map_3","Chi2Map_3",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *New_Chi2Map_4 = new TH2D("Chi2Map_4","Chi2Map_4",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *New_Chi2Map_5 = new TH2D("Chi2Map_5","Chi2Map_5",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *New_Chi2Map_6 = new TH2D("Chi2Map_6","Chi2Map_6",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *New_Chi2Map_7 = new TH2D("Chi2Map_7","Chi2Map_7",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *New_Chi2Map_8 = new TH2D("Chi2Map_8","Chi2Map_8",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *New_Chi2Map_9 = new TH2D("Chi2Map_9","Chi2Map_9",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *New_Chi2Map_10 = new TH2D("Chi2Map_10","Chi2Map_10",nbinsx,bounds,nbinsy,loy,hiy);
  TH2D *New_Chi2Map_11 = new TH2D("Chi2Map_11","Chi2Map_11",nbinsx,bounds,nbinsy,loy,hiy);


  fillit(nbinsx,nbinsy,Chi2Map_0,New_Chi2Map_0);
  fillit(nbinsx,nbinsy,Chi2Map_1,New_Chi2Map_1);
  fillit(nbinsx,nbinsy,Chi2Map_2,New_Chi2Map_2);
  fillit(nbinsx,nbinsy,Chi2Map_3,New_Chi2Map_3);
  fillit(nbinsx,nbinsy,Chi2Map_4,New_Chi2Map_4);
  fillit(nbinsx,nbinsy,Chi2Map_5,New_Chi2Map_5);
  fillit(nbinsx,nbinsy,Chi2Map_6,New_Chi2Map_6);
  fillit(nbinsx,nbinsy,Chi2Map_7,New_Chi2Map_7);
  fillit(nbinsx,nbinsy,Chi2Map_8,New_Chi2Map_8);
  fillit(nbinsx,nbinsy,Chi2Map_9,New_Chi2Map_9);
  fillit(nbinsx,nbinsy,Chi2Map_10,New_Chi2Map_10);
  fillit(nbinsx,nbinsy,Chi2Map_11,New_Chi2Map_11);

  TString outfile = "root/Bubbles_q23_exp";
  outfile += exp;
  outfile += ".root";
  TFile *out = new TFile(outfile,"recreate");
  New_Chi2Map_0->Write();
  New_Chi2Map_1->Write();
  New_Chi2Map_2->Write();
  New_Chi2Map_3->Write();
  New_Chi2Map_4->Write();
  New_Chi2Map_5->Write();
  New_Chi2Map_6->Write();
  New_Chi2Map_7->Write();
  New_Chi2Map_8->Write();
  New_Chi2Map_9->Write();
  New_Chi2Map_10->Write();
  New_Chi2Map_11->Write();
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
  const double pi = 3.1415926535897;
  for (int xbin=0; xbin < nbinsx+2; ++xbin) {
    double xval = myhist->GetXaxis()->GetBinCenter(xbin);
    double newxval = sin(xval*pi/180)*sin(xval*pi/180);
    for (int ybin=0; ybin < nbinsy+2; ++ ybin) {
      double yval = myhist->GetYaxis()->GetBinCenter(ybin);
      double bincontent = myhist->GetBinContent(xbin,ybin);
      mynewhist->Fill(newxval,yval,bincontent);
    }
  }
}


