## Start typing here

"""
abccBa -> false
abccba -> true
a -> true
"" -> true
aa -> true
^^
aba -> true
abca -> false
"""
def isPalindrome(word):
    i, j = 0, len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False 
        i += 1
        j -= 1
    return True

assert isPalindrome(word="aba")
assert isPalindrome(word="a")
assert not isPalindrome(word="ab")
assert isPalindrome(word="")

"""
"abc -> [['a','b','c']]"
"aa -> [['a','a'], ['aa']]"

'aabc' -> [['a','a','b','c'],['aa','b','c']]
     
                   aabc
               /.     \            \
           a, abc        aa, bc      aab, c
               /. \
             a,bc  ab,c
               /.     \
               b,c.   a,b
               
                 start=0, curPath =[]
                /     \                \
           1,['a']    2,['aa']         3,['aab']
            /    \
    2,['a','a']  3,['a','ab']
        /
    3,['a','a','b']
    
    aabc
                0, []
                /     \                \
        1,['a']    2,['aa']         3,['aab']
            /    \
    2,['a','a']  3,['a','ab']
        /
    3,['a','a','b']
     / 
     
aabc
"""

def breakStrings(s):
    res = []
    
    def dfs(start, curPath):
        nonlocal s, res
        print("start={}, curPath={}, condition={}".format(start, curPath, start == len(s) - 1 and isPalindrome(curPath)))
        # reach the end of the string
        if start == len(s) - 1:
            for word in curPath:
                if not isPalindrome(word):
                    return
            res.append(curPath[:])
            print("add to res: ", res)
            return 
        # ways to break strings
        for i in range(start + 1, len(s)):
            curPath.append(s[start:i])
            dfs(i, curPath)  # ['abc'] + ['aa'] = ['abc', 'aa']
            curPath.pop()
        
    dfs(0, [])
    return res



res = breakStrings("aabc")
print("res:", res)

# assert isPalindrome(["aab"])
