from typing import List
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        while asteroids:
            asteroid = asteroids.pop(0)
            if mass < asteroid:
                return False
            mass += asteroid
        return True