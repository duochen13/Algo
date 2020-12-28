
def segments(message):
    # Write your code here
    lastSpace = -1
    seg, prevStart = 1, 0
    N = len(message) // 160 + 1
    D = 160 - 5
    res = []
    for i, c in enumerate(message):
        if c == ' ':
            lastSpace = i
        if i % D == 0 and i != 0:
            # print("i: {}, lastSpace: {}, str: {}".format(i, lastSpace, message[lastSpace: lastSpace + 5]))
            content = message[prevStart:lastSpace]
            res.append(message[prevStart:lastSpace] + ('' if len(content) == 155 else ' ') + '({}/{})'.format(seg, N))
            prevStart = lastSpace + 1
            if len(content) == D:
                prevStart -= 1
            seg += 1
    res.append(message[prevStart:] + (('({}/{})'.format(seg, N)) if N != 1 else ''))
    return res

message = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus"
# print(message)

res = segments(message)

print(res)



# def f1(codes, numbers):
#     memo = {}
#     keys = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
#     for i, key in enumerate(keys):
#         for c in key:
#             memo[c] = str(i)
#     # print(memo)

#     phoneNumberSet = set()
#     res = []
#     for code in codes:
#         num = ''.join([memo[k] for k in code])
#         # print("code:{}, num:{}".format(code, num))
#         for number in numbers:
#             if num in number[4:] and number not in phoneNumberSet:
#                 res.append(number)
#                 phoneNumberSet.add(number)
#     # sort
#     return res

# codes = ['TWLO', 'CODE', 'HTCH']
# numbers = ['17474824380', '14157088956', '919810155555', '15109926333', '1415123456']

# res = f1(codes, numbers)
# print(res)


# from collections import deque

# def printMax(nums, n, k): 
    
#     res = nums[0]
    
#     dq = deque() 
      
#     for i in range(k): 
        
#         # For every element, the previous  
#         # smaller elements are useless 
#         # so remove them from Qi 
#         while dq and nums[i] <= nums[dq[-1]] : 
#             dq.pop() 
          
#         # Add new element at rear of queue 
#         dq.append(i); 
          
#     # Process rest of the elements, i.e.  
#     # from arr[k] to arr[n-1] 
#     for i in range(k, n): 
          
#         # The element at the front of the 
#         # queue is the largest element of 
#         # previous window, so print it 
#         print(str(nums[dq[0]]) + " ", end = "") 
#         res = max(res, nums[dq[0]])
          
#         # Remove the elements which are  
#         # out of this window 
#         while dq and dq[0] <= i-k: 
              
#             # remove from front of deque 
#             dq.popleft()  
          
#         # Remove all elements smaller than 
#         # the currently being added element  
#         # (Remove useless elements) 
#         while dq and nums[i] < nums[dq[-1]] : 
#             dq.pop() 
          
#         # Add current element at the rear of Qi 
#         dq.append(i) 
      
#     # Print the maximum element of last window 
#     print(str(nums[dq[0]])) 
#     res = max(res, nums[dq[0]])
#     return res

# arr = [12, 1, 78, 90, 57, 89, 56] 
# k = 3

# res = printMax(arr, len(arr), 3)


# print("res: ", res)