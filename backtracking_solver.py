import os, copy, random
from collections import deque

class Solver:
    def __init__(self):
        """
        Initialize the Solver object with default values for the maze.
        """
        self.board = None  # 2D array representing the maze
        self.wall = '#'  # Character representing a wall in the maze
        self.route = '.'  # Character representing a route in the maze
        self.start = (0, 0)  # Starting cell coordinates
        self.finish = None  # Finish cell coordinates (will be set during maze loading)
    
    def get_maze(self, file):
        """
        Load the maze from the given file.
        """
        with open(file, 'r') as maze_file:
            self.board = [list(line.strip()) for line in maze_file]  # Read the maze from the file into a 2D array
        self.finish = (len(self.board) - 1, len(self.board[0]) - 1)  # Set the finish cell coordinates to the last cell in the maze
    
    def backtracking_solver(self):
        """
        Solve the maze using the backtracking algorithm.
        """
        self.current_cell = self.start  # Start from the starting cell
        self.board[self.current_cell[0]][self.current_cell[1]] = "o"  # Mark the starting cell as visited
        self.stack = deque()  # Stack to store the visited cells
        
        while self.current_cell != self.finish:  # Continue until the finish cell is reached
            neighbors = []  # List to store the neighboring cells
            
            # Check left neighbor
            if (
                self.current_cell[1] > 0
                and self.board[self.current_cell[0]][self.current_cell[1] - 1] == "."
            ):
                neighbors.append((self.current_cell[0], self.current_cell[1] - 1))
            
            # Check right neighbor
            if (
                self.current_cell[1] < len(self.board[0]) - 1
                and self.board[self.current_cell[0]][self.current_cell[1] + 1] == "."
            ):
                neighbors.append((self.current_cell[0], self.current_cell[1] + 1))
            
            # Check up neighbor
            if (
                self.current_cell[0] > 0
                and self.board[self.current_cell[0] - 1][self.current_cell[1]] == "."
            ):
                neighbors.append((self.current_cell[0] - 1, self.current_cell[1]))
            
            # Check down neighbor
            if (
                self.current_cell[0] < len(self.board) - 1
                and self.board[self.current_cell[0] + 1][self.current_cell[1]] == "."
            ):
                neighbors.append((self.current_cell[0] + 1, self.current_cell[1]))
            
            if neighbors:  # If there are neighboring cells
                random.shuffle(neighbors)  # Randomize the order of the neighbors
                next_cell = neighbors[0]  # Choose the first neighbor
                self.stack.append(self.current_cell)  # Push the current cell to the stack
                self.current_cell = next_cell  # Move to the next cell
                self.board[self.current_cell[0]][self.current_cell[1]] = "o"  # Mark the current cell as visited
            else:  # If there are no neighboring cells
                if not self.stack:  # If the stack is empty
                    print("No Solution")  # Maze has no solution
                    break
                else:
                    self.board[self.current_cell[0]][self.current_cell[1]] = "*"  # Mark the current cell as a dead end
                    self.current_cell = self.stack.pop()  # Backtrack to the previous cell
        
    def print_solution(self):
        """
        Print the maze with the solution.
        """
        for row in self.board:
            print(' '.join(row))

if __name__ == "__main__":
    solver = Solver()  # Create a Solver object
    solver.get_maze("maze.txt")  # Load the maze from the file
    
    output_dir = "solved_mazes"  # Directory to store the maze solutions
    
    if not os.path.exists(output_dir):  # Create the directory if it doesn't exist
        os.makedirs(output_dir)
    
    file_name = input("Enter a file name to save the solution (add .txt): ")  # Ask the user for a file name
    
    unsolved_maze = copy.deepcopy(solver)  # Create a copy of the maze
    
    solver.backtracking_solver()  # Solve the maze
    
    file_path = os.path.join(output_dir, file_name)  # Construct the path to the file
    
    with open(file_path, 'w') as output:  # Save the original maze to the file
        output.write("Original Maze:\n")
        for row in unsolved_maze.board:
            output.write(' '.join(row) + '\n')
    
    with open(file_path, 'a') as output:  # Save the maze solution to the file
        output.write("\nSolution:\n")
        for row in solver.board:
            output.write(' '.join(row) + '\n')
    
    print("Solution saved to", file_path)