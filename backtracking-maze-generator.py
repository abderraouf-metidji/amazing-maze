import random

class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {'N': True, 'E': True, 'S': True, 'W': True}
        self.visited = False

    def break_wall(self, direction, next_cell):
        opposite_direction = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
        self.walls[direction] = False
        next_cell.walls[opposite_direction[direction]] = False

class Maze:
    def __init__(self, name, n):
        self.name = name
        self.n = n
        self.board = [[Cell(x, y) for y in range(self.n)] for x in range(self.n)]

    def backtrack(self, current_cell):
        current_cell.visited = True
        stack = [current_cell]
        i = 0
    
        while i < self.n ** 2:
            neighbors = self.check_neighbors(current_cell)
            unvisited_neighbors = [cell for cell in neighbors if not cell[0].visited]
            if unvisited_neighbors:
                next_cell, direction = random.choice(unvisited_neighbors)
                current_cell.break_wall(direction, next_cell)
                next_cell.visited = True
                stack.append(next_cell)
                current_cell = next_cell
            else:
                if stack:
                    current_cell = stack.pop()  # Backtrack when there are no unvisited neighbors
                    i -= 1
            
            i += 1

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
                if self.board[row][col].visited:
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

if __name__ == "__main__":
    n = int(input("Enter the size of the maze: "))
    maze = Maze("maze", n)
    maze.backtrack(maze.board[0][0])
    maze.print_maze()