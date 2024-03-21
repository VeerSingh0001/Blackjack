from art import logo
from random import choices
from os import system
from sys import platform

def dealCard():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choices(cards)
    return card[0]


def calulateScore(cards):
    """Take a list of cards and return the score calculated from the cards"""
    total = sum(cards)

    if total == 21 and len(cards) == 2:
        return 0

    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)

    return total


def compare(user_score, computer_score):
    """Take a final score of user and computer and retun the winner"""
    if user_score == computer_score:
        return "Draw🥲"
    elif computer_score == 0:
        return "Lose, opponent has a Blackjack 😭"
    elif user_score == 0:
        return "win with a Blacjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😢"
    elif computer_score > 21:
        return "Opponent went over. You win🥳"
    elif user_score > computer_score:
        return "You win🥳"
    else:
        return "You lose😢"


def playGame():
    """Initial function to start game"""
    print(logo)

    userCards = []
    ComputerCards = []
    isGameOver = False

    for _ in range(2):
        userCards.append(dealCard())
        ComputerCards.append(dealCard())

    while not isGameOver:
        userScore = calulateScore(userCards)
        computerScore = calulateScore(ComputerCards)

        print(f"Your cards: {userCards}, current score: {userScore}")
        print(f"Computer's first card: {ComputerCards[0]}")

        if userScore == 0 or computerScore == 0 or userScore > 21:
            isGameOver = True
        else:
            userShouldDeal = input("Type 'y' to get another card, type 'n' to pass: ")
            if userShouldDeal == "y":
                userCards.append(dealCard())
            else:
                isGameOver = True

    while computerScore != 0 and computerScore < 17:
        ComputerCards.append(dealCard())
        computerScore = calulateScore(ComputerCards)

    print(f"Your final hand: {userCards}, final score: {userScore}")
    print(f"Computer's final hand: {ComputerCards}, final score: {computerScore}")

    print(compare(userScore, computerScore))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == "y":
    if platform == "win32": #Check operating system
        system("cls")
    else:
        system("clear")
    playGame()
