#include <iostream>
#include <vector>
#include <unordered_map>

// [2,4,1,5,3,6]   k = 6
//        ^

int subarraySum(std::vector<int> &nums, int k) {
    std::unordered_map<int, int> memo;
    memo[0] = 1;
    int res = 0, cur_sum = 0;
    for (int i = 0; i < nums.size(); ++i) {
        cur_sum += nums[i];
        res += memo[cur_sum - k];
        memo[cur_sum] += 1;
    }
    return res;
}

int main() {
    std::vector<int> nums;
    nums.push_back(2);
    nums.push_back(4);
    nums.push_back(1);
    nums.push_back(5);
    nums.push_back(3);
    nums.push_back(6);
    
    int k = 6;
    int res = subarraySum(nums, k);
    std::cout << "res: " << res << "\n";
}
