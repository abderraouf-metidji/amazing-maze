import random
import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node to this node
        self.h = 0  # Heuristic (estimated cost from this node to goal)
        self.f = 0  # Total cost (f = g + h)

    def __lt__(self, other):
        return self.f < other.f

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
        start_node = Node(self.start)
        finish_node = Node(self.finish)
        
        open_set = []
        closed_set = set()
        
        heapq.heappush(open_set, (0, start_node))
        
        while open_set:
            _, current_node = heapq.heappop(open_set)
            
            if current_node.position == finish_node.position:
                return self.reconstruct_path(current_node)
            
            closed_set.add(current_node.position)
            
            for neighbor in self.get_neighbors(current_node):
                if neighbor.position in closed_set:
                    continue
                
                tentative_g = current_node.g + 1
                
                if neighbor not in [node for _, node in open_set] or tentative_g < neighbor.g:
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(neighbor, finish_node)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current_node
                    
                    heapq.heappush(open_set, (neighbor.f, neighbor))
        
        return None

    def heuristic(self, node, finish_node):
        # Manhattan distance heuristic
        return abs(node.position[0] - finish_node.position[0]) + abs(node.position[1] - finish_node.position[1])

    def get_neighbors(self, node):
        neighbors = []
        x, y = node.position
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(self.board) and 0 <= new_y < len(self.board[0]) and self.board[new_x][new_y] != self.wall:
                neighbors.append(Node((new_x, new_y), node))
        
        return neighbors

    def reconstruct_path(self, current_node):
        path = []
        while current_node is not None:
            x, y = current_node.position
            self.board[x][y] = 'o'  # Mark path with 'o'
            path.append((x, y))
            current_node = current_node.parent
        return path[::-1]

    def print_solution(self):
        # Print the maze with the solution
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[0])):
                print(self.board[i][j], end=" ")
            print()

if __name__ == "__main__":
    solver = Solver("maze.txt")
    solver.get_maze("maze.txt")
    path = solver.astar_solver()
    
    if path:
        print("Solution found:")
        solver.print_solution()
    else:
        print("No solution found.")
