computer_choice = 'scissor'
user_input = input("Enter your choice (rock, paper, scissor): ")

if user_input == computer_choice:
    print("It's a tie!")
elif user_input == 'rock' and computer_choice == 'scissor':
    print("You win! Rock beats scissor.")
elif user_input == 'paper' and computer_choice == 'rock':
    print("You win! Paper beats rock.") 
elif user_input == 'scissor' and computer_choice == 'paper':
    print("You win! Scissor beats paper.")
else:
    print("You lose! Computer wins.")