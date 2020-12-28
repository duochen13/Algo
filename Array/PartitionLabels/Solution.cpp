/*
 * test.cpp
 * g++ -std=c++11 test.cpp -o test.exep
 */
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

/*
 *  Input: S = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 */

// helper function
void printVectorWithIndex(string &nums);
template <typename T, typename Y>
void printHashTable(unordered_map<T, Y> &memo);

vector<int> partitionLabels(string S) {
    vector<int> res;
    unordered_map<char, int> memo;
    for (int i = 0; i < S.size(); ++i)
        memo[S[i]] = i;
    printHashTable(memo);

    int i = 0;
    while (i < S.size()) {
        int start = i;
        int upper = memo[S[i]];
        while (i <= upper) {
            upper = max(memo[S[i]], upper);            
            cout << "s[" << i << "] = " << S[i] << ", upper = " << upper << endl;
            i++;
        }   
        // partition here
        res.push_back(upper - start + 1);
    }

    return res;
}


int main(int argv, char** argc) {

    string S = "ababcbacadefegdehijhklij";
    printVectorWithIndex(S);

    vector<int> res = partitionLabels(S);

    return 0;
}

template <typename T, typename Y>
void printHashTable(unordered_map<T, Y> &memo) {
    cout << "print hashtable key value pair" << endl;
    for (auto it = memo.begin(); it != memo.end(); ++it) {
        cout << it->first << ":" << it->second << " ";
    }
    cout << endl;
}

void printVectorWithIndex(string &nums) {
    cout << "print vector with index: " << endl;
    for (int i = 0; i < nums.size(); ++i)
        cout << i << " ";
    cout << endl;
    for (int i = 0; i < nums.size(); ++i)
        cout <<  nums[i] << ((i >= 10) ? "  " : " ");
    cout << endl;
}
