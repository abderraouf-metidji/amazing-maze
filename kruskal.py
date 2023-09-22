import random

class Cell:
    def __init__(self, x, y, number=None):
        """
        Initialize a cell with its coordinates (x, y) and an optional number.
        """
        self.x = x
        self.y = y
        self.walls = {'N': True, 'E': True, 'S': True, 'W': True}  # Boolean values representing the presence of walls
        self.number = number  # Optional number assigned to the cell

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
        self.cell_value()  # Initialize cell values sequentially

    def cell_value(self):
        """
        Assign a sequential number to each cell in the maze.
        """
        value = 0
        for row in self.board:
            for cell in row:
                cell.number = value
                value += 1

    def kruskal(self):
        """
        Generate the maze using the Kruskal's algorithm.
        """
        while not self.all_cells_connected():
            current_cell = self.board[random.randint(0, self.n - 1)][random.randint(0, self.n - 1)]  # Choose a random cell
            neighbors = self.check_neighbors(current_cell)  # Get the neighboring cells
            for neighbor, direction in neighbors:
                if neighbor.number != current_cell.number:  # Check if the cells belong to different sets
                    current_cell.break_wall(direction, neighbor)  # Break the wall between the current cell and the neighbor
                    new_number = min(current_cell.number, neighbor.number)  # Update the set number
                    self.update_numbers(current_cell, neighbor, new_number)  # Update the set numbers in the maze

    def all_cells_connected(self):
        """
        Check if all cells in the maze are connected.
        """
        first_cell_number = self.board[0][0].number
        return all(cell.number == first_cell_number for row in self.board for cell in row)

    def update_numbers(self, current_cell, neighbor_cell, new_number):
        """
        Update the set numbers in the maze.
        """
        to_update = []
        for row in self.board:
            for cell in row:
                if cell.number == max(current_cell.number, neighbor_cell.number):
                    to_update.append(cell)
        for cell in to_update:
            cell.number = new_number

    def check_neighbors(self, current_cell):
        """
        Get the neighboring cells of the current cell.
        """
        neighbors = []
        directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
        for direction, (dx, dy) in directions.items():
            nx, ny = current_cell.x + dx, current_cell.y + dy
            if 0 <= nx < self.n and 0 <= ny < self.n:
                neighbors.append((self.board[nx][ny], direction))
        return neighbors

    def print_maze(self):
        """
        Generate a string representation of the maze.
        """
        maze_display = [["#" for _ in range(2 * self.n + 1)] for _ in range(2 * self.n + 1)]  # 2D array to represent the maze
        for row in range(self.n):
            for col in range(self.n):
                maze_display[2 * row + 1][2 * col + 1] = "."  # Cells are represented by '.'
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

    def save_maze_to_txt(self, filename):
        """
        Save the maze to a text file.
        """
        with open(filename, 'w') as file:
            file.write(self.print_maze())

if __name__ == "__main__":
    n = int(input("Enter the size of the maze: "))  # User input for maze size
    maze = Maze("maze", n)  # Create a maze object
    maze.kruskal()  # Generate the maze using Kruskal's algorithm
    maze_str = maze.print_maze()  # Generate the string representation of the maze
    maze.save_maze_to_txt('maze.txt')  # Save the maze to a text file