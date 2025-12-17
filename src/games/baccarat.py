import random
import sys
import os

from src.games.common import get_bet
from src.wallet import Wallet


def baccarat(wallet: Wallet):
    """Standard Baccarat (Punto Banco) with proper third-card rules"""
    balance = wallet.user.get_balance()
    print("\n === BACCARAT === ")
    print("Bet on Player, Banker, or Tie")
    print("Payouts: Player 1:1, Banker 0.95:1 (5% commission), Tie 8:1")

    bet = get_bet(balance, minimum=50)
    print("\n[1] Bet on Player")
    print("[2] Bet on Banker")
    print("[3] Bet on Tie")
    choice = input("Your bet: ").strip()

    if choice not in ['1', '2', '3']:
        print("Invalid choice!")
        return

    # Deal initial two cards
    def deal_card():
        card = random.randint(1, 13)
        # Face cards (J, Q, K) and 10 count as 0
        return 0 if card >= 10 else card

    def hand_value(cards):
        return sum(cards) % 10

    player_cards = [deal_card(), deal_card()]
    banker_cards = [deal_card(), deal_card()]

    player_total = hand_value(player_cards)
    banker_total = hand_value(banker_cards)

    print(f"\nPlayer: {player_cards[0]} + {player_cards[1]} = {player_total}")
    print(f"Banker: {banker_cards[0]} + {banker_cards[1]} = {banker_total}")

    # Check for naturals (8 or 9)
    if player_total >= 8 or banker_total >= 8:
        print("Natural! No more cards drawn.")
    else:
        # Player draws third card if total is 0-5
        player_third = None
        if player_total <= 5:
            player_third = deal_card()
            player_cards.append(player_third)
            player_total = hand_value(player_cards)
            print(f"Player draws: {player_third} (new total: {player_total})")
        else:
            print("Player stands.")

        # Banker draws based on complex rules
        banker_draws = False

        if player_third is None:
            # Player didn't draw - banker draws on 0-5
            if banker_total <= 5:
                banker_draws = True
        else:
            # Player drew - banker follows tableau
            if banker_total <= 2:
                banker_draws = True
            elif banker_total == 3:
                banker_draws = (player_third != 8)
            elif banker_total == 4:
                banker_draws = (player_third in [2, 3, 4, 5, 6, 7])
            elif banker_total == 5:
                banker_draws = (player_third in [4, 5, 6, 7])
            elif banker_total == 6:
                banker_draws = (player_third in [6, 7])

        if banker_draws:
            banker_third = deal_card()
            banker_cards.append(banker_third)
            banker_total = hand_value(banker_cards)
            print(f"Banker draws: {banker_third} (new total: {banker_total})")
        else:
            print("Banker stands.")

    # Final totals
    print(f"\n--- FINAL ---")
    print(f"Player: {' + '.join(map(str, player_cards))} = {player_total}")
    print(f"Banker: {' + '.join(map(str, banker_cards))} = {banker_total}")

    # Determine winner
    if player_total > banker_total:
        result = "player"
        print("\nPlayer wins!")
    elif banker_total > player_total:
        result = "banker"
        print("\nBanker wins!")
    else:
        result = "tie"
        print("\nIt's a tie!")

    # Process winnings
    if result == "tie":
        if choice == "3":
            wallet.process_win(bet * 8)
        else:
            print(f"Push! Your ${bet} bet is returned")
    elif choice == '1' and result == "player":
        wallet.process_win(bet)
    elif choice == '2' and result == "banker":
        winnings = int(bet * 0.95)  # 5% commission
        wallet.process_win(winnings)
    else:
        wallet.process_deduction(bet)


if __name__ == "__main__":
    # For testing purposes
    print("Run this from the main menu!")

