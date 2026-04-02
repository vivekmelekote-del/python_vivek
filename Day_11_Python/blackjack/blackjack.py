#Blackjack:
#It's also called 21
#It is to collect set of largest number cards without going over 21. If the sum of cards add upto 21, it's called BUST, which inturn means LOST.
#Jack : Queen : King = 10
#Ace can count as 1 or 11 for your total

# First dealer and player has 1 card each
# Once the dealer give 1 card each again, deler doesn't reveal it. But we can calculate what's out total.
# If we are close to 21, we can end the game. Otherwise, we continue
# Deler will again give a card each
# Now, we calculate and repeat untill eithr one loose.
from random import choice

def choose_a_card():
    """Return a random card value"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)

def get_new_cards(player, dealer):
    """Deal both user and computer a starting hand of 2 random card values"""
    player.clear()
    dealer.clear()
    for _ in range(2):
        player.append(choose_a_card())
        dealer.append(choose_a_card())
    # Reveal computer's first card to the user
    print(f"You have card {player} and dealer has card {dealer[0]}")

def replace_jack_with_1_on_condition(list):
    """If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead."""
    if sum(list) == 21 and len(list) == 2:
        return 0
    elif sum(list) > 21 and  11 in list:
        list.remove(11)
        list.append(1)
    return (sum(list))

def compaer(player, dealer):
    """Checks if the game is draw or who won"""
    if(player == dealer):
        return "draw"
    elif dealer == 0:
        return "Dealer won with blackjack"
    elif player == 0:
        return "Player won with blackjack"
    elif dealer > 21:
        return "Dealer lost, went beyond 21"
    elif player > 21:
        return "You win. Dealer went beyond 21"
    elif player > dealer:
        return "You win"
    else:
        return "you loose"






def play_game():
    """BlackJack game"""
    game_over = False
    player = []
    dealer = []
    dealer_total = -1
    player_total = -1
    user_new_card = "no"
    get_new_cards(player= player, dealer= dealer)
    while not game_over:
        player_total = replace_jack_with_1_on_condition(player)
        dealer_total = replace_jack_with_1_on_condition(dealer)

        if player_total == 0 or dealer_total == 0 or player_total > 21:
            game_over == True
        else:
            user_new_card = input("Do you need another card?: ").lower()
            if user_new_card == "yes":
                player.append(choose_a_card())
                print(player)
            else:
                game_over = True
    while dealer_total != 0 and dealer_total < 17:
        dealer.append(choose_a_card())
        dealer_total = replace_jack_with_1_on_condition(dealer)

    print(f"Your cards are {player} and your total is {sum(player)}")
    print(f"Dealer cards are {dealer} and total is {dealer_total}")
    print(compaer(sum(player), sum(dealer)))

while(input("Do you want to play blackjack game: 'y' to play and 'n' to not playe") == 'y'):
    play_game()