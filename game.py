import argparse
from deck import *


def calculate_sum(cards):
    ordered_cards = sorted(cards, key=lambda x: x.value, reverse=True)
    total = 0

    for c in ordered_cards:
        if c.value in [11, 12, 13]:
            total += 10
        elif c.value == 1:
            # handle when J, A, A == 22 should be 12 instead
            if c == ordered_cards[-1] and total + 11 <= 21:
                total += 11
            else:
                total += 1
        else:
            total += c.value

    return total


def process_dealer_hand(card_deck, cards):
    dealer_total = calculate_sum(cards)

    while dealer_total < 17:
        cards.append(card_deck.cards.pop(0))
        print(f'Dealer will hit and draws {cards[-1]}')
        dealer_total = calculate_sum(cards)

    print('Dealer will stay.')


def decide_winner(dealer_cards, player_cards):
    player_total = calculate_sum(player_cards)
    dealer_total = calculate_sum(dealer_cards)

    if dealer_total == 21 and len(dealer_cards) == 2:
        if player_total == 21 and len(player_cards) == 2:
            print('Both the dealer and you have blackjack. YOU WIN!!')
            return True
        else:
            print('Dealer has blackjack!. YOU LOSE!')
            return False
    elif player_total == 21 and len(player_cards) == 2:
        if dealer_total > 21:
            print(f'You have blackjack and the dealer busted with {dealer_total}. YOU WIN!!')
        else:
            print(f'You have blackjack and the dealer has {dealer_total}. YOU WIN!!')

        return True
    elif dealer_total > 21:
        print(f'You have {player_total} and the dealer busted with {dealer_total}. YOU WIN!!')
        return True
    elif player_total > dealer_total:
        print(f'You have {player_total} and the dealer has {dealer_total}. YOU WIN!!')
        return True
    elif player_total < dealer_total:
        print(f'You have {player_total} and the dealer has {dealer_total}. YOU LOSE!')
        return False
    elif player_total == dealer_total:
        print(f'Both the dealer and you have {dealer_total}. You pushed.')
        return False


def main():
    parser = argparse.ArgumentParser(description='Play blackjack.')
    parser.add_argument('-d', '--decks', default=1, type=int, choices=range(1, 9), help='number of decks to use')

    args = parser.parse_args()
    deck = Deck(args.decks)
    total_hands, hands_won = 0, 0
    while True:
        deck.shuffle()
        user_input = input('Enter \'p\' to play or \'q\' to quit: ')
        if user_input == 'p':
            total_hands += 1
            player_hand, dealer_hand = [], []

            # Deal out the cards
            player_hand.append(deck.cards.pop(0))
            dealer_hand.append(deck.cards.pop(0))
            player_hand.append(deck.cards.pop(0))
            dealer_hand.append(deck.cards.pop(0))
            player_hand_str = 'Your are dealt '
            player_hand_str += ', '.join(str(card) for card in player_hand)

            print(f'{player_hand_str}. The dealer has {dealer_hand[0]}.')
            player_hand_total = calculate_sum(player_hand)

            while player_hand_total <= 21:
                user_input = input('Enter \'h\' to hit or \'s\' to stay: ')
                if user_input.lower() == 'h':
                    player_hand.append(deck.cards.pop(0))
                    player_hand_total = calculate_sum(player_hand)
                    print(f'You are dealt {player_hand[-1]}')
                else:
                    break

            if player_hand_total > 21:
                print(f'You busted with total of {player_hand_total}. YOU LOSE!')
            else:
                print(f'Dealer flips card over with {dealer_hand[-1]}')

                # handle if dealer has blackjack
                process_dealer_hand(deck, dealer_hand)
                if decide_winner(dealer_hand, player_hand):
                    hands_won += 1

        else:
            print(f'You have won {hands_won} out of {total_hands} total hands played.')
            break


if __name__ == '__main__':
    main()
