class SceneManager:
    def __init__(self):
        self.next = self

    def process(self, events):
        pass
        #print("process")

    def update(self):
        pass
        #print("update")

    def render(self, screen):
        pass
        #print("render")

    def nextScene(self, scene):
        self.next = scene