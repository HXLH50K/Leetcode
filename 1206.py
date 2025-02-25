import random


class Node:
    def __init__(self, val=-1, level=32):
        self.val = val
        # forward列表存储每层的下一个节点
        self.forward = [None] * level


class Skiplist:
    def __init__(self):
        self.MAX_LEVEL = 32  # 最大层数
        self.P = 0.25  # 层数增加的概率
        self.level = 0  # 当前最大层数
        # 创建头节点
        self.head = Node()

    def _random_level(self) -> int:
        """随机生成层数"""
        level = 1
        # 每次有25%的概率增加一层
        while random.random() < self.P and level < self.MAX_LEVEL:
            level += 1
        return level

    def search(self, target: int) -> bool:
        """查找目标值是否存在"""
        current = self.head

        # 从最高层开始查找
        for i in range(self.level - 1, -1, -1):
            # 在当前层向右移动,直到找到最后一个小于target的节点
            while current.forward[i] and current.forward[i].val < target:
                current = current.forward[i]

        # 移动到第0层的下一个节点
        current = current.forward[0]

        # 判断是否找到目标值
        return current is not None and current.val == target

    def add(self, num: int) -> None:
        """添加新值"""
        # update数组记录每一层需要更新的节点
        update = [None] * self.MAX_LEVEL
        current = self.head

        # 从最高层开始查找插入位置
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].val < num:
                current = current.forward[i]
            update[i] = current

        # 生成随机层数
        new_level = self._random_level()

        # 如果新的层数大于当前最大层数
        if new_level > self.level:
            for i in range(self.level, new_level):
                update[i] = self.head
            self.level = new_level

        # 创建新节点
        new_node = Node(num, new_level)

        # 更新每一层的指针
        for i in range(new_level):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        """删除指定值"""
        # update数组记录每一层需要更新的节点
        update = [None] * self.MAX_LEVEL
        current = self.head

        # 从最高层开始查找要删除的节点
        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].val < num:
                current = current.forward[i]
            update[i] = current

        # 移动到可能要删除的节点
        current = current.forward[0]

        # 如果没有找到要删除的值
        if not current or current.val != num:
            return False

        # 从最低层开始删除节点
        for i in range(self.level):
            if update[i].forward[i] != current:
                break
            update[i].forward[i] = current.forward[i]

        # 更新当前最大层数
        while self.level > 1 and not self.head.forward[self.level - 1]:
            self.level -= 1

        return True
