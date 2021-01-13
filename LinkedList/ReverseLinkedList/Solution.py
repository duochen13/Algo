"""
input:
    1->2->3->4->5
output:
    5->4->3->2->1


    1->2->3->4->5
cur ^      (1->3)
tmp    ^   (2->1)
hea    ^

    2->1->3->4->5
cur    ^       (1->4)
tmp       ^    (3->2)
hea       ^

    3->2->1->4->5
cur       ^
tmp  
hea ^
    
            
cur (1)
tmp = cur.next (2)
tmp.next = head (2->1)
cur.next = tmp.next (1->3)
head = tmp


    3->2->1->4->5
    tmp

"""



