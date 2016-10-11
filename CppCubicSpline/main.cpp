#include<iostream>
#include<vector>
#include"CppCubicSpline.h"
#include"matplotlibcpp.h"

namespace plt=matplotlibcpp;

using namespace std;

int main(void){
  cout<<"cpp spline sample"<<endl;
  vector<double> sx{0,1,2,3};
  vector<double> sy{2.7,6,5,6.5};

  CppCubicSpline cppCubicSpline(sy);
  vector<double> rx;
  vector<double> ry;
  for(double i=0.0;i<=3.2;i+=0.1){
    rx.push_back(i);
    ry.push_back(cppCubicSpline.Calc(i));
  }

  plt::named_plot("Truth",sx,sy, "xb");
  plt::named_plot("interporation",rx,ry, "-r");
  plt::legend();
  plt::axis("equal");
  plt::grid(true);
  plt::show();
}

