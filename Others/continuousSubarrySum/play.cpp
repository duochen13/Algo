#include<iostream>
#include<vector>

void print_helper(std::vector<int> &nums);

bool checkSubarraySum(std::vector<int> &nums, int k) {
    std::vector<int> pre_sum(nums.size() + 1, 0);
    for (int i = 0; i < nums.size(); ++i) {
        pre_sum[i + 1] = pre_sum[i] + nums[i];
    }
    for (int i = 0; i < pre_sum.size(); ++i) {
        for (int j = 0; j < i; ++j) {
            int diff = pre_sum[i] - pre_sum[j];
            if (diff == k && (i - j) > 1) {
               return true;
            } 
        }
    }
    return false;
}

void print_helper(std::vector<int> & nums) {
    for (auto & num : nums) {
        std::cout << num << " ";
    }
    std::cout << "\n";
}


int main() {
    // [23, 2, 4, 6, 7],  k=6
    std::vector<int> nums;
    nums.push_back(23);
    nums.push_back(2);
    nums.push_back(4);
    nums.push_back(6);
    nums.push_back(7);
    int k = 7;
    bool res = checkSubarraySum(nums, k);
    std::cout << ((res) ? "yes" : "no");
}
