## my_Sudoku_Solver
- This repo is to implement a Sudoku solver using backtracking algorithm.

#### So what is Sudoku?
- Sudoku is a logic-based, combinatorial number-placement puzzle. In classic sudoku, the objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid contains all the digits from 1 to 9.
### Steps to create the automatic sudoku solver:
##### Naive Algorithm:
- try out all the numbers for all the cells(This is very long).
##### With backtracking:
- [X] pick an empty cell
- [X] try all numbers for the cell
- [X] find one that works
- [X] repeat the above steps
- [X] backtrack when no correct ans
###About the GUI version
##### The Sudoku GUI is made using pygame
###### There is an option to manually insert the values into the sudoku grid, when done and want to check the answer press the "s" key to solve the board. The board will solve by itself using backtracking, and the process can be visualized.

### Future plans for this project:
- [ ] add functionality of a timekeeper
- [ ] add functionality of a cell validator
- [ ] add functionality of a difficulty switcher
- [ ] improve the graphics of the board