# %%
from typing import List


class Solution:

    # def asteroidCollision(self, asteroids: List[int]) -> List[int]:
    # while True:
    #     new_asteroids = []
    #     i = 0
    #     while i < len(asteroids):
    #         if i == len(asteroids) - 1 or asteroids[i] * asteroids[
    #                 i + 1] > 0 or asteroids[i] < 0 and asteroids[i +
    #                                                              1] > 0:
    #             new_asteroids.append(asteroids[i])
    #         elif asteroids[i] == -asteroids[i + 1]:
    #             i += 1
    #         elif asteroids[i] > -asteroids[i + 1]:
    #             new_asteroids.append(asteroids[i])
    #             i += 1
    #         else:
    #             new_asteroids.append(asteroids[i + 1])
    #             i += 1
    #         i += 1
    #     if new_asteroids == asteroids:
    #         break
    #     asteroids = new_asteroids
    # return asteroids
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        a = []
        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                while stack:
                    if -x > stack[-1]:
                        stack.pop()
                    elif x == -stack[-1]:
                        stack.pop()
                        break
                    elif -x < stack[-1]:
                        break
                else:
                    a.append(x)
        return a + stack


a = Solution()
a.asteroidCollision([-1, -2, 2, 1])
# %%
