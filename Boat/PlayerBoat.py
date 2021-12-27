import pygame as pg
from Boat.BaseBoat import BaseBoat

class PlayerBoat(BaseBoat):
    def __init__(self, space, left, right, up, down):
        super().__init__(space)
        self.left, self.right, self.up, self.down = left, right, up, down

    def update(self):
        return super().update(self.move, self.turn)

    def processEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == self.left:
                self.turn = -1
            elif event.key == self.right:
                self.turn = 1
            elif event.key == self.up:
                self.move = 1
            elif event.key == self.down:
                self.move = -1
        if event.type == pg.TEXTINPUT:
            if event.text == self.left:
                self.turn = -1
            elif event.text == self.right:
                self.turn = 1
            elif event.text == self.up:
                self.move = 1
            elif event.text == self.down:
                self.move = -1
        if event.type == pg.KEYUP:
            if event.key in [self.left, self.right] or event.unicode in [   
                self.left,
                self.right,
            ]:
                self.turn = 0
            if event.key in [self.up, self.down] or event.unicode in [
                self.up,
                self.down,
            ]:
                self.move = 0
