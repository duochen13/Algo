#include <iostream>
#include <vector>

void print_helper(std::vector<int> &nums);

int subarraySum(std::vector<int> &nums, int k) {
    int res = 0;
    std::vector<int> pre_sum(nums.size() + 1, 0);
    for (int i = 0; i < nums.size(); ++i) {
        pre_sum[i + 1] = pre_sum[i] + nums[i];
    }
    print_helper(pre_sum);
    for (int i = 0; i < pre_sum.size(); ++i) {
        for (int j = 0; j < i; ++j) {
            if (pre_sum[i] - pre_sum[j] == k)
                ++res;
        }
    }
    return res;
}

void print_helper(std::vector<int> &nums) {
    for (auto &num: nums)
        std::cout << num << " ";
    std::cout << "\n";
}

int main() {
    std::vector<int> nums;
    nums.push_back(1);
    nums.push_back(1);
    nums.push_back(1);
    int k = 2;
    int res = subarraySum(nums, k);
    std::cout << res << std::endl;
}

