import random
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.games.common import get_bet
from src.wallet import Wallet

def blackjack(wallet: Wallet):
    balance = wallet.user.get_balance()
    bet = get_bet(balance)
    def deal_card():
        return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

    def hand_value(hand):
        value = sum(hand)
        aces = hand.count(11)
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    player = [deal_card(), deal_card()]
    dealer = [deal_card(), deal_card()]
    print("Dealer shows:", dealer[0])
    print("Your hand:", player, f"(= {hand_value(player)})")

    while hand_value(player) < 21:
        move = input("Hit or Stand? (h/s): ").strip().lower()
        if move == 'h':
            player.append(deal_card())
            print("Your hand:", player, f"(= {hand_value(player)})")
        else:
            break

    pval = hand_value(player)
    if pval > 21:
        print("Bust! Dealer wins.")
        wallet.process_deduction(bet)
        return
    print("Dealer's hand:", dealer)
    while hand_value(dealer) < 17:
        dealer.append(deal_card())
    dval = hand_value(dealer)
    print("Dealer's final hand:", dealer, f"(= {dval})")
    if dval > 21 or pval > dval:
        print("You win!")
        wallet.process_win(bet)
    elif pval == dval:
        print("Push!")
    else:
        print("Dealer wins")
        wallet.process_deduction(bet)