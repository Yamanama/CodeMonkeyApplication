import pygame
class Scene:
    """
    Base class for scenes
    """
    def __init__(self):
        self.next = self
    
    def process_input(self, events):
        """
        process user input

        Raises - NotImplementedError - override in sub classes
        """
        raise NotImplementedError
    def update(self):
        """
        update

        Raises - NotImplementedError - override in sub classes
        """
        raise NotImplementedError
    def render(self, screen):
        """
        render the scene

        Raises - NotImplementedError - override in sub classes
        """
        raise NotImplementedError
    def switch_scene(self, next_scene):
        """
        switch to next scene
        """
        self.next = next_scene