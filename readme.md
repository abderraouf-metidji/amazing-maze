# Maze generation and resolution

Project done using : 

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Project
We were tasked with creating 2 algorithms to generate mazes and 2 algorithms to solve the maze we have generated. 

The algorithm used are:
* **Recursive / Backtracking**
* **Kruskal**
* **Backtracking / Backtracking**
* **A***

The Recursive and Kruskal algorithm were used for the generation of the maze, while the Backtracking and A* were used to solve the mazes.

## Solution and implementation

Let's take a deeper look into the algorithms and how they were implemented.

### Generator

#### Recursive / Backtracking

The first algorithm which uses recursive to create a maze is based on breaking walls start from the first cell in the grid (_the starting point of the maze_) and advancing from cell to cell until it reaches an already visited cell, meaning that is has no "**neighbor**" available. 

_The "**visited**" variable is in algorithm to allow us to check if a cell has already been visited by the generator or not. Neighbor is a term that we will use to describe the cells that are next to our current cell._ 

The algorithm then stops when it reaches a certain number of iterations which is equal to the size of the maze, the maze being of size **n*n**. Once all cells have been visited and a wall has been broken each time we have a fully working maze with one possible route from the starting position to the finish. 

#### Kruskal

The second algorithm is a bit more complex and uses the **Kruskal** logic. Here, our starting point is completely randomized. We are still using the concept of neighboring cells but we change our starting point each time and we are not following a "**route**". The way we establish if the maze is finished or not is by attributing a value to each cell. For example cell **(0, 0)** will have a value of **0** while cell **(0, 1)** will have a value of **1**.

Therefore, we can see that each cell has a unique value allowing us to differentiate between all the cells. 
Once a value has been attributed we are going to pick a random cell, check its neighbors and check its value. If there are available neighbors and the value of the neighboring cell is not equal to our **current_cell** we will chose a neighbor at random again and changes its value to the lowest of the two. For example, if our current cell value is **5** and our neighbor value is **6**, both cell will have a value of **5**. 

Once the neighboring cell has had its value changed the algorithm checks for cells connected to the neighbor and changes their value as well in order to start the creation of multiple routes throughout the maze. 
When all our cell have reached a value of **0**, we know that our maze is finished and all the cells are connected. 

### Solver

#### Recursive / Backtracking

In this case the logic is similar to the generator but here we don't break walls, we simple move from cell to cell until we reach a point where there are no more neighbor available. Meaning that we are stuck in the maze.

When we find ourselves stuck we go back to a position where another neighbor is available in order to change the route we are taking. Of course a condition is used to check whether we have reached the exit of the maze or not in order to avoid backtracking to the entrance when we have solved the maze. 

#### A*

Just like Kruskal, this algorithm is a bit more complex. Here we are going through the maze twice. The first time we are calculating 3 values known as **g**, **h** and **f**.

Here is a formula representing these values: 

**f(n) = g(n)+h(n)**

Where **f(n)** is the total cost to reach the cell **n** and **g(n)** and **h(n)** are defined as:

**g(n) →** It is the **actual cost** to reach cell **n** from the **start** cell.

**h(n) →** It is the **heuristic cost** to reach to the **goal** cell from cell **n**. It is the **estimated cost** to reach the goal cell from cell **n**.

In this case to calculate the value of h we have used the **Manhattan distance**. 

We will save the value of each cell in different lists that we will use when going through the maze the second time in order to chose the best path possible, the one with the lower **cost** in order to reach the finish. 

Here we are not looking for an exit but rather calculating the most optimal path to take in order to solve the maze. 

## Complexity

TBD

## Conclusion

The project is not finished yet but from what I was able to test on my end the kruskal algorithm is having a harder time generating bigger mazes when compared to the backtracking/recursive algorithm. This might be because I have decided to work with cells instead of sets when generating the mazes. 

Maybe using the method where we first iterate through all the walls in the maze and then pick a random wall to connect two cells instead of two cells and break a wall might be more efficient.

Other than that we are able, with the run.py file, to generate a maze based on two algorithms and solve the generated maze with two algorithms as well. When we decide to solve a maze we simply have to name the file and the maze + png of the maze will be generated in a folder. 