"""
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

amazing video: https://www.youtube.com/watch?v=OvpKeraoxW0
"""

def copyRandomList(self, head):

    tmp = head
    nodes = collections.defaultdict(Node)
    while tmp:
        # dead node sitting in memory
        nodes[tmp] = Node(tmp.val, None, None)
        tmp = tmp.next
    nodes[tmp] = None
        
    res = Node(head.val, None, None)
    tmp = res
    while head:
        # get complete node in the original linkedlist
        nextNode, randomNode = head.next, head.random
        # assign properties with dead nodes sitting in memory
        tmp.random = nodes[randomNode]
        tmp.next = nodes[nextNode]
        # move forward
        tmp = tmp.next
        head = head.next

    return res
