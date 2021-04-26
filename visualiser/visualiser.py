import pygame
from pygame.locals import *
from visualiser.Animation.Blocks.Grid import Grid


class Animate(object):
    def __init__(self, function, args: tuple = (), block_list: list = [], dim: tuple = (40, 40), resolution: tuple =(600,800), fps:int = 30):
        """Main class to animate the function"""

        # Store the variables
        self.init_func = function
        self.args = args
        self.isRunning = True
        self.startFlag = False
        self.fps = fps

        # Initialise the Blocks
        self.grid = Grid(*dim, *resolution, block_list=block_list)
        self.grid_reset = True
        self._init_grid()

        # Initialise the items
        self.screen = pygame.display.set_mode(resolution)
        self.function = function(*self.args, self.grid)

    def _init_grid(self):
        """Initialise the grid"""
        self.grid.set_dest(*self.args[1])
        self.grid.set_source(*self.args[0])

        if self.grid_reset:
            return

        self.grid_reset = True
        self.grid.reset()
        

    def parse_event(self, event) -> None:
        """Parse the event"""


        # If the user wants to quit
        if event.type == pygame.QUIT:
            self.isRunning = False

        # Mouse events
        if pygame.mouse.get_pressed()[0] and hasattr(event, 'pos'):
            self.grid.toggle_collision(event.pos)

        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                self.startFlag = not self.startFlag
            elif event.key == K_r:
                self._init_grid()
                self.function = self.init_func(*self.args, self.grid)
                self.startFlag = False
            elif event.key == K_e:
                self.grid.clear_blocks()

    def run(self) -> None:
        """Run the animation"""
        clock = pygame.time.Clock()

        curr_paths = []

        # Mainloop for the game
        while self.isRunning:

            # Cap the framerate
            clock.tick(self.fps)

            if self.grid_reset:
                self.grid_reset = False

            # Loop through all the events in the loop
            for event in pygame.event.get():
                self.parse_event(event)

            if self.startFlag:
                try:
                    curr = next(self.function)
                    self.grid.mark_visited(*curr)
                except StopIteration:
                    pass

            # Update the screen
            self.grid.draw(self.screen)
            pygame.display.update()
