#include <iostream>
#include <math.h>
using namespace std;


int main()
{
	cout << "Numerical Methods: Practice Task #02 / Example A" << endl;
	// x = log(1 + x) 
	// Fixed Point Iteration Method

	int n = 30;
	double x1 = 0.5;
	double x2;
	double delta;

	for (int i = 0; i <= n; i++)
	{
		x2 = log(x1 + 1);
		delta = abs(x2 - x1);

		printf("# iter. - %d\t| x[n] = %f\t| x[n+1] = %f\t| delta = %f\n", i, x1, x2, delta);

		x1 = x2;
	}

	system("pause");
	return 0;
}
