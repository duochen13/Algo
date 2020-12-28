/*
 * test.cpp
 * g++ -std=c++11 test.cpp -o test.exep
 */
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
/*
 * 1->2->3->4->5->null
 * ^h -
 * 2->1->3->4->5
 * h  ^  -
 * 3->2->1->4->5
 * h     ^  -
 * 4->3->2->1->5
 * h   
 *
 * cur's next becomes new head
 *
 * 5->4->3->2->1->null
 */

// given
struct ListNode {
    int val;
    ListNode *next;
    ListNode(): val(0), next(nullptr) {}
    ListNode(int x): val(x), next(nullptr) {}
    ListNode(int x, ListNode *next): val(x), next(next) {}
};

// helper function
ListNode * constructListNode(vector<int> nums); 
void printListNode(ListNode *node);


ListNode *reverseList(ListNode *head) {
    
    ListNode *cur = head, *curNext = head->next;
    while (cur->next != nullptr) {
        curNext = cur->next;
        cur->next = curNext->next;
        curNext->next = head;
        head = curNext;
        printListNode(curNext);
    }
        
    return head;
}

int main(int argv, char** argc) {

    vector<int> nums = {1,2,3,4,5};
    ListNode *node = constructListNode(nums);
    printListNode(node);

    ListNode *res = reverseList(node);
    printListNode(res);

    return 0;
}

void printListNode(ListNode *node) {
    while (node != nullptr) {
        cout << node->val << " ";
        node = node->next;
    }
    cout << endl;
}

ListNode * constructListNode(vector<int> nums) {
    ListNode *res = new ListNode(-1);
    ListNode *tmp = res;
    for (int num : nums) {
        tmp->next = new ListNode(num);
        tmp = tmp->next;
    }
    return res->next;
}


