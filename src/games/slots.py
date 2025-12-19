import random

from src.wallet import Wallet


def slots(wallet: Wallet):
    """Slot machine integrated with Wallet service.

    Uses Wallet for balance reads and updates. Interactive; returns when
    player runs out of money or chooses to stop by entering 0 at the bet prompt.
    """
    symbols = ["🍒", "🍋", "🔔", "⭐", "💎"]

    print("🎰 WELCOME TO SLOT MACHINE 🎰")

    while True:
        balance = wallet.user.get_balance()
        print(f"\n💰 Current Balance: {balance}")

        if balance <= 0:
            print("❌ You are out of money!")
            break

        # Use inline input validation; allow 0 to quit like the old implementation
        try:
            raw = input(f"Your balance: ${balance}. Enter bet (min $1, 0 to quit): ")
            bet = int(raw)
        except ValueError:
            print("❌ Invalid input")
            continue

        if bet == 0:
            print("Thank you for playing slots!")
            break

        if bet < 1 or bet > balance:
            print("❌ Invalid bet amount")
            continue

        # Deduct bet immediately
        wallet.process_deduction(bet)

        spin = random.choices(symbols, k=3)

        print("\nSpinning...")
        print("==============================")
        print(f"| {spin[0]} | {spin[1]} | {spin[2]} |")
        print("==============================")

        # RESULTS
        if spin[0] == spin[1] == spin[2]:
            win = bet * 10
            print(f"💥 JACKPOT! +{win}")
            wallet.process_win(win)

        elif len(set(spin)) == 2:
            win = bet * 3
            print(f"🎉 TWO MATCHES! +{win}")
            wallet.process_win(win)

        else:
            print("😢 No win")

        print(f"💰 Updated Balance: {wallet.user.get_balance()}")
