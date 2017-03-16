#include <algorithm>
#include <vector>
#include <iomanip>
#include <sstream>

std::string seriesSum(int n)
{
    float sum = 0;
    if(n > 0){
        std::vector<float> values(n);
        values[0] = 1; // set first value to 1 cuz 1/1 = 1
        // generate the rest of the values
        std::generate(values.begin() + 1, values.end(), [i=1,n] () mutable {
            return i += 3;
        });
        // now find the sum of 1/ n where n in values generated above
        std::for_each(values.begin(), values.end(), [i = 0, &sum](const int &n) mutable {
                sum += 1 / float(n);
        });
    }
    // format the string according to the description
    std::stringstream stream;
    stream << std::fixed << std::setprecision(2) << sum;
    return stream.str();
}