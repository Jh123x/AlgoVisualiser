# Algo Visualiser

## What does this do?
- Visualise your algorithms based on what you code


## Quick Start
1. Go to `__main__.py` file
1. Create a new function 
1. Pass the function into the `game = Animate(<Your Function>, (<source coord>, <target coord>), dim = <(x,y) dimention of grid>, resolution = <resolution of the window>)`


## Restriction on functions
1. Whenever a node is visited please yield the node coordinates for the UI
1. Make use of the visited array that will be passed to the function
1. Function signature must be `(*args, visited)` where args are any arguments you passed in yourself. Look at the example in `__main__.py` for more information


## Instructions when using
1. `Space bar` to start the simulation
1. `left click` to set which squares are blocked (Click same squares again to unblock)
1. `r` to reset the simulation
1. `e` to reset the blocking


## Tech Stack
1. [Pygame](https://www.pygame.org/docs/)


## Know Bugs
1. Unable to work with recursive functions


## To do
1. Add backtracking (Increases complexity for the user implementing the function)
1. Better UI (I'm not really a UI Guy thou ><)
