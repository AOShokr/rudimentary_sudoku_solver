# Rudimentary Sudoku Solver
### Solves Sudoku puzzles

## Introduction

I've been looking for projects to flex my Python muscles a bit, and everywhere I look there is someone recommending that your portfolio should have a Sudoku solver. Well here is mine.

I knew this would be a bit of a challenge since my experience with Python is still somewhat limited and my knowledge of Sudoku is far more limited. In my entire life I may have solved like 15 puzzles including 10 I did while working on this project. I also didn't want to look at any tutorials since I wanted to see if I can do it completely on my own (which as it turns out, I could). I do plan on finally looking at those tutorials to see if I can simplify the code a bit, rewrite some parts.

The biggest limitation is in how the program takes the puzzle. It has to be hardcoded. I left it that way for now since any improvements I can apply now will just improve the way the user can input the numbers when I would much rather have the puzzles either generated automatically or imported from somewhere else.


## How it works:

As mentioned above, the puzzle is hardcoded in the program in the form of 9 lists, each representing a row of the puzzle. A list of the 9 rows called "grid" is then passed to the function **update()** and inside a list called "cols" will be generated with 9 lists inside it each representing a column, and similarly a list called "boxes" containing 9 lists each represinting a box is generated. **update()** then passes back "cols", "boxes", and an updated version of "grid" plus a list called "digs" containing the digits 1-9 to **main()**, they are then passed to the function **solver()** which proceeds to solve the puzzle, passing the value of grid, now with the solved pazzule in it back to **main()** which will then send the final "grid" to a function called **displayer()** which displays the solved puzzle.

The logic that the program uses to solve the puzzle is: it iterates over the rows in the grid, and for every row it iterates over every digit in digs, and iterates over every position in the "row", checking if the value is None. If it is None it will check if the dig is already in the row, if it is then it'll be skipped to the next, if not then the **get_boxes()** function is called to determine the box this place is in. The digit is checked against the corresponding column and the box. If it exists in neither a possibility counter increments by 1 and then we move on to the next place looking for the same digit, repeating on all the places until the entire row is checked. If the possibility counter is at only 
