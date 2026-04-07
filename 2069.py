from typing import List


class Robot:

    def __init__(self, width: int, height: int):
        self.grid_boundary = [None] * (2 * (width + height) - 4)
        self.width = width
        self.height = height
        self.pos = 0
        self.first_step = True
        i = 0
        while i < width:
            self.grid_boundary[i] = [i, 0]
            i += 1
        while i < width + height - 1:
            self.grid_boundary[i] = [width - 1, i - width + 1]
            i += 1
        while i < 2 * width + height - 2:
            self.grid_boundary[i] = [2 * width - 3 - i + height, height - 1]
            i += 1
        while i < 2 * (width + height) - 4:
            self.grid_boundary[i] = [0, 2 * (width + height) - 4 - i]
            i += 1

    def step(self, num: int) -> None:
        if num > 0:
            self.first_step = False
        self.pos = (self.pos + num) % len(self.grid_boundary)

    def getPos(self) -> List[int]:
        return self.grid_boundary[self.pos]

    def getDir(self) -> str:
        if self.pos == 0:
            if self.first_step:
                return "East"
            else:
                return "South"
        if self.pos <= self.width - 1:
            return "East"
        elif self.pos <= self.width + self.height - 2:
            return "North"
        elif self.pos <= 2 * self.width + self.height - 3:
            return "West"
        else:
            return "South"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
