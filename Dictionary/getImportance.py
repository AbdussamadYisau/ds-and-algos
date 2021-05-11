#  https://leetcode.com/problems/employee-importance/submissions/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees, id):
        
        employeeDict = dict()
        
        for employee in employees: 
            employeeDict[employee.id] = employee
        
        
        def Importance(ele):
            if len(ele.subordinates) == 0:
                return ele.importance
            else:
                S = ele.importance
                
                for _id in ele.subordinates:
                    S += Importance(employeeDict[_id])
                return S
                    
        return Importance(employeeDict[id])
            
example = Solution()

print(example.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1))