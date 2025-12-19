from auth import Authentication
from src.wallet import Wallet
import profile
import sys
import time

from src.games import blackjack, slots, baccarat

auth_service = Authentication()
wallet_service = None
profile_service = profile.Profile(auth_service)

def pause():
    input("\nPress Enter to continue...")

def invalid_option():
    print("\n❌ Invalid option! Try again.")
    time.sleep(1)

def login_menu():
    global wallet_service
    while True:
        print("\n+------------------------------+")
        print("|     CASINO APP: SIGN IN      |")
        print("+------------------------------+")
        print("|  [1] Sign-in                 |")
        print("|  [2] Register                |")
        print("|  [0] Exit Application        |")
        print("+------------------------------+")
        choice = input("Choice: ")

        if choice == '1':
            u = input("Username: ")
            p = input("Password: ")

            if auth_service.login(u, p):
                wallet_service = Wallet.initialize(auth_service.current_user)
                main_menu()
            else:
                pause()

        elif choice == '2':
            name = input("Name: ")
            last = input("Last Name: ")

            print("==Birth Date==")
            b_day = [
                int(input("Month(1 - 12): ")),
                int(input("Day: ")),
                int(input("Year(ex.2006): "))
            ]

            u = input("New Username: ")
            p = input("New Password: ")
            c = int(input("Contact No.: "))
            e = input("Email: ")

            auth_service.register(u, p, e, name, last, b_day, c)

        elif choice == '0':
            print("\nExiting...")
            sys.exit(0)

        else:
            invalid_option()

def game_menu():
    """Casino games selection menu"""
    while True:
        current_balance = auth_service.current_user.get_balance()
        print("\n+------------------------------+")
        print("|      CASINO GAMES            |")
        print("+------------------------------+")
        print(f"|  Balance: ${current_balance:,.2f}")
        print("+------------------------------+")
        print("|  [1] Blackjack               |")
        print("|  [2] Slots                   |")
        print("|  [3] Baccarat                |")
        print("|  [0] Back to Main Menu       |")
        print("+------------------------------+")

        choice = input("Choose a game: ")

        if choice == "1":
            blackjack.blackjack(wallet_service)
        elif choice == "2":
            slots.slots(wallet_service)
        elif choice == "3":
            baccarat.baccarat(wallet_service)
        elif choice == "0":
            return
        else:
            invalid_option()

def main_menu():
    while True:
        print("")
        auth_service.profile()
        print("[1] Play")
        print("[2] Deposit")
        print("[3] Profile")
        print("[0] Exit")

        choice = input("Choice: ")

        if choice == "1":
            game_menu()

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            wallet_service.process_deposit(
                amount
            )

        elif choice == "3":
            profile_menu()

        elif choice == "0":
            Wallet.clear()
            auth_service.logout()
            break

        else:
            invalid_option()

def profile_menu():
    while True:
        print("")
        auth_service.get_profile_info()
        print("[1] Update Profile")
        print("[2] Delete Account")
        print("[0] Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            update_profile_menu()

        elif choice == "2":
            sure = input("Sure ka? (Y/N): ").upper()
            if sure == "Y":
                profile_service.delete_account()
                print("\nExiting...")
                sys.exit(0)

        elif choice == "0":
            return

        else:
            invalid_option()

def update_profile_menu():
    while True:
        print("\n+------------------------------------+")
        print("|          UPDATE PROFILE            |")
        print("+------------------------------------+")
        print("|  [1] Username                      |")
        print("|  [2] Password                      |")
        print("|  [3] Email                         |")
        print("|  [4] First Name                    |")
        print("|  [5] Last Name                     |")
        print("|  [6] Birth Date                    |")
        print("|  [7] Contact No                    |")
        print("|  [0] Exit                          |")
        print("+------------------------------------+")
        type = int(input("Enter choice: "))

        if type == 0:
            return

        if type in (1, 2, 3, 4, 5):
            value = input("Enter value: ")

        elif type == 7:
            value = int(input("Enter new Phone.No: "))

        elif type == 6:
            value = [
                int(input("Month(1 - 12): ")),
                int(input("Day: ")),
                int(input("Year(ex.2006): "))
            ]

        else:
            invalid_option()
            continue

        profile_service.update_profile(value, type)
        return
