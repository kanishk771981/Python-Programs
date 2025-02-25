import random

# Function to determine wins and bets
def gambler(stake, goal):
    wins = 0
    bets = 0

    while 0 < stake < goal:
        bets += 1
        if random.random() < 0.5:
            stake += 1
            wins += 1
        else:
            stake -= 1

    return wins, bets

# Function to calculate win & loss percentages
def percentage(stake, goal, trials):
    total_wins = 0
    total_bets = 0

    for _ in range(trials):
        wins, bets = gambler(stake, goal)
        total_wins += wins
        total_bets += bets

    average_wins = total_wins / trials if trials > 0 else 0
    win_percentage = (total_wins / total_bets) * 100 if total_bets > 0 else 0
    loss_percentage = 100 - win_percentage  # Fix loss percentage calculation

    return average_wins, win_percentage, loss_percentage

# Taking user input
stake = int(input("Enter initial stake: "))
goal = int(input("Enter the goal amount: "))
trials = int(input("Enter the number of trials: "))

# Running the function
average_wins, win_percentage, loss_percentage = percentage(stake, goal, trials)

# Printing results
print(f"Average number of wins: {average_wins:.2f}")
print(f"Win percentage: {win_percentage:.2f}%")
print(f"Loss percentage: {loss_percentage:.2f}%")



        

         

    

  
