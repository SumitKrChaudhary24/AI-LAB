#8 Puzzle program Solution

def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def find_empty_tile(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def is_goal_state(board):
    return board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def get_neighbors(board):
    x, y = find_empty_tile(board)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_board = [row[:] for row in board]
            new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
            neighbors.append(new_board)
    return neighbors

def bfs(initial_board):
    queue = [(initial_board, 0, [])]
    visited = set()

    while queue:
        current_board, moves, path = queue.pop(0)
        if is_goal_state(current_board):
            return moves, path + [current_board]
        visited.add(tuple(map(tuple, current_board)))

        for neighbor in get_neighbors(current_board):
            if tuple(map(tuple, neighbor)) not in visited:
                queue.append((neighbor, moves + 1, path + [current_board]))

    return -1, []

# Function to get user input
def get_user_input():
    print("Enter the 8-puzzle configuration (use 0 for the empty space):")
    user_input = input("Example: 1 2 3 4 0 6 7 5 8\n")
    tiles = list(map(int, user_input.split()))
   
    if len(tiles) != 9:
        raise ValueError("Please enter exactly 9 numbers.")
   
    return [tiles[i:i + 3] for i in range(0, 9, 3)]

# Example usage
if __name__ == "__main__":
    try:
        initial_board = get_user_input()
        print("Initial Board:")
        print_board(initial_board)
        moves, solution_path = bfs(initial_board)

        if moves != -1:
            print(f"Solved in {moves} moves.\nSolution path:")
            for step in solution_path:
                print_board(step)
        else:
            print("No solution found.")
    except ValueError as e:
        print(e)
