/*
 * test.cpp
 * g++ -std=c++11 test.cpp -o test.exep
 */
#include <iostream>
#include <vector>
using namespace std;


template<typename T, typename F>
void callFunc(F f, T t) {
    f(t);
}

template<typename T>
void printVector(vector<T> &data) {
    cout << "print data: " << endl;
    for (auto & d : data) 
        std::cout << d << std::endl;
}


template<typename T>
void selectionSort(vector<T> &nums) {
    
    cout << "selection sort" << endl;
    for (int i = 0; i < nums.size(); ++i) {
        // find tmpMin in [i, N]
        int minIndex = i;       
        for (int j = i + 1; j < nums.size(); ++j) {
           if (nums[j] < nums[i]) {
                minIndex = j;
           }
        }
        // swap
        T tmp = nums[i];
        nums[i] = nums[minIndex];
        nums[minIndex] = tmp;
        cout << "nums[i]: " << nums[i] << ", nums[minIndex]: " << nums[minIndex] << endl;
        callFunc(printVector<T>, nums);
    }
}


int main(int argv, char** argc) {
    
    vector<int> nums;
    nums.push_back(64);
    nums.push_back(25);
    nums.push_back(12);
    nums.push_back(22);
    nums.push_back(11);

    selectionSort(nums);

//    callFunc(printVector<int>, nums);
//    callFunc(selectionSort<int>, nums);
//    callFunc(printVector<int>, nums);
    for (int & num : nums)
        cout << num << endl;

    return 0;
}

