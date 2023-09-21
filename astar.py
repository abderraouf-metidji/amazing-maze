import os, copy, random, heapq
from collections import deque

class Node:
    def __init__(self, position, parent=None):
        """
        Initialize a node with its position and its parent node.
        """
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node to this node
        self.h = 0  # Heuristic (estimated cost from this node to goal)
        self.f = 0  # Total cost (f = g + h)
    
    def __lt__(self, other):
        """
        Compare two nodes based on their total cost.
        """
        return self.f < other.f

class Solver:
    def __init__(self):
        """
        Initialize a solver with a maze file, a board, a wall character, a route character, a start position and a finish position.
        """
        self.board = []
        self.wall = '#'
        self.route = '.'
        self.start = (0, 0)
        self.finish = None  # Finish cell will be set during maze loading
    
    def get_maze(self, file):
        """
        Load the maze from a file and set the finish position.
        """
        with open(file, 'r') as maze_file:
            self.board = [list(line.strip()) for line in maze_file]
        # Set the finish cell to the last cell in the list
        self.finish = (len(self.board) - 1, len(self.board[0]) - 1)
    
    def astar_solver(self):
        """
        Solve the maze using the A* algorithm.
        """
        start_node = Node(self.start)
        finish_node = Node(self.finish)
        open_set = []
        closed_set = set()
        heapq.heappush(open_set, (0, start_node, start_node.position))
        while open_set:
            _, current_node, current_position = heapq.heappop(open_set)
            if current_position == finish_node.position:
                return self.reconstruct_path(current_node)
            closed_set.add(current_position)
            for neighbor in self.get_neighbors(current_node):
                if neighbor.position in closed_set:
                    continue
                tentative_g = current_node.g + 1
                if (neighbor, neighbor.position) not in open_set or tentative_g < neighbor.g:
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(neighbor, finish_node)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current_node
                    heapq.heappush(open_set, (neighbor.f, neighbor, neighbor.position))
        return None
    
    def heuristic(self, node, finish_node):
        """
        Calculate the Manhattan distance heuristic between a node and the finish node.
        """
        return abs(node.position[0] - finish_node.position[0]) + abs(node.position[1] - finish_node.position[1])
    
    def get_neighbors(self, node):
        """
        Get the neighboring nodes of a node.
        """
        neighbors = deque()
        x, y = node.position
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(self.board) and 0 <= new_y < len(self.board[0]) and self.board[new_x][new_y] != self.wall:
                neighbors.append(Node((new_x, new_y), node))
        return list(neighbors)
    
    def reconstruct_path(self, current_node):
        """
        Reconstruct the path from the start node to the current node.
        """
        path = deque()
        while current_node is not None:
            x, y = current_node.position
            self.board[x][y] = 'o'  # Mark path with 'o'
            path.appendleft((x, y))
            current_node = current_node.parent
        return list(path)
    
    def print_solution(self):
        """
        Print the maze with the solution.
        """
        for row in self.board:
            print(' '.join(row))

if __name__ == "__main__":
    solver = Solver()  # Create a Solver object
    solver.get_maze("maze.txt")  # Load the maze from the file
    
    # Create the directory to store the maze solutions if it doesn't exist
    output_dir = "solved_mazes"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Ask the user for a file name
    file_name = input("Enter a file name to save the solution (add .txt): ")

    unsolved_maze = copy.deepcopy(solver)  # Create a copy of the maze

    # Solve the maze
    solver.astar_solver()
    
    # Construct the path to the file
    file_path = os.path.join(output_dir, file_name)

    # Save the original maze to the file
    with open(file_path, 'w') as output:
        output.write("Original Maze:\n")
        for row in unsolved_maze.board:
            output.write(' '.join(row) + '\n')

    # Save the maze solution to the file
    with open(file_path, 'a') as output:
        output.write("\nSolution:\n")
        for row in solver.board:
            output.write(' '.join(row) + '\n')

    print("Solution saved to", file_path)