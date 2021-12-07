import random


def calculate_score(cards):
    """Returns the sum of all the cards"""
    if (sum(cards) == 21) and (len(cards) == 2):
        return 0

    if 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1

    return sum(cards)


def deal_card():
    """Returns a random card"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def compare(user_score, computer_score):
    """Compares the scores and returns the result."""
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "You lose, opponent has a blackjack."
    elif user_score == 0:
        return "You win with a blackjack."
    elif user_score > 21:
        return "You went over, you lose."
    elif computer_score > 21:
        return "Opponent went over, you win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


def start_blackjack():
    ai_cards = []
    player_cards = []
    
    # deal 2 cards to both the player and the AI
    for _ in range(2):
        player_cards.append(deal_card())
        ai_cards.append(deal_card())

    ai_score = calculate_score(ai_cards)
    player_score = calculate_score(player_cards)

    should_continue = True
    while should_continue:
        print(f"AI's first card: {ai_cards[0]}")
        print(f"Your cards: {player_cards} | score: {player_score}")

        if ai_score < 17:
            ai_cards.append(deal_card())

        if input("\nDo you want another card? ") == "yes":
            player_cards.append(deal_card())

        ai_score = calculate_score(ai_cards)
        player_score = calculate_score(player_cards)

        print(f"\nAI STATS:\t\tcards: {ai_cards} | score: {ai_score}")
        print(f"YOUR STATS:\t\tcards: {player_cards} | score: {player_score}\n")

        print(compare(player_score, ai_score))
        should_continue = False
    else:
        if input("\nDo you want to play again? enter 'yes' to do so: ").casefold() == "yes":
            start_blackjack()


start_blackjack()
