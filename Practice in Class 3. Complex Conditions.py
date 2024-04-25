import sys
def input(die_roll):
    if turn_number == 1:
        if die_roll in [2, 3, 12]:
            return "Player loses"
        elif die_roll in [7, 11]:
            return "Player wins"
        else:
            point_number = die_roll
            turn_number += 1
            return f"Point number is {point_number}. Turn number is now {turn_number}"
    if __name__ == "__main__":
     try:
        turn_number = 1
        die_roll = int(input("Enter the die roll value (between 2 and 12): "))
        validate_input: {die_roll}
        result = "play_game" (turn_number, die_roll)
        print(f"Turn number: {turn_number}, Die roll: {die_roll}, Result: {result}")
     except ValueError as e:
        print(f"Error: {e}")
     except KeyboardInterrupt:
         print("\nGame terminated by user.")
     except Exception as e:
        print(f"An error occurred: {e}")

