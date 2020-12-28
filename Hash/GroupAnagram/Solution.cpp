/*
 * test.cpp
 * g++ -std=c++11 test.cpp -o test.exep
 */

/*
   Input: strs = ["eat","tea","tan","ate","nat","bat"]
   Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
 */
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <unordered_map>
using namespace std;

// { sortedWord: [word1, word2, ...] }
// { aet: [eat, tea, ate], ... }
vector<vector<string>> groupAnagrams(vector<string> & strs) {
    unordered_map<string, vector<string>> memo;
    vector<vector<string>> res;

    for (string & str : strs) {
        string key = str;
        sort(key.begin(), key.end());
        memo[key].push_back(str);
    } 

    for (auto it = memo.begin(); it != memo.end(); ++it) {
        res.push_back(it->second);
    }
    
    return res;
}


// helper function
template<typename T>
void print(vector<vector<T>> data) {
    for (auto & d : data) {
        for (auto & x : d) {
            cout << x << " ";
        }
        cout << endl;
    }
}

int main(int argv, char** argc) {

    vector<string> strs = { "eat","tea","tan","ate","nat","bat" };

    vector<vector<string>> res = groupAnagrams(strs);
    print(res);

    return 0;
}
