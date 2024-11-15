# Vaccume cleaner Code 
def vacuum_world():
    # Initialize goal state
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    # User inputs for the vacuum's location and status
    location_input = input("Enter Location of Vacuum (A/B): ").strip().upper()
    status_input = input(f"Enter status of {location_input} (0: Clean, 1: Dirty): ").strip()
    other_location = 'B' if location_input == 'A' else 'A'
    status_input_complement = input(f"Enter status of {other_location} (0: Clean, 1: Dirty): ").strip()

    print("Initial Location Condition:", goal_state)

    def clean_room(room):
        """Cleans the specified room and updates the cost."""
        nonlocal cost
        goal_state[room] = '0'
        cost += 1  # Cost for sucking dirt
        print(f"Location {room} has been cleaned.")

    def move_to_room(room):
        """Moves to the specified room and updates the cost."""
        nonlocal cost
        cost += 1  # Cost for moving
        print(f"Moving to Location {room}.")

    # Start cleaning based on the location input
    if location_input == 'A':
        if status_input == '1':
            print("Location A is Dirty.")
            clean_room('A')

        if status_input_complement == '1':
            print("Location B is Dirty.")
            move_to_room('B')
            clean_room('B')
        elif status_input == '0' and status_input_complement == '0':
            print("Both locations are clean.")

    elif location_input == 'B':
        if status_input == '1':
            print("Location B is Dirty.")
            clean_room('B')

        if status_input_complement == '1':
            print("Location A is Dirty.")
            move_to_room('A')
            clean_room('A')
        elif status_input == '0' and status_input_complement == '0':
            print("Both locations are clean.")

    # Output final state and cost
    print("GOAL STATE:", goal_state)
    print("Performance Measurement:", cost)

vacuum_world()
