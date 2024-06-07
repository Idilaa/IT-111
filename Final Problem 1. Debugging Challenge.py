import random

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def print_dice(dice):
    for i, die in enumerate(dice, start=1):
        print(f"Die {i}: {die}")

def main():
    num_dice = 5
    dice = roll_dice(num_dice)

    print("Roll 1")
    print_dice(dice)

    hold_dice = []
    for i in range(1, num_dice + 1):
        choice = input(f"Hold Die {i}?  y/n ")
        if choice.lower() == 'y':
            hold_dice.append(i)

    dice = [random.randint(1, 6) if i not in hold_dice else die for i, die in enumerate(dice, start=1)]

    print("\nRoll 2")
    print_dice(dice)

    # Prompt for holding dice after the second roll
    for i in range(1, num_dice + 1):
        choice = input(f"Hold Die {i}?  y/n ")

if __name__ == "__main__":
    main()
