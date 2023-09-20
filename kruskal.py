import random
from random import randint

class Cell:
    def __init__(self, x, y, number=None):
        self.x = x
        self.y = y
        self.walls = {'N': True, 'E': True, 'S': True, 'W': True}
        self.number = number

    def break_wall(self, direction, next_cell):
        opposite_direction = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
        self.walls[direction] = False
        next_cell.walls[opposite_direction[direction]] = False

class Maze:
    def __init__(self, name, n):
        self.name = name
        self.n = n
        self.board = [[Cell(x, y) for y in range(self.n)] for x in range(self.n)]
        self.cell_value()  # Initialize cell values sequentially

    def cell_value(self):
        value = 0
        for row in range(self.n):
            for col in range(self.n):
                self.board[row][col].number = value
                value += 1

    def kruskal(self):
        while not self.all_cells_connected():
            current_cell = self.board[randint(0, self.n - 1)][randint(0, self.n - 1)]
            neighbors = self.check_neighbors(current_cell)

            for neighbor, direction in neighbors:
                if neighbor.number != current_cell.number:
                    current_cell.break_wall(direction, neighbor)
                    new_number = min(current_cell.number, neighbor.number)
                    self.update_numbers(current_cell, neighbor, new_number)

    def all_cells_connected(self):
        # Check if all cells have the same number
        first_cell_number = self.board[0][0].number
        return all(cell.number == first_cell_number for row in self.board for cell in row)

    def update_numbers(self, current_cell, neighbor_cell, new_number):
        # Update the numbers of connected cells
        for row in self.board:
            for cell in row:
                if cell.number == max(current_cell.number, neighbor_cell.number):
                    cell.number = new_number

    def check_neighbors(self, current_cell):
        neighbors = []
        if current_cell.x > 0:
            neighbors.append((self.board[current_cell.x - 1][current_cell.y], 'N'))
        if current_cell.x < self.n - 1:
            neighbors.append((self.board[current_cell.x + 1][current_cell.y], 'S'))
        if current_cell.y > 0:
            neighbors.append((self.board[current_cell.x][current_cell.y - 1], 'W'))
        if current_cell.y < self.n - 1:
            neighbors.append((self.board[current_cell.x][current_cell.y + 1], 'E'))
        return neighbors

    def print_maze(self):
        maze_display = [["#" for _ in range(2 * self.n + 1)] for _ in range(2 * self.n + 1)]
        for row in range(self.n):
            for col in range(self.n):
                maze_display[2 * row + 1][2 * col + 1] = "."
                if self.board[row][col].walls['N']:
                    maze_display[2 * row][2 * col + 1] = "#"
                else:
                    maze_display[2 * row][2 * col + 1] = "."
                if self.board[row][col].walls['S']:
                    maze_display[2 * row + 2][2 * col + 1] = "#"
                else:
                    maze_display[2 * row + 2][2 * col + 1] = "."
                if self.board[row][col].walls['W']:
                    maze_display[2 * row + 1][2 * col] = "#"
                else:
                    maze_display[2 * row + 1][2 * col] = "."
                if self.board[row][col].walls['E']:
                    maze_display[2 * row + 1][2 * col + 2] = "#"
                else:
                    maze_display[2 * row + 1][2 * col + 2] = "."
        maze_display[0][0] = "."
        maze_display[1][0] = "."
        maze_display[2 * self.n][2 * self.n] = "."
        maze_display[2 * self.n - 1][2 * self.n] = "."
        maze_str = ""
        for line in maze_display:
            maze_str += "".join(line) + "\n"
        print(maze_str)
        return maze_str

    def print_cell_numbers(self):
        for row in range(self.n):
            for col in range(self.n):
                print(f"Cell ({row}, {col}) - Number: {self.board[row][col].number}")

    def save_maze_to_txt(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)

if __name__ == "__main__":
    n = int(input("Enter the size of the maze: "))
    maze = Maze("maze", n)
    maze.kruskal()
    maze_str = maze.print_maze()
    maze.print_cell_numbers()
    maze.save_maze_to_txt('maze.txt', maze_str)
