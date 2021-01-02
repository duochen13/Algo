/*
 * test.cpp
 * g++ -std=c++11 test.cpp -o test.exep
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <unordered_map>
#include <limits>

using namespace std;


bool comp(string &a, string &b) {
    return a.size() < b.size();
}

int longestStrChain(vector<string> &words) {

    sort(words.begin(), words.end(), comp);
    unordered_map<string, int> memo;
    int res = numeric_limits<int>::min();

    for (string word : words) {
        for (int i = 0; i < word.size(); ++i) {
            string tmp = word.substr(0, i) + word.substr(i + 1);
            cout << "tmp: " << tmp << " , word: " << word << endl;
            memo[word] = max(memo[word], memo[tmp] + 1);
            res = max(res, memo[word]);
        }
    }

    return res;
}


int main(int argv, char** argc) {

    vector<string> words = {"a","b","ba","bca","bda","bdca"};
    int res = longestStrChain(words);

    cout << "res: " << res << endl;


    return 0;
}
