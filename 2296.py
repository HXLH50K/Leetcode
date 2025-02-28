class TextEditor:
    def __init__(self):
        # 初始化空文本和光标位置
        self.text = ""
        self.cursor = 0

    def addText(self, text: str) -> None:
        # 在光标位置插入文本
        self.text = self.text[: self.cursor] + text + self.text[self.cursor :]
        # 移动光标到插入文本的末尾
        self.cursor += len(text)

    def deleteText(self, k: int) -> int:
        # 计算实际可以删除的字符数
        delete_count = min(k, self.cursor)
        # 删除光标左边的字符
        self.text = self.text[: self.cursor - delete_count] + self.text[self.cursor :]
        # 更新光标位置
        self.cursor -= delete_count
        return delete_count

    def cursorLeft(self, k: int) -> str:
        # 移动光标向左
        self.cursor = max(0, self.cursor - k)
        # 返回光标左边最多10个字符
        return self.text[max(0, self.cursor - 10) : self.cursor]

    def cursorRight(self, k: int) -> str:
        # 移动光标向右
        self.cursor = min(len(self.text), self.cursor + k)
        # 返回光标左边最多10个字符
        return self.text[max(0, self.cursor - 10) : self.cursor]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
