#include <numeric>

int solution(int number) 
{
    unsigned sum = 0;
    if(number > 1) {
      std::vector<int> v(number);
      std::iota(v.begin(), v.end(), 0); // generate numbers
      std::for_each(v.begin(), v.end(), [&sum](int i){  // then find sum
          sum += (i % 3 == 0) || (i % 5 == 0) ? i : 0;
      });
    }
    return sum;
}