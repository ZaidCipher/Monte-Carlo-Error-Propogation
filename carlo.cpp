#include <iostream>
#include <vector>
#include <random>
#include <cmath>
#include <fstream>

using namespace std;

double mearth = 5.9722e24;
double rearth = 6.371e6;
double pi=3.141592653;

int main() {

	random_device rd;
	mt19937 gen(rd());

	normal_distribution<double> tmass(1.347,0.069);
	normal_distribution<double> tradius(1.116,0.014);
    double n=100000;
	vector<double> dens(n);
    ofstream file("x.txt");


	double sum=0;
	double sqsum=0;

	for(int i=0;i<n;i++){
		double m=tmass(gen)*mearth;
		double r=tradius(gen)*rearth;

		double volume=(4.0/3.0)*pi*pow(r,3);
		double density=(m/volume)*0.001;
		sum+=density;

		file<<density<<endl;

	}
	double mean=sum/n;

	for(double d:dens){
		sqsum+=(mean-d)*(mean-d);
	}

	double std=sqrt(sqsum/n);

	cout<<mean<<endl;
	cout<<std<<endl;

    
    
}