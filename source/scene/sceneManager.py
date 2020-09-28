class SceneManager:
    def __init__(self):
        self.next = self

    def process(self, events):   #필요성 검토 중
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

    def nextScene(self, scene):
        self.next = scene