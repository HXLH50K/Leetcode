# %%
class MyLinkedList:

    def __init__(self):
        self.arr = []

    def get(self, index: int) -> int:
        try:
            return self.arr[index]
        except:
            return -1

    def addAtHead(self, val: int) -> None:
        self.arr.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.arr.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > len(self.arr):
            return
        index = max(index, 0)
        self.arr.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        try:
            del self.arr[index]
        except:
            pass


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)