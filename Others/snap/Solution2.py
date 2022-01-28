# Course Secheudling
#
# A: OS
# B: Databases
# C: Networks
# D: Intro to Programming
#
# A -> B
# A -> C 
# C -> D
#
# 1. Design the course catalog
# 2. Write a function to return one way to take a course
#  findWay(c: Catalog, course)
#  findWay(c1, "A") -> ["D", "C", "B", "A"] or ["B", "D", "C",  "A"]
#  findWay(c1, "C") -> ["D", "C"]

class Node:
    def __init(self, cid, name):
        self.cid = cid
        self.name = name
        
# mapping: course -> prerequest courses
catalog = {
    "A": ["B", "C"],
    "B": [],
    "C": ["D"],
    "D": []
}

"""
A -> "B"
      -> None
 ->. "C"
      -> "D"
         -> None 
curPath=[], to keep track of the path to take the target course
curCid
             "A", []
              /         \
           "B", ["A"]    "C", ["A"]
                           \
                        "D", ["A", "C", "B"]
add courses from last level to curPath ["B", "C"]
"""

"""
A -> "B"
      -> "Z" 
        -> None
 ->. "C"
      -> "D"
         -> None 
curPath=[], to keep track of the path to take the target course
curCid
             "A", []
              /         \
           "B", ["A"]    "C", ["A"]
            /                \ 
"Z", ["A", "C", "B"]            "D", ["A", "C", "B"]
add courses from last level to curPath ["B", "C"]
"""


def findWayDFS(catalog, targetCourse):
    coursePath = []
    
    def dfs(catalog, targetCourse, prevPath):
        nonlocal coursePath
        # if there is no prerequest
        if not catalog[targetCourse]:
            coursePath = prevPath + [targetCourse]
            print("targetCourse={}, coursePath={}".format(targetCourse, coursePath))
            return
        # store courses from last level
        prevPath = catalog[targetCourse]
        for course in catalog[targetCourse]:
            if dfs(catalog, course, prevPath):
                return
        return 
    
    dfs(catalog, targetCourse, [])
    return coursePath[::-1]

catalog = {
    "A": ["B", "C"],
    "B": [],
    "C": ["D"],
    "D": []
}
# findWay(catalog, "A") # ["D","B","C","A"]
    
"""
catalog = {
    "A": ["B", "C"],
    "B": [],
    "C": ["D"],
    "D": []
}
findWay(catalog, "A")
        "A", []
          /            \
       "B",["B","C"]     "C",["B","C"]
        /
     "", ["B", "C"] + ["B"]
"""


def findWay(catalog, targetCourse):
    q = [targetCourse]
    coursePath = [targetCourse]
    
    while q:
        # if not catalog[targetCourse]:
        #     coursePath += [catalog[targetCourse]]
        # print("coursePath: ", coursePath)
        curCourse = q.pop(0)
        print("curCourse:", curCourse)
        # if not catalog[curCourse]:
        #     coursePath.append(curCourse)
        # else:
        for course in catalog[curCourse]:
            # print("==child course:", course)
            q.append(course)
            coursePath.append(course)
        # print("==q:", q)
    return coursePath[::-1]

catalog = {
    "A": ["B", "C"],
    "B": [],
    "C": ["D"],
    "D": []
}
res = findWay(catalog, "A")
print(res)
"""
catalog = {
    "A": ["B", "C"],
    "B": [],
    "C": ["D"],
    "D": []
}

q = ["A"]
N = 1
coursePath = ["B", "C"]


findWay(catalog, "A")
"""
    
