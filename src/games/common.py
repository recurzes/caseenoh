def get_bet(balance, minimum=50):
    while True:
        try:
            bet = int(input(f"Your balance: ${balance}. Enter bet (min ${minimum}): "))

            if minimum <= bet <= balance:
                return bet
            print("Invalid bet.")

        except ValueError:
            print("Enter a valid integer bet")
