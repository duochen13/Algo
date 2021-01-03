/*
 * test.cpp
 * g++ -std=c++11 test.cpp -o test.exep
 */
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>


using namespace std;

bool dfs(unordered_map<int, vector<int>> &memo, unordered_set<int> &visited, int node, int parent){
    // node is visited, cycle detected
    if (visited.find(node) != visited.end())
        return false;
    // mark as visited
    visited.insert(node);
    // dfs
    for (int & n : memo[node]) {
        if (n != parent)
            if (!dfs(memo, visited, n, node))
                return false;
    }
    return true;
}

bool validTree(int n, vector<vector<int>> &edges) {
    // hashset to store visited nodes
    unordered_set<int> visited;
    // construct adjacent list for graph representation
    unordered_map<int, vector<int>> memo;
    for (vector<int> & edge : edges) {
        memo[edge[0]].push_back(edge[1]);
        memo[edge[1]].push_back(edge[0]);
    }
    // dfs starting from 0, detect if there exists a cycle
    if (!dfs(memo, visited, 0, -1))
        return false;

    return visited.size() == n;
}


int main(int argv, char** argc) {

    return 0;
}
