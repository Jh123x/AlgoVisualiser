from visualiser.Animation.Blocks.Block import Block
from visualiser.Animation.Constants.Enums import State

class Grid(object):
    def __init__(self, rows:int, cols:int, height:int, width:int, block_list: list):
        """Grid that will be animated"""
        self.rows = rows
        self.cols = cols
        self.blocks = []
        self.height = height
        self.width = width
        self.block_width = min(height// rows, width // cols) 

        # Create the blocks
        for r in range(rows):
            for c in range(cols):
                self.blocks.append(Block(self.block_width, self.block_width * r, self.block_width * c))

        for x,y in block_list:
            self.get(x,y).set_blocked()

        return super().__init__()

    def draw(self, screen):
        """Draw the blocks on the screen"""
        for b in self.blocks:
            b.update(screen)

    def toggle_collision(self, pos):
        """Check for collision"""
        for b in self.blocks:
            if b.rect.collidepoint(pos):
                b.cycle()

    def get(self, x:int, y:int):
        """Get the block at the position"""
        ind = x * self.cols + y
        return self.blocks[ind]

    def set_source(self, x, y):
        b = self.get(x,y)
        b.set_source()

    def set_dest(self, x, y):
        b = self.get(x,y)
        b.set_target()

    def mark_visited(self, x, y):
        """Mark the block as visited"""
        block = self.get(x,y)
        block.set_visited()

    def is_blocked(self, x, y):
        """Check if the path is blocked"""
        return self.get(x,y).status in (State.VISITED, State.BLOCKED, State.VISITING)

    def in_range(self, x, y):
        """Check if the coord is in range"""
        return 0 <= x < self.rows and 0 <= y < self.cols

    def reset(self):
        for b in self.blocks:
            b.reset()

    def clear_blocks(self):
        for b in self.blocks:
            b.clear_block()