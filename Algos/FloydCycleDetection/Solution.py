

# time complexity: O(n)
# ref: https://stackoverflow.com/questions/47193225/runtime-complexity-of-floyds-cycle-detection

class Solution(object):
    
    # fast & slow pointer
    def findNext(self, n):
        tmp = 0
        for digit in str(n):
            tmp += int(digit)**2
        return tmp
    
    def isHappy(self, n):
        if n == 1:
            return True
        slow = n
        fast = self.findNext(n)
        while slow != fast:
            if slow == 1 or fast == 1:
                return True
            slow = self.findNext(slow) # speed = v
            fast = self.findNext(self.findNext(fast))  # speed = 2v
        return False

    # alternative
    def isHappy(self, n):
        memo = set()
        memo.add(n)
        while n != 1:
            nextNum, a = 0, n
            while a > 0:
                a, b = n // 10, n % 10
                n = a
                nextNum += b**2
            if nextNum in memo:
                return False
            memo.add(nextNum)
            n = nextNum
        return True
    
    def isHappy(self, n):
        memo = set()
        memo.add(n)
        while n != 1:
            tmp = 0
            for digit in str(n):
                tmp += int(digit)**2
            if tmp in memo:
                return False    
            memo.add(tmp)
            n = tmp
        return True
    