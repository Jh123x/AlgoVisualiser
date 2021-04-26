import pygame
from visualiser.Animation.Constants.Enums import State


class Block(pygame.sprite.Sprite):
    color_map = {
        State.NOT_VISITED: (255, 0, 0),
        State.VISITED: (0, 255, 0),
        State.VISITING: (0, 0, 255),
        State.BLOCKED: (255, 255, 255),
        State.TARGET: (255, 255, 0),
        State.SOURCE: (0, 255, 255)
    }

    def __init__(self, width: int, x_pos: int, y_pos: int):
        """The main block that makes up the screen"""

        # Initialise the vars
        self.status = State.NOT_VISITED
        self.width = width
        self.xpos = x_pos
        self.ypos = y_pos
        self.rect = pygame.Rect(x_pos, y_pos, width, width)
        self.rect.left = self.xpos
        self.rect.top = self.ypos

        return super().__init__()

    def set_visiting(self):
        """Mark as visiting this block"""
        self.status = State.VISITING

    def set_visited(self):
        """Mark as visiting this block"""
        self.status = State.VISITED
    
    def set_blocked(self):
        self.status = State.BLOCKED

    def set_unvisit(self):
        """Unvisit the block"""
        self.status = State.NOT_VISITED

    def set_source(self):
        self.status = State.SOURCE
    
    def set_target(self):
        self.status = State.TARGET

    def update(self, screen):
        """Draw the sprite"""
        color = self.color_map[self.status]
        pygame.draw.rect(screen, color, self.rect)

    def cycle(self):
        """Cycle through the states when clicked"""
        if self.status == State.BLOCKED:
            self.status = State.NOT_VISITED
        elif self.status == State.NOT_VISITED:
            self.status = State.BLOCKED


    def reset(self):
        """Reset the status of the block"""
        if self.status in (State.BLOCKED, State.SOURCE, State.TARGET):
            return
        self.status = State.NOT_VISITED

    def clear_block(self):
        """Clear blocks"""
        if self.status == State.BLOCKED:
            self.status = State.NOT_VISITED