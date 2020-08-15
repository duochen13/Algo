#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int jump(vector<int> nums) {
	int s = 0, e = 0, res = 0, max_end = INT_MAX;
	while (e + 1 < nums.size()) {
		++res;
		max_end = INT_MAX;
		for (int i = s; i < e + 1; ++i) {
			max_end = max(max_end, i + nums[i]);
		}
		s = e + 1;
		e = max_end;
	}
	return res;
}

int main() {
	return -1;
}
