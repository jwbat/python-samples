#pragma once
#include "global.h"
#include <complex>

using std::complex;
using std::exp;

constexpr double    PI = 3.141592653589793238;
constexpr complex<double> I(0, 1);


complex<double> create_z(double theta1, double theta2, double theta3)
{
    complex<double> z =   0.5 * exp(I * theta1)
                        + 0.3 * exp(I * theta2)
                        + 0.7 * exp(I * theta1)
                        + 0.5 * exp(I * theta3);

    z *= HEIGHT / (2.0 * 2.1);                           // scale
    z += complex(WIDTH / 2.0, HEIGHT / 2.0);             // center
    return z;
}


struct Point
{
    double x;
    double y;
};
