MAX_LINES = 3
MAX_BET = 325
MIN_BET = 25

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: 
                print("Amount must be greater than 0")
        else:
            print("Amount must be a number")

    return amount

def grab_number_of_lines():
    while True:
        lines = input("Enter the amount of lines to bet on (1-"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else: 
                print("Enter a valid number of lines")
        else:
            print("Amount must be a number")

    return lines

def get_bet():
    while True:
        amount = input("What's your bet on the lines? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: 
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Amount must be a number")

    return amount

def main():
    balance = deposit()
    lines = grab_number_of_lines()
    bet = get_bet()
    total_bet = lines * bet
    print(f"You are betting ${bet} on {lines} lines. Total bet: ${total_bet}")

main()
