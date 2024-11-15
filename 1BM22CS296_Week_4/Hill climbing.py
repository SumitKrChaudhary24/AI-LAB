mport random

def fitness(board):
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def generate_random_state(n):
    return [random.randint(0, n-1) for _ in range(n)]

def get_neighbors(board):
    neighbors = []
    n = len(board)
    for row in range(n):
        for col in range(n):
            if board[row] != col:
                new_board = board[:]
                new_board[row] = col
                neighbors.append(new_board)
    return neighbors

def hill_climbing(n):
    current = generate_random_state(n)
    while True:
        neighbors = get_neighbors(current)
        next_state = min(neighbors, key=lambda board: fitness(board))
       
        if fitness(next_state) == 0:
            return next_state
       
        if fitness(next_state) >= fitness(current):
            return None
       
        current = next_state

# Example usage:
n = 5  # Size of the board (8 queens problem)
solution = hill_climbing(n)
if solution:
    print("Solution found:", solution)
else:
    print("No solution found")
