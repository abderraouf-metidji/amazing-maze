import random

class Solver:
    def __init__(self, file):
        self.file = file
        self.board = []
        self.wall = '#'
        self.route = '.'
        self.start = (0, 0)
        self.finish = None  # Finish cell will be set during maze loading

    def get_maze(self, file):
        with open(file, 'r') as file:
            for line in file:
                line = line.strip()
                row = list(line)

                self.board.append(row)
                
        # Set the finish cell to the last cell in the list
        self.finish = (len(self.board) - 1, len(self.board[0]) - 1)

    def backtracking_solver(self): 
        self.current_cell = self.start
        self.board[self.current_cell[0]][self.current_cell[1]] = "o"
        self.stack = []

        while self.current_cell != self.finish:
            neighbors = []

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

            if neighbors:
                # Choose a random neighbor
                next_cell = random.choice(neighbors)
                self.stack.append(self.current_cell)
                self.current_cell = next_cell
                self.board[self.current_cell[0]][self.current_cell[1]] = "o"
            else:
                if not self.stack:
                    print("No Solution")
                    break
                else:
                    self.board[self.current_cell[0]][self.current_cell[1]] = "*"
                    self.current_cell = self.stack.pop()

    def print_solution(self):
        # Print the maze with the solution
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[0])):
                if self.board[i][j] == "o":
                    print("o", end = " ")
                elif self.board[i][j] == "*":
                    print("*", end = " ")
                else:
                    print(self.board[i][j], end = " ")
            print()

if __name__ == "__main__":
    solver = Solver("maze.txt")
    solver.get_maze("maze.txt")
    solver.backtracking_solver()
    solver.print_solution()
