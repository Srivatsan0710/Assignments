#include<bits/stdc++.h>
//#include<stdio.h>
using namespace std;
double randomval(double minv, double maxv)
{
	srand(time(0));
	return minv + (maxv - minv) * ((double)rand() / (double)RAND_MAX);
}
class Point
{
    public:
	double x1,x2,y;
	Point()
	{
	    x1 = randomval(-1.0,1.0);
	    x2 = randomval(-1.0,1.0);
	    y = randomval(-1.0,1.0);
	}
	Point(double a, double b,double c)
	{
		this->x1 = a;
		this->x2 = b;
		this->y = c;
 	}
 	Point(double a,double b)
 	{
 		this->x1 = a;
 		this->x2 = b;
	}
};

class Line
{
    public :
	double x1,x2,y1,y2;
	double m,b;
	Line(double xcoord1, double ycoord1, double xcoord2, double ycoord2)
	{
		this->x1 = xcoord1;
		this->y1 = ycoord1;
		this->x2 = xcoord2;
		this->y2 = ycoord2;
		this->m = (this->y2 - this->y1) / (this->x2 - this->x1);
		this->b = this->y1 - (this->m * this->x1);
	}
};



void hw1(int iter, int n)
{
	int i = 0;
	int c = 0;
	int counts[iter];
	double rates[iter];
	for(i=0; i<iter; i++)
	{
		double w[3] = {0.0};
		c = 0;
		double x1 = randomval(-1.0,1.0);
		double x2 = randomval(-1.0,1.0);
		double y1 = randomval(-1.0,1.0);
		double y2 = randomval(-1.0,1.0);
		
		Line line(x1,y1,x2,y2);
		
		Point points[n];
		
		for(int j=0; j<n; j++)
		{
			double newX, newY;
			newX = randomval(-1.0, 1.0);
			newY = randomval(-1.0, 1.0);

			Point p(newX, newY, 0.0);

			double pointY = p.x2;
			double lineY = (line.m * p.x1) + line.b;

			if(pointY > lineY)
				p.y = 1.0;
			else
				p.y = -1.0;

			points[j] = p;
		}
		
		int flag = 0;
		do
		{
			flag = 0;
			int k = 0;
			for(int k=0; k<n; k++)
			{
				double acty = points[k].y;
				double calcy;
				double d;
				d = w[0] + (w[1] * points[k].x1) + (w[2] * points[k].x2);
				if(d > 0)
				calcy = 1.0;
				else
				calcy = -1.0;
				if(calcy != acty)
				{
					flag = 1;
					c++;	
					w[0] +=  acty;
					w[1] +=  (acty * points[k].x1);
					w[2] +=  (acty * points[k].x2);	
					break;
				}
			}
		}while(flag);
		
		counts[i] = c;
		int dis = 0;
		for(int k = 0; k<n; k++)
		{
			double X1 = randomval(-1.0, 1.0);
			double X2 = randomval(-1.0, 1.0);		
			double f = (line.m * X1) + line.b;
			double Y;		
			if(X2 > f)
				 Y = 1.0;
			else 
				Y = -1.0;			
			double d = w[0] + (w[1] * X1) + (w[2] * X2);
			double gY;
			if (d > 0)
				gY = 1.0;
			else 
				gY = -1.0;	
			if (Y != gY)
				dis++;
		}
		rates[i] = (double)dis / 100;
	}
	int noi;
	double d ;
	cout << endl;
	for(int i=0; i<iter; i++)
	{
		noi += counts[i];
		cout << counts[i] << " " << rates[i] << endl;
		d += rates[i];
	}
	cout << "Iterations : " << noi/iter << endl;
	cout << "Rate of disagreement : " << d/iter << endl; 	
}

int main()
{
	int iter , n;
	cout << "Enter number of iterations : " ;
	cin >> iter;
	cout << endl << "Enter number of points : " ;
	cin >> n;
	hw1(iter,n);
//	getch();
	return 0;
}

