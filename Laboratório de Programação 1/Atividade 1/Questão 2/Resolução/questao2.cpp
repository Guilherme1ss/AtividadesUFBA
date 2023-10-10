#include <iostream>

int main()
{

    int k, kN, j, jN, h, hN;

    std::cin >> k >> j >> h;
    std::cin >> kN >> jN >> hN;

    k = k + kN;
    j = j + jN;
    h = h + hN;

    std::cout << k << " " << j << " " << h << std::endl;

    return 0;
}