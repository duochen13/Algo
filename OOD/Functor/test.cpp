#include <iostream>
#include <vector>
#include <algorithm>


class CalSum {
    public:
        // usage: for_each(data.begin(), data.end(), CalSum());
        CalSum(): sum(0) {}
        void operator() (int n) {
            sum += n;
        }
        CalSum(std::vector<int> nums) {
            for (int &num: nums)
                sum += num;
        }
        int getSum() const { return sum; }
    private:
        int sum = 0;
};


struct Sum {
    // usage: Sum s1 = for_each(data.begin(), data.end(), Sum())
    void operator() (int n) {
        sum += n;
    }
    int sum = 0;
};


int main(int argv, char**argc) {

    std::vector<int> nums;
    nums.push_back(3);
    nums.push_back(4);
    CalSum cs(nums);

    std::cout << cs.getSum() << std::endl;
    
    
    CalSum cs_ = for_each(nums.begin(), nums.end(), CalSum());
    std::cout << cs_.getSum() << std::endl;

    Sum s1 = for_each(nums.begin(), nums.end(), Sum());
    std::cout << s1.sum << std::endl;

    return 0;
}
