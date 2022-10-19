# %%
from typing import List


class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for x in sandwiches:
            if x in students:
                students.remove(x)
            else:
                break
        return len(students)