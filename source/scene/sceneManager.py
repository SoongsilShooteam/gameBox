class SceneManager:
    def __init__(self):
        self.next = self

    def process(self, events):
        print("process")

    def update(self):
        print("update")

    def render(self, screen):
        print("render")

    def nextScene(self, scene):
        self.next = scene