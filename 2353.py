from sortedcontainers import SortedList


class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        # 存储食物信息的字典 food -> (cuisine, rating)
        self.food_info = {}
        # 存储每种烹饪方式的评分和食物 cuisine -> SortedList((-rating, food))
        self.cuisine_ratings = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            # 存储食物信息
            self.food_info[food] = [cuisine, rating]
            # 初始化该烹饪方式的SortedList（如果不存在）
            if cuisine not in self.cuisine_ratings:
                self.cuisine_ratings[cuisine] = SortedList()
            # 添加食物评分信息（用负数是为了实现从高到低排序）
            self.cuisine_ratings[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        # 获取食物信息
        cuisine, oldRating = self.food_info[food]
        # 从对应烹饪方式的列表中移除旧的评分信息
        self.cuisine_ratings[cuisine].remove((-oldRating, food))
        # 添加新的评分信息
        self.cuisine_ratings[cuisine].add((-newRating, food))
        # 更新食物信息
        self.food_info[food][1] = newRating

    def highestRated(self, cuisine: str) -> str:
        # 返回该烹饪方式下评分最高的食物
        # 由于使用了负数评分，SortedList中第一个元素就是评分最高的
        # 如果有相同评分，元组的第二个元素(food名称)会决定顺序
        return self.cuisine_ratings[cuisine][0][1]
