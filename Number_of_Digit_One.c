//Leetcode link: https://leetcode.com/problems/number-of-digit-one/description/
//Suresh G --> C++

class Solution {
public:
    int countDigitOne(int n) {
        int res = 0;
        for (long m = 1; m <= n; m *= 10) {
            long a = n / (10 * m), b = n % m, x = n / m % 10;
            if (x == 0) res += m * a;
            else if (x == 1) res += m * a + (b + 1);
            else if (x >= 2) res += (a + 1) * m;
        }
        return res;
    }
};
