/*
 * test.cpp
 * g++ -std=c++11 test.cpp -o test.exep
 */
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/*
 * input: [1,2,3,5], missing value wont appear in the beginning or the end
 * output: 4
 *
 * input: [3,6,12]
 * output: 9
 *
 */

// helper function
int sum(vector<int> nums);
void swap(int &a, int &b);
void printVector(vector<int> nums);

// math solution
int findMissingNumberMath(vector<int> nums) {
    return ((nums[0] + nums[nums.size() - 1]) * (nums.size() + 1) / 2) - sum(nums);
}

// binary search
// 0 1 2 3 4 index
// 1 2 3 5 6 nums
// l   m   r   1 + 1 * 2 = 3
//     l m r   1 + 1 * 3 = 4
//     l r     1 + 1 * 2 = 3
// 
int findMissingNumber(vector<int> nums) {
    int res = -1, l = 0, r = nums.size() - 1, d = (nums[nums.size() - 1] - nums[0]) / nums.size();
    while (l < r) {
        int mid = l + (r - l) / 2;
        if (nums[mid] == nums[0] + d * mid)
            l = mid + 1;
        else
            r = mid;
    }
    return nums[0] + d * l;
}

/*
  Input: A = [4,7,9,10], K = 3
  Output: 8
  Explanation: 
  The missing numbers are [5,6,8,...], hence the third missing number is 8.
  
  Input: A = [1,2,4], K = 3
  Output: 6
  Explanation: 
  The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
*/

// 0 1 2 3
// 4 7 9 10  nums[mid]  nums[l] + diff 
// l m   r      7          4 + 0 = 4    diff = 2 < K, diff = K - diff = 3 - 2 = 1
//   l m r      9          

int missingElement(vector<int> &nums, int k) {
    return -1;
}
    
int main(int argv, char** argc) {

    vector<int> nums = {9,6,4,2,3,5,7,0,1};
    int res = -1;

    cout << res << endl;

    return 0;
}

int sum(vector<int> nums) {
    int res = 0;
    for (int num : nums)
        res += num;
    return res;
}

void swap(int &a, int &b) {
    int tmp = a;
    a = b;
    b = tmp;
}

void printVector(vector<int> nums) {
    cout << " ";
    for (int i = 0; i < nums.size(); ++i)
        cout << i << " ";
    cout << endl;
    for (int num : nums)
        cout << num << " ";
    cout << endl;
}


