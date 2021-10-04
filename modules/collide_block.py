import pygame

class collide_block():

    def __init__(self,pygameObj,x=0,y=0):
        self.x = x
        self.y = y
        self.pygame = pygameObj
        self.image_path = R"imgs\tiles\dark_block.gif"
        self.img = self.pygame.image.load(self.image_path)
        
        self.up = pygame.Rect(x,y,63,1)
        self.down = pygame.Rect(x,y+63,63,1)
        self.left = pygame.Rect(x,y+5,1,63)
        self.right = pygame.Rect(x+63,y+5,1,63)

    def disable_up(self):
        self.up = None
