import math


class Vector2:
    x = 0.0
    y = 0.0

    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 두 벡터의 내적 구하기
    def dot(self, v2):
        return (self.x * v2.x) + (self.y * v2.y)

    # 두 벡터 사이각 구하기
    def angle(self, v2):
        v = Vector2(v2.x - self.x, v2.y - self.y)
        return math.atan2(v.y, v.x)

    # 벡터의 길이 구하기
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    # 두 벡터의 사이 길이 구하기
    def distance(self, v2):
        return math.sqrt(math.pow(v2.x - self.x, 2) + math.pow(v2.y - self.y, 2))

    # 벡터 정규화
    def normalize(self):
        length = self.length()
        self.x /= length
        self.y /= length

    # 벡터 정규화
    def normalized(self):
        length = self.length()
        return Vector2(self.x / length, self.y / length)
