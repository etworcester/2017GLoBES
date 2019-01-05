#include <vector>
#include <TSystem.h>

void BubblePlot(char exp[3])
{
  //Use this to draw the contours for a delta_CP and sin^2(2theta13) simulataneous measurement.
  
  //load GLOBESPlotterLib
  gSystem->Load("/lbne/u/etw2/globes/globes/lib/libGLOBESPlotterLib.so");
  
  //Create a BubblePlotter object.  BubblePlotter takes in a .dat file (see the documentation for details) and draws the contours for a delta_CP vs sin^2(2theta13) measurement.
  //use AddCurve(string filename,string label) for each curve you want drawn. 'label' is in TLatex style.
  cout << "working..." << endl;
  BubblePlotter *p = new BubblePlotter();
  char file1[80], file2[80], file3[80], file4[80], file5[80], file6[80], file7[80], file8[80], file9[80], file10[80], file11[80], file12[80], file13[80], file14[80], file15[80];
  strcpy(file1,"data/bubble_q23_optimized_long_dcp0_q23lo_exp");
  strcat(file1,exp);
  strcat(file1,".dat");
  strcpy(file2,"data/bubble_q23_optimized_long_dcp0_q23nom_exp");
  strcat(file2,exp);
  strcat(file2,".dat");
  strcpy(file3,"data/bubble_q23_optimized_long_dcp0_q23max_exp");
  strcat(file3,exp);
  strcat(file3,".dat");
  strcpy(file5,"data/bubble_q23_optimized_long_dcp0_q23hi_exp");
  strcat(file5,exp);
  strcat(file5,".dat");

  strcpy(file6,"data/bubble_q23_optimized_long_dcp+90_q23lo_exp");
  strcat(file6,exp);
  strcat(file6,".dat");
  strcpy(file7,"data/bubble_q23_optimized_long_dcp+90_q23nom_exp");
  strcat(file7,exp);
  strcat(file7,".dat");
  strcpy(file8,"data/bubble_q23_optimized_long_dcp+90_q23max_exp");
  strcat(file8,exp);
  strcat(file8,".dat");
  strcpy(file10,"data/bubble_q23_optimized_long_dcp+90_q23hi_exp");
  strcat(file10,exp);
  strcat(file10,".dat");

  strcpy(file11,"data/bubble_q23_optimized_long_dcp-90_q23lo_exp");
  strcat(file11,exp);
  strcat(file11,".dat");
  strcpy(file12,"data/bubble_q23_optimized_long_dcp-90_q23nom_exp");
  strcat(file12,exp);
  strcat(file12,".dat");
  strcpy(file13,"data/bubble_q23_optimized_long_dcp-90_q23max_exp");
  strcat(file13,exp);
  strcat(file13,".dat");
  strcpy(file15,"data/bubble_q23_optimized_long_dcp-90_q23hi_exp");
  strcat(file15,exp);
  strcat(file15,".dat");

  p->AddCurve(file1,"");
  p->AddCurve(file2,"");
  p->AddCurve(file3,"");
  //p->AddCurve(file4,"");
  p->AddCurve(file5,"");
  p->AddCurve(file6,"");
  p->AddCurve(file7,"");
  p->AddCurve(file8,"");
  //p->AddCurve(file9,"");
  p->AddCurve(file10,"");
  p->AddCurve(file11,"");
  p->AddCurve(file12,"");
  p->AddCurve(file13,"");
  //p->AddCurve(file14,"");
  p->AddCurve(file15,"");
  
  //SetX(number of log(sin^2(2theta13)) points and the range (inclusive) of those points. 
  //SetY(number of delta_CP points and the range (inclusive) of those points (in degrees).
  //set the labels for each axis
  p->SetX(200,30,60);
  p->SetY(200,-210,210);
  p->SetXLabel("#theta_{23}");
  p->SetYLabel("#delta_{CP} (degrees)");
  
  //Set a vector that determines what color each curve will be.  Each entry is the ROOT TColor code.
  //Here, the 68% curves will be red and the 95% curves will be blue.
  vector<int> colors(15,1);
  p->SetLineColors(colors);
  
  //Set a vector that determines what line style each curve will be.  Each entry is the ROOT TAttLine style code.
  //Here, all curves are solid
  vector<int> styles(15,1);
  p->SetLineStyles(styles);
  
  //Set a vector that determines the contour level, i.e. for what delta-chi2 do you want to draw the contour.
  //The 68% curves correspond to a delta-chi2 of 2.3, and the 95% curves correspond to a delta-chi2 of 6 (these are the delta-chi2 for *2* degrees of freedom!)
  vector<double> levels(15,2.3);
  p->SetContourLevels(levels);
  
  //Draw it!  
  //The string will be used in the names of the output files:
  //"xx.root" Has each histogram AFTER the contour levels have been set.  Draw with histname->Draw("cont3") to see the contour curves.
  //"chi2maps_xx.root" Has each chi2 vs delta_CP vs log(sin^2(2theta13))  histogram BEFORE the contour level has been set, so you can see the whole chi2 map.  Draw with histname->Draw("colz").
  //"xx.eps" Each plot will be saved to an eps file.
  char outfile[80];
  strcpy(outfile,"Bubbles_q23_exp");
  strcat(outfile,exp);
  p->DrawBubbles(outfile);
  
  //To make a pretty plot (like with the nice sin^2(2theta13) axis), you'll have to read in the histograms from the file into another script.
  
  return;
}
