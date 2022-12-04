# Rudimentary Sudoku Solver
### Solves Sudoku puzzles

## Introduction

I've been looking for projects to flex my Python muscles a bit, and everywhere I look there is someone recommending that your portfolio should have a Sudoku solver. Well here is mine.

I knew this would be a bit of a challenge since my experience with Python is still somewhat limited and my knowledge of Sudoku is far more limited. In my entire life I may have solved like 15 puzzles including 10 I did while working on this project. I also didn't want to look at any tutorials since I wanted to see if I can do it completely on my own (which as it turns out, I could). I do plan on finally looking at those tutorials to see if I can simplify the code a bit, rewrite some parts.

The biggest limitation is in how the program takes the puzzle. It has to be hardcoded. I left it that way for now since any improvements I can apply now will just improve the way the user can input the numbers when I would much rather have the puzzles either generated automatically or imported from somewhere else.


## How it works:

As mentioned above, the puzzle is hardcoded in the program in the form of 9 lists, each representing a row of the puzzle. A list of the 9 rows called "grid" is then passed to the function **update()** and inside a list called "cols" will be generated with 9 lists inside it each representing a column, and similarly a list called "boxes" containing 9 lists each represinting a box is generated. **update()** then passes back "cols", "boxes", and an updated version of "grid" plus a list called "digs" containing the digits 1-9 to **main()**, they are then passed to the function **solver()** which proceeds to solve the puzzle, passing the value of grid, now with the solved pazzule in it back to **main()** which will then send the final "grid" to a function called **displayer()** which displays the solved puzzle.

The logic that the program uses to solve the puzzle is: it iterates over the rows in the grid, and for every row it iterates over every digit in digs, and iterates over every position in the "row", checking if the value is None. If it is None it will check if the dig is already in the row, if it is then it'll be skipped to the next, if not then the **get_boxes()** function is called to determine the box this place is in. The digit is checked against the corresponding column and the box. If it exists in neither a possibility counter increments by 1 and then we move on to the next place looking for the same digit, repeating on all the places until the entire row is checked. If the possibility counter is at only 1, the value of the position in the row is updated to the value of the digit. Then **update()** is called to take in the new value of the row, generate updated grid, columns, and boxes. The process is then repeated until no more rows have values = None.

This might not be the best logic to solve Sudoku but I am such a novice in the game that I wouldn't know if this might not work for all cases. All puzzles I fed it so far were solved but I recognize that it might actually hit a wall. Conclusion, I need to solve more Sudoku puzzles.

## main()

**main()** initializes the values of the rows in the form of lists. The values in the lists are either an int or None. All the lists are grouped in a list called "grid". **main()** also initializes a list called "digs" which contains the digits 1-9. It then callse **update()** and retrieves the cols and boxes, prints the unsolved puzzle, then passes the cols, boxes, and the grid over to **solver()**, getting back the solved puzzle and displaying it.


## update()

This function creates lists to function as the columns of the puzzle, and lists to function as the boxes. It takes the grid and populates the columns and the boxes with the values in them.

This function takes the grid, iterates over each row inside the grid, and for each nth column it will take the value corresponding to n-1. For example the 7th column (which will sit in the 6th value inside cols) will take the 6th value in each of the rows. This is the code:

 cols = [col1,col2,col3,col4,col5,col6,col7,col8,col9]
   
 
 ```
 for x in range(9):
     for r in grid:
         cols[x].append(r[x])
```

Populating the boxes proved more tricky, since positionally they are not as defined as Rows or Columns. For example the first box is comprised of the first 3 values in the first 3 rows, the fifth box has the fourth, fifth, and sixth values in the fourth, fifth, and sixth rows...etc.

I relied on if conditionals to detrmine in which box each value belonged. I realize that this is only one step above just assigning the values into the boxes one at a time.

Here is the code:

```
for box in boxes:
    if boxno in [0,1,2]:
        for row in grid[0:3]:
            for j in range(3):
                box.append(row[j+boxno*3])
    elif boxno in [3,4,5]:
        boxno_ = boxno - 3
        for row in grid[3:6]:
            for j in range(3):
                box.append(row[j+boxno_*3])
    elif boxno in [6,7,8]:
        boxno_ = boxno - 6
        for row in grid[6:]:
            for j in range(3):
                box.append(row[j+boxno_*3])
    boxno += 1
```


In the end the rows, columns, and boxes with the updated values are returned.

## get_box()
  '''

## displayer()

This function takes the "Grid" which again is a list of 9 rows each has 9 values (either an int or None) and displayes it in the Sudoku grid way. It does so by simply adding white space after every third value and every third line. This is the resulting view

![image](https://user-images.githubusercontent.com/109043036/205515532-3cc17575-f935-4aae-8dde-d9687d54999a.png)


This fucnction is only called twice, at the beginning to display the unsolved puzzle and once at the end to display the solution.

## solver()

The function that solves. It takes the grid, columns, boxes, and a list of digits (digs) and returns the solved puzzle. Initially a "while True" since the idea is to keep iterating until the puzzle is solved, there are 3 more nested loops, iterating over the rows, for each value in each row it iterates over each digit in digs, if the digit is already in the row it's skipped entirely, otherwise the code proceeds to check the columns and boxes. Two temporary variables are initialized with value 0: *possib*, and *spot*, we'll get back to *spot* later but for now *possib* refers to the number of possible locations for each "dig". 

For each position **get_box()** is called to determine which box the position is in, and then the code checks if the digit is in either the corresponding box or column, if the answer is no to both, *possib* is incremented by 1. Once the entire row is iterated over, if possib equals zero or if it equals more than 1 then we move to the next digit. If *possib* does equal 1, it means that there was only 1 possible location where that particular digit can be placed, and so it is placed there and we're one step closer to a solution.

A problem I faced here is that during the first tests I ran, I found the solution written down in wrong positions. I had failed to account for the fact that the third nested for loop is iterating over all the values in a row and by the time the correct position is found we could be looking at a completely different value (position). This is where *spot* comes in. *spot* takes the current value of x which the is the constant used to iterate over the values in a given row each time *possib* is incremented, so it will always have the position of the last "possible' location for a given digit however since we're only interested in cases where *possib* equals 1, *spot* will always have the right position, and is used to update it inside the row.

To simplify it, here is the order of iteration: rows > digits > values inside the rows, columns, and boxes

```
while True:
    for s in range(9): ## iterates over the rows
        row = grid[s]
        for dig in digs: ## iterates over the digits
            possib = 0
            spot = 0
            if dig in row:
                pass
            else:
                for x in range(9): ## iterates over the values inside the rows, columns, and boxes
                    box = get_box(row,x,grid,boxes)
                    if row[x] == None:
                        if dig not in cols[x] and dig not in box:
                            possib += 1
                            spot = x
```

After every full "cycle" (iteration over rows, columns, and boxes) **update()** is called with the updated rows contain the new values and is used to substitue the values of the columns and boxes.

I've set 2 mechanisms to exit out of the infinite loop. The first is where the puzzle is solved, after every full cycle the code iterates over each row looking for any remaining "None" values, if one is found it breaks out of that loop to continue to the next cycle. If no "None" values are found a variable called cest_fini is set to True. If after checking all rows cest_fini is True then the program returns the solved puzzle to **main()**.

The last bit of code and the other way to exit the program is something I call the safety counter, if after a 1000 cycle no solution is found for the puzzle the program exits with a warning message.


## Future Plans:

I do not intend to add/fix any features on this as I plan to write a completely new Sudoku solver. That being said, if I were to change some things, here they are

1. Doing away with the grid/cols/boxes system and instead using dictionaries to manage the values. I thought about that when I was about two thirds of the way through but ultimately decided to push through with the foolish way I chose to write it.
2. Adding extra algorithms to solve the puzzles. Even though I have yet to encounter any in the tests I have run so far, I am sure there might be puzzles that cannot be solved by the code as it is. I want to implement at least 1 more approach and have the program switch back and forth between the two until the puzzle is solved.



