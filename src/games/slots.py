import random
import sqlite3

# ---------------- DATABASE CONNECTION ----------------
def get_connection():
    return sqlite3.connect("/home/chrishian/Downloads/casino")

connection = get_connection()
cursor = connection.cursor()

# ---------------- CONSTANTS ----------------
USER_ID = 1  # Change if needed

# ---------------- DATABASE SETUP ----------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    balance REAL
)
""")

# Ensure user exists
cursor.execute("SELECT balance FROM users WHERE id = ?", (USER_ID,))
user = cursor.fetchone()

if user is None:
    cursor.execute(
        "INSERT INTO users (id, balance) VALUES (?, ?)",
        (USER_ID, 100.0)  # starting balance
    )
    connection.commit()

# ---------------- HELPER FUNCTIONS ----------------
def get_balance():
    cursor.execute(
        "SELECT balance FROM users WHERE id = ?",
        (USER_ID,)
    )
    result = cursor.fetchone()
    return result[0] if result else 0.0


def update_balance(amount):
    cursor.execute(
        "UPDATE users SET balance = balance + ? WHERE id = ?",
        (amount, USER_ID)
    )
    connection.commit()  # REAL-TIME SAVE

# ---------------- SLOT MACHINE ----------------
def slotMachine():
    symbols = ["🍒", "🍋", "🔔", "⭐", "💎"]

    print("🎰 WELCOME TO SLOT MACHINE 🎰")

    while True:
        balance = get_balance()
        print(f"\n💰 Current Balance: {balance}")

        if balance <= 0:
            print("❌ You are out of money!")
            break

        try:
            bet = float(input("Enter bet amount (0 to quit): "))
        except ValueError:
            print("❌ Invalid input")
            continue

        if bet == 0:
            print("Thank you for playing!")
            break

        if bet < 0 or bet > balance:
            print("❌ Invalid bet amount")
            continue

        # Deduct bet
        update_balance(-bet)

        spin = random.choices(symbols, k=3)

        print("\nSpinning...")
        print("==============================")
        print(f"| {spin[0]} | {spin[1]} | {spin[2]} |")
        print("==============================")

        # RESULTS
        if spin[0] == spin[1] == spin[2]:
            win = bet * 10
            print(f"💥 JACKPOT! +{win}")
            update_balance(win)

        elif len(set(spin)) == 2:
            win = bet * 3
            print(f"🎉 TWO MATCHES! +{win}")
            update_balance(win)

        else:
            print("😢 No win")

        print(f"💰 Updated Balance: {get_balance()}")

# ---------------- RUN ----------------
slotMachine()

print(f"\nFinal Balance: {get_balance()}")
connection.close()
