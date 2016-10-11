/**
 *  @brief Cubic Spline header library
 *
 *  @author Atsushi Sakai
 *
 **/

#include <vector>
#include <math.h>

using namespace std;

/**
 *  @brief Cubic Spline header library
 *
 *  @usage 
 *    vector<double> sy{2.7,6,5,6.5};
 *    CppCubicSpline cppCubicSpline(sy);
 *    vector<double> rx;
 *    vector<double> ry;
 *    for(double i=0.0;i<=3.2;i+=0.1){
 *       rx.push_back(i);
 *       ry.push_back(cppCubicSpline.Calc(i));
 *    }
 */
class CppCubicSpline{
  public:
    CppCubicSpline(const vector<double> &y){

      InitParameter(y);

    }

    double Calc(double t){
        int j=int(floor(t));
        if(j<0){
            j=0;
        }
        else if(j>=a_.size()){
            j=(a_.size()-1);
        }

        double dt=t-j;
        double result=a_[j]+(b_[j]+(c_[j]+d_[j]*dt)*dt)*dt;
        return result;
    }

  private:
    vector<double> a_;
    vector<double> b_;
    vector<double> c_;
    vector<double> d_;
    vector<double> w_;

    void InitParameter(const vector<double> &y){
      int ndata=y.size()-1;

      for(int i=0;i<=ndata;i++){
        a_.push_back(y[i]);
      }

      for(int i=0;i<ndata;i++){
        if(i==0){
          c_.push_back(0.0);
        }
        else if(i==ndata){
          c_.push_back(0.0);
        }
        else{
          c_.push_back(3.0*(a_[i-1]-2.0*a_[i]+a_[i+1]));
        }
      }

      for(int i=0;i<ndata;i++){
        if(i==0){
          w_.push_back(0.0);
        }
        else{
          double tmp=4.0-w_[i-1];
          c_[i]=(c_[i]-c_[i-1])/tmp;
          w_.push_back(1.0/tmp);
        }
      }

      for(int i=(ndata-1);i>0;i--){
        c_[i]=c_[i]-c_[i+1]*w_[i];
      }

      for(int i=0;i<=ndata;i++){
        if(i==ndata){
          d_.push_back(0.0);
          b_.push_back(0.0);
        }
        else{
          d_.push_back((c_[i+1]-c_[i])/3.0);
          b_.push_back(a_[i+1]-a_[i]-c_[i]-d_[i]);
        }
      }

    }

};

