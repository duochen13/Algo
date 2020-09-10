#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;


void dfs(vector<vector<int>> &Broad, int x, int y, string cur, int &res) {

    // base case
    if (cur.length() == 4) {
        res = max(res, stoi(cur));
        cout << "Res: " << res << endl;
        return;
    }

    int m = Broad.size(), n = Broad[0].size();
    int localMax = -1, final_x = 0, final_y = 0;
    int directions[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};

    for (auto pair : directions) {
        int a = pair[0], b = pair[1];
        if (x + a < 0 || x + a >= m || y + b < 0 || y + b >= n || Broad[x + a][y + b] == -1) {
            continue;
        }
        if (Broad[x + a][y + b] > localMax) {
            localMax = Broad[x + a][y + b];
            final_x = x + a;
            final_y = y + b;
        }
    }

    cout << "cur: " << cur << ", localMax: " << localMax << ", x: " << x << ", y: " << y << "|final_x: " << final_x << ", final_y: " << final_y << endl;

    int pre = Broad[x][y];
    Broad[x][y] = -1;
    dfs(Broad, final_x, final_y, cur + to_string(localMax), res); /// 
    Broad[x][y] = pre;
}

void dfs(vector< vector<int> > &A, int x, int y, int country, const int marked) {
    int m = int(A.size()), n = int(A[0].size());
    // out of range or makred
    if (x < 0 || x >= m || y < 0 || y >= n || A[x][y] == marked || A[x][y] != country)
        return;
    // mark current position
    A[x][y] = marked;
    cout << "x: " << x << ", y: " << y << ", A[x][y]: " << A[x][y] << endl;
    int directions[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
    // dfs in 4 directions
    for (auto pair : directions) {
        int a = pair[0], b = pair[1];
        dfs(A, x + a, y + b, country, marked);
    }
    return;
} 

int solution(vector< vector<int> > &A) {
    // write your code in C++14 (g++ 6.2.0)
    int m = int(A.size()), n = int(A[0].size());
    int res = 0;
    const int marked = 10001;

    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (A[i][j] == marked)
                continue;
            res += 1;
            dfs(A, i, j, A[i][j], marked);
        }
    }
    return res;
}



int main(int argv, char** argc) {
    // 1,000,000,000
    vector<vector<int>> A = {{5,4,3,2,3,1,4},{4,3,2,2,3,4,1},{4,4,4,2,4,4,1}};
    int res = solution(A);
    cout << res << endl;

    // string S = "cdeo";
    // vector<int> A = {3,2,0,1};
    // string res = solution(S, A);
    // cout << res << endl;
}

// int solution(vector<int> &A, int K) {
//     if (K > int(A.size()))
//         return -1;
//     // write your code in C++14 (g++ 6.2.0)
//     sort(A.begin(), A.end(), greater<int>());
//     int res = 0, k = 0, tmp1, tmp2;
//     // get top k elements
//     while (k < K) {
//         res += A[k];
//         k += 1;
//     }
//     // current sum is even
//     if ((res & 1) == 0) {
//         return res;
//     }
//     // current sum is odd
//     int smallestOdd = numeric_limits<int>::max(), smallestEven = numeric_limits<int>::max();

//     for (int i = 0; i < k; ++i) {
//         if (A[i] % 2 == 1) {
//             smallestOdd = min(A[i], smallestOdd);
//         } else {
//             smallestEven = min(A[i], smallestEven);
//         }
//     }
//     int largestEven = numeric_limits<int>::min(), largestOdd = numeric_limits<int>::min();
//     for (int j = k; j < int(A.size()); ++j) {
//         if (A[j] % 2 == 0) {
//             largestEven = max(A[j], largestEven);
//         } else {
//             largestOdd = max(A[j], largestOdd);
//         }
//     }
//     // swap
//     bool tmp1Valid = smallestOdd != numeric_limits<int>::max() && largestEven != numeric_limits<int>::min();
//     bool tmp2Valid = smallestEven != numeric_limits<int>::max() && largestOdd != numeric_limits<int>::min();
//     tmp1 = res - smallestOdd + largestEven;
//     tmp2 = res - smallestEven + largestOdd;

//     cout<<"sOdd: "<<smallestOdd<<", lEven:"<<largestEven<<", sEven:"<<smallestEven<<", lOdd:"<<largestOdd << endl;
//     cout <<"res: " << res << ", tmp1:" << tmp1 << ", tmp2:" << tmp2 << endl;
//     cout <<"tmp1Valid:"<< tmp1Valid << ", tmp2Valid:" << tmp2Valid << endl;

//     if (!tmp1Valid && !tmp2Valid) {
//         return -1;
//     } else if (tmp1Valid && !tmp2Valid) {
//         return (tmp1 % 2 == 0) ? tmp1 : -1;
//     } else if (!tmp1Valid && tmp2Valid) {
//         return (tmp2 % 2 == 0) ? tmp2 : -1;
//     } 
    
//     cout << "tmp1: " << tmp1 << ", tmp2: " << tmp2 << endl;

//     return max(tmp1, tmp2);
// }



// int findLargetInt(vector<vector<int>> &Broad) {
//     int m = Broad.size(), n = Broad[0].size();
//     int res = 0, maxDigit = -1;

//     for (int i = 0; i < m; ++i) {
//         for (int j = 0; j < n; ++j) {
//             maxDigit = max(maxDigit, Broad[i][j]);
//         }
//     }

//     for (int i = 0; i < m; ++i) {
//         for (int j = 0; j < n; ++j) {
//             if (Broad[i][j] == maxDigit)
//                 dfs(Broad, i, j, to_string(maxDigit), res);
//         }
//     }

//     return res;
// }


// int main(int argv, char** argc) {
//     // vector< vector<int> > Broad(3, vector<int>(5, 0));
//     // Broad = {{9,1,1,0,7}, {1,0,2,1,0}, {1,9,1,1,0}};
//     vector< vector<int> > Broad(4, vector<int>(5, 0));
//     Broad = {{1,2,2,1,1}, {1,0,1,1,1}, {9,1,2,2,1}, {0,0,9,1,1}};
//     int res = findLargetInt(Broad);
//     cout << "hello" << endl;
// }


// [[1,2,2,1,1],
// [1,0,1,1,1],
// [9,1,2,2,1],
// [0,0,9,1,1]]