import random

def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        roll_result = random.randint(1, 6)
        results.append(roll_result)
    return results

def main():
    print("Welcome to the Dice Rolling App!")

    while True:
        num_dice = int(input("How many dice do you want to roll? "))
        if num_dice <= 0:
            print("Please enter a valid number of dice.")
            continue
        
        dice_results = roll_dice(num_dice)
        print("Dice roll result:")
        for i, result in enumerate(dice_results):
            print(f"Die {i + 1}: {result}")

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for using the Dice Rolling App!")
            break

if __name__ == "__main__":
    main()