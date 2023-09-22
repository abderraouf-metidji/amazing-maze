import os
import copy
from PIL import Image, ImageDraw
from backtracking import Maze as BacktrackingMaze
from kruskal import Maze as KruskalMaze
from astar import Solver as AStarSolver
from backtracking_solver import Solver as BacktrackingSolver

# Define the colors for '*' and 'o' cells
color_dead_end = (255, 0, 0)  # Red for dead ends ('*')
color_path = (0, 255, 0)      # Green for path cells ('o')

def create_colored_maze_image(board):
    """
    Create an image representation of the maze with different colors for '*' and 'o' cells.
    """
    image = Image.new("RGB", (len(board[0]), len(board)))
    draw = ImageDraw.Draw(image)
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == '#':
                color = (255, 255, 255)  # White for walls ('#')
            elif board[y][x] == '*':
                color = color_dead_end
            elif board[y][x] == 'o':
                color = color_path
            else:
                color = (0, 0, 0)  # Black for other characters
            draw.rectangle(
                [(x, y), (x + 1, y + 1)],
                fill=color,
                outline=None
            )
    return image

def generate_maze(algorithm):
    """
    Generate a maze using the specified algorithm.
    """
    n = int(input("Enter the size of the maze: "))  # User input for maze size
    if algorithm == '1':
        maze = BacktrackingMaze("maze", n)  # Create a maze object using Backtracking
        maze.backtrack(maze.board[0][0])
        maze_str = maze.print_maze()
        maze.save_maze_to_txt('maze.txt', maze_str)
    elif algorithm == '2':
        maze = KruskalMaze("maze", n)  # Create a maze object using Kruskal
        maze.kruskal()
        maze_str = maze.print_maze()
        maze.save_maze_to_txt('maze.txt')

def solve_maze(algorithm):
    """
    Solve a maze using the specified algorithm.
    """
    solver = AStarSolver()  # Create an A* Solver object
    solver.get_maze("maze.txt")  # Load the maze from the file
    output_dir = "solved_mazes"  # Directory to store the maze solutions
    if not os.path.exists(output_dir):  # Create the directory if it doesn't exist
        os.makedirs(output_dir)
    file_name = input("Enter a file name to save the solution (add .txt): ")  # Ask the user for a file name
    folder_name = file_name.split(".")[0]  # Extract the folder name from the file name
    folder_path = os.path.join(output_dir, folder_name)  # Construct the path to the folder
    if not os.path.exists(folder_path):  # Create the folder if it doesn't exist
        os.makedirs(folder_path)
    unsolved_maze = copy.deepcopy(solver)  # Create a copy of the maze
    if algorithm == '1':
        solver = AStarSolver()  # Create an A* Solver object
        solver.get_maze("maze.txt")  # Load the maze from the file
        solver.astar_solver()  # Solve the maze using A* algorithm
    elif algorithm == '2':
        solver = BacktrackingSolver()  # Create a Backtracking Solver object
        solver.get_maze("maze.txt")  # Load the maze from the file
        solver.backtracking_solver()  # Solve the maze using Backtracking
    file_path = os.path.join(folder_path, file_name)  # Construct the path to the txt file
    with open(file_path, 'w') as output:  # Save the original maze to the file
        output.write("Original Maze:\n")
        for row in unsolved_maze.board:
            output.write(' '.join(row) + '\n')
    with open(file_path, 'a') as output:  # Save the maze solution to the file
        output.write("\nSolution:\n")
        for row in solver.board:
            output.write(' '.join(row) + '\n')
    print("Solution saved to", file_path)
    # Create an image representation of the solved maze with different colors
    maze_image = create_colored_maze_image(solver.board)
    image_path = os.path.join(folder_path, "solved_maze.png")  # Construct the path to the jpg file
    maze_image.save(image_path)  # Save the image
    maze_image.show()  # Display the image

if __name__ == "__main__":
    while True:
        print("Select an option:")
        print("1. Generate a maze")
        print("2. Solve a maze")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            print("Select a maze generation algorithm:")
            print("1. Backtracking")
            print("2. Kruskal")
            generation_algorithm = input("Enter your choice (1/2): ")
            generate_maze(generation_algorithm)
        elif choice == '2':
            print("Select a maze solving algorithm:")
            print("1. A*")
            print("2. Backtracking")
            solving_algorithm = input("Enter your choice (1/2): ")
            solve_maze(solving_algorithm)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")