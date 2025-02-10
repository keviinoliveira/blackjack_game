import art
import random


def decision(your_cards, pc_cards, n):
    next_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if next_card == 'y':
        your_cards.append(random.choice(CARDS))
        print(f"Your Cards: {your_cards}, current score: {sum(your_cards)}")
        print(f"Computer's first card: {pc_cards}")
        if sum(your_cards) > 21:
            print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
            print(f"Computer's final hand: {pc_cards}, final score: {sum(pc_cards)}")
            print("You went over. You lose 😭")
        else:
            n = n +1
            decision(your_cards, pc_cards, n)
    else:
        print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
        pc_cards.append(random.choice(CARDS))
        if sum(pc_cards) > 21:
            print(f"Computer's final hand: {pc_cards}, final score: {sum(pc_cards)}")
            print("Opponent went over. You win 😁")
            return
        else:
            while sum(pc_cards) < 17:
                pc_cards.append(random.choice(CARDS))
                if sum(pc_cards) > 21:
                    print(f"Computer's final hand: {pc_cards}, final score: {sum(pc_cards)}")
                    print("Opponent went over. You win 😁")
                    return
                elif sum(pc_cards) == 21:
                    print(f"Computer's final hand: {pc_cards}, final score: {sum(pc_cards)}")
                    print("Lose, opponent has Blackjack 😱")
            if sum(your_cards) > sum(pc_cards):
                print(f"Computer's final hand: {pc_cards}, final score: {sum(pc_cards)}")
                print("You win 😃")
            elif sum(your_cards) == sum(pc_cards):
                print(f"Computer's final hand: {pc_cards}, final score: {sum(pc_cards)}")
                print("Dawn")
            else:
                print(f"Computer's final hand: {pc_cards}, final score: {sum(pc_cards)}")
                print("You lose 😭")

print(art.art)
game = input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
CARDS = [11,2,3,4,5,6,7,8,9,10,10,10,10]
while game == 'y':
    your_cards = random.choices(CARDS,k=2)
    print(f"Your Cards: {your_cards}, current score: {sum(your_cards)}")
    pc_cards = random.choices(CARDS, k=1)
    print(f"Computer's first card: {pc_cards}")
    n = 0
    if sum(your_cards) == 21:
        print(f"Your final hand: {your_cards}, final score: {sum(your_cards)}")
        print(f"Computer's final hand: {pc_cards}, final score: {sum(pc_cards)}")
        print("Win with a Blackjack 😎")
    decision (your_cards, pc_cards, n) 
    game = input ("Do you want to play a game of Blackjack? Type 'y' or 'n': ")