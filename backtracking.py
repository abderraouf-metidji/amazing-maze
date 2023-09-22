import random

class Cell:
    def __init__(self, x, y):
        """
        Initialize a cell with its coordinates (x, y).
        """
        self.x = x
        self.y = y
        self.walls = {'N': True, 'E': True, 'S': True, 'W': True}  # Boolean values representing the presence of walls
        self.visited = False  # Flag to track if the cell has been visited

    def break_wall(self, direction, next_cell):
        """
        Break the wall between the current cell and the next cell in the given direction.
        """
        opposite_direction = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}  # Mapping of opposite directions
        self.walls[direction] = False
        next_cell.walls[opposite_direction[direction]] = False


class Maze:
    def __init__(self, name, n):
        """
        Initialize a maze with a name and size n x n.
        """
        self.name = name
        self.n = n
        self.board = [[Cell(x, y) for y in range(self.n)] for x in range(self.n)]  # 2D array of cells representing the maze

    def backtrack(self, current_cell):
        """
        Generate the maze using the backtrack algorithm.
        """
        current_cell.visited = True
        stack = [current_cell]  # Stack to store the visited cells

        while stack:
            current_cell = stack[-1]
            neighbors = self.check_neighbors(current_cell)  # Get the neighboring cells
            unvisited_neighbors = [cell for cell in neighbors if not cell[0].visited]  # Filter unvisited neighbors

            if unvisited_neighbors:
                next_cell, direction = random.choice(unvisited_neighbors)  # Choose a random unvisited neighbor
                current_cell.break_wall(direction, next_cell)  # Break the wall between the current cell and the next cell
                next_cell.visited = True
                stack.append(next_cell)
            else:
                stack.pop()

    def check_neighbors(self, current_cell):
        """
        Get the neighboring cells of the current cell.
        """
        neighbors = []

        if current_cell.x > 0:
            neighbors.append((self.board[current_cell.x - 1][current_cell.y], 'N'))  # North neighbor
        if current_cell.x < self.n - 1:
            neighbors.append((self.board[current_cell.x + 1][current_cell.y], 'S'))  # South neighbor
        if current_cell.y > 0:
            neighbors.append((self.board[current_cell.x][current_cell.y - 1], 'W'))  # West neighbor
        if current_cell.y < self.n - 1:
            neighbors.append((self.board[current_cell.x][current_cell.y + 1], 'E'))  # East neighbor

        return neighbors

    def print_maze(self):
        """
        Generate a string representation of the maze.
        """
        maze_display = [["#" for _ in range(2 * self.n + 1)] for _ in range(2 * self.n + 1)]  # 2D array to represent the maze

        for row in range(self.n):
            for col in range(self.n):
                maze_display[2 * row + 1][2 * col + 1] = "."  # Cells are represented by '.'
                if self.board[row][col].visited:
                    maze_display[2 * row + 1][2 * col + 1] = "."  # Mark visited cells with '.'
                if self.board[row][col].walls['N']:
                    maze_display[2 * row][2 * col + 1] = "#"  # North walls are represented by '#'
                else:
                    maze_display[2 * row][2 * col + 1] = "."  # No north wall
                if self.board[row][col].walls['S']:
                    maze_display[2 * row + 2][2 * col + 1] = "#"  # South walls are represented by '#'
                else:
                    maze_display[2 * row + 2][2 * col + 1] = "."  # No south wall
                if self.board[row][col].walls['W']:
                    maze_display[2 * row + 1][2 * col] = "#"  # West walls are represented by '#'
                else:
                    maze_display[2 * row + 1][2 * col] = "."  # No west wall
                if self.board[row][col].walls['E']:
                    maze_display[2 * row + 1][2 * col + 2] = "#"  # East walls are represented by '#'
                else:
                    maze_display[2 * row + 1][2 * col + 2] = "."  # No east wall

        maze_display[0][0] = "."  # Start cell
        maze_display[1][0] = "."  # Start cell
        maze_display[2 * self.n][2 * self.n] = "."  # Finish cell
        maze_display[2 * self.n - 1][2 * self.n] = "."  # Finish cell

        maze_str = "\n".join(["".join(line) for line in maze_display])
        return maze_str

    def save_maze_to_txt(self, filename, content):
        """
        Save the maze to a text file.
        """
        with open(filename, 'w') as file:
            file.write(content)


if __name__ == "__main__":
    n = int(input("Enter the size of the maze: "))  # User input for maze size
    maze = Maze("maze", n)  # Create a maze object
    maze.backtrack(maze.board[0][0])  # Generate the maze starting from the top-left cell
    maze_str = maze.print_maze()  # Generate the string representation of the maze
    maze.save_maze_to_txt('maze.txt', maze_str)  # Save the maze to a text file