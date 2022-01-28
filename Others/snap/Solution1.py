# Consider the following string compression algorithm that works on a string containing only English uppercase letters.
#   If there is a substring that consists of a pattern P repeated K times, it may be written as "(KP)".
#     For example, a string ABABAB may be written as (3AB).
#       Compression can be applied to the already compressed string:
#        a string ABABABAABABABA may be first compressed as (2ABABABA), and then as (2(3AB)A).
# 
# You are given the compressed string.  Do a decompression procedure.
# 
# Example input 1:
#   (2(3AB)A)。 ABABAB ABABAB A
# Example output 1:
#   ABABAB A ABABABA


"""
s = "(2(1AB)C)"  -> 
output = "ABCABC"  

s = "(1(0AB)C)" 
output = "C"

s = "(12AC)"
output = "ACAC...AC"

index 012345678
s =   (2(3AB)A)
             ^

res = ""
             
stack = [(, 2, (, 3]
pattern = "AB"
res = pattern * stack[-1]

stack = [(, 2]
pattern = ""
res = 3 * "AB" = ABABAB
res += pattern = ABABAB + A

res = pattern * stack[-1] = 2 * (ABABABA)

while not reach the end
    if encounter a character:
        while not encounter ):
            keep finding characters 
            append to pattern
        we find a complete pattern
        find the multipler
            pop stack until encounter (
        calcualte multiper * pattern
        reset pattern
        
    store current val in stack

index 012345678
s =   (2(3AB)A)
              ^

stack = [(, 2, (, 3]
pattern = "AB"
mutliper = "3"
res = "ABABAB"


stack = [(, 2]
pattern = "A"
mutliper = 2
res = 2 * res
"""

def convertString(s):
    # check invalid input
    if not s or s[0] != "(" or s[-1] != ")":
        raise Exception("Error: the string should contain left and right braces.")
    stack = []
    pattern, res = "", ""
    
    i = 0
    while i < len(s):
        c = s[i]
        if c.isdigit() or c == "(":
            stack.append(c)
        # uppercase characters
        else:
            # finding complete pattern
            while not s[i] == ")":
                pattern += s[i]
                i += 1
            # find the multiper by poping elemenets from stack
            multipler = ""
            while stack[-1] != "(":
                multipler = stack.pop() + multipler
            stack.pop()
            # check if multiper is missing
            if not multipler:
                raise Exception("Error: multiper is missing.")
            # concatenate to res
            res += pattern
            res = int(multipler) * res
            pattern, multipler = "", ""
        i += 1
        
    return res

# assert convertString(s="(2(3AB)A)") == "ABABABAABABABA"
# assert convertString(s="(1AB)C") == "ABC"
# assert convertString(s="(1(11A)B)") == "AAAAAAAAAAAB"

# left and right braces are missing
# convertString(s="(AB)C")
# multiper is missing
convertString(s="((11A)B)")
        
# invalid input: s="(11A)B", "(?(11A)B)"


