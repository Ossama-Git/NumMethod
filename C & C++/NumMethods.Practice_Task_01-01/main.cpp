#include <iostream>
#include <math.h>
using namespace std;


int main()
{
	cout << "Numerical Methods: Practice Task #01 / Example A" << endl;
	// f(x) = x^6 - X - 1
	// The Bisection Method

	double x1 = 0;
	double x2 = 2;
	double f1, f, f2;
	double x;
	int n = 20;

	for (int i = 1; i <= n; i++)
	{
		x = (x1 + x2) / 2;

		f1 = pow(x1, 6.0) - x -1;
		f = pow(x, 6.0) - x -1;
		f2 = pow(x2, 6.0) - x - 1;

		if (f1 * f <= 0)
		{
			x1 = x1;
			x2 = x;
		}
		else
		{
			x1 = x;
			x2 = x2;
		}

		printf("# iter. - %d\t| x1 = %f\t| x = %f\t|  x2 = %f\t|  f1 = %f\t|  f = %f\t|  f2 = %f\t|\n", i, x1, x, x2, f1, f, f2);
	}

	printf("Solution: %f\n", x);

	system("pause");
	return 0;
}


