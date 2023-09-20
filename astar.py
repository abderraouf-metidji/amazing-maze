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

    def astar_solver(self):
        pass

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
    solver.astar_solver()
    solver.print_solution()