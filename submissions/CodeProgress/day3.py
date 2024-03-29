import random

def adventure_game():
   
    print("Welcome to this world adventurer")

    while True:
        respond = input("Are you ready to engage on an adventure? (yes/no) ").lower()
        if respond == "yes":
            name = input("Please, enter your name: ")
            print(f"Hello {name}, Welcome to the Slime Slayer!")
            break
        elif respond == "no":
            print("Come back again if you're ready.")
        else:
            print("Invalid input. Please answer 'yes' or 'no'.")

    print("You're walking in the plaza and you encounter a boy being chased by a slime.")
    print("What will you do?")
    print("1. Help the boy fight the slime.")
    print("2. Run away and ignore the situation.")

    choice = input("> ")

    if choice == "1":
        print("You decide to help the boy fight the slime.")
        print("You pick up a stick nearby and engage in combat!")
        combat_result = fight_slime()
        if combat_result:
            print("You defeated the slime! The boy thanks you and offers a reward.")
            print("Congratulations, you win!")
        
    elif choice == "2":
        print("You decide to run away and ignore the situation. You continue your journey.")
        print("As you walk away, you can hear the boy screaming for help.")
        print("You feel a sense of guilt but continue forward.")
        print("Game Over.")
    else:
        print("Invalid choice. Game Over.")

def fight_slime():
    
    return random.choice([True, False])

adventure_game()