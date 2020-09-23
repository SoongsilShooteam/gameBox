from source.scene.sceneManager import *
import pygame
import object

class StageOneScene(SceneManager):
    def __init__(self):
        SceneManager.__init__(self)

    def process(self, events):
        print("process")

    def update(self):
        print("update")

    def render(self, screen):
        screen.fill((100, 100, 100))
        #print("StageOneScene")