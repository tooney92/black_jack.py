import random

class Royals():
    def __init__(self, card, value):
        self.card = card
        self.value = value

    def card_name(self):
        return self.card
    def card_value(self):
        return self.value
      
class players_bet_account():
    
    def __init__(self, balance = 1500):
        self.balance = balance
    
    def print_player_account_startup(self):
        print('your startup amount is 1500')
    def credit_player1_account(self, amount):
        self.balance =  self.balance + amount
        return self.balance
    def debit_player_account(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        if amount > self.balance:
            print('error!, insufficent balance')
        
    def player_bet_amount(self, bet_amount): 
        self.balance =  self.balance - bet_amount
                
player_bet_account = players_bet_account(1500)
     
card_shape = ['spade', 'club', 'heart', 'diamond']

king_royal_card = Royals('king', 10)
queen_royal_card = Royals('queen', 10)
joker_royal_card = Royals('joker', 10)


deck_main = [2, 3, 4, 5, 6, 7, 8, 9,10, king_royal_card.card_name(), queen_royal_card.card_name(), joker_royal_card.card_name(), 'Ace']

deck = [2,'Ace']

while player_bet_account.balance > 100:
    
    print('your currnet balance is:', player_bet_account.balance)
    while True:
        player_bet = int(input('how much are u betting?'))
        if player_bet > player_bet_account.balance:
            print('sorry you do not have such amount!')
            continue
        if player_bet < player_bet_account.balance:
            break
         
    print('your currnet balance after betting', player_bet, 'is:',player_bet_account.balance - player_bet)
   
    card1 = random.choice(deck_main)
    card2 = random.choice(deck_main)

    if type(card1) is int:
        print('your first card is',random.choice(card_shape),card1)

    if type(card2) is int:
        print('your second card is',random.choice(card_shape),card2)

    if card1 is king_royal_card.card_name():
        print('Your 1st card is',card1, 'which has  a value of 10')
        card1 = 10

    if card1 is queen_royal_card.card_name():
        print('Your 1st card is',card1, 'which has a value of 10')
        card1 = 10

    if card1 is joker_royal_card.card_name():
        print('Your 1st card is',card1, 'which has a value of 10')
        card1 = 10

    if card2 is king_royal_card.card_name():
        print('Your 2nd card is',card2, 'which has a value of 10')
        card2 = 10

    if card2 is queen_royal_card.card_name():
        print('Your 2nd card is',card2, 'which has a value of 10')
        card2 = 10

    if card2 is joker_royal_card.card_name():
        print('Your 2nd card is',card2, 'which has a value of 10')
        card2 = 10

    if card1 is 'Ace':

        player_choice = int(input('Your 1st card is an Ace! how would you like your ace to be tallied? 1 or 11? You may select 0 to wait: '))
        print('You chose:', player_choice)

        if player_choice is 1:
            card1 = 1
        elif player_choice is 11:
            card1 = 11
        elif player_choice is 0:
            card1 = 0

    if card2 is 'Ace':

        player_choice = int(input('Your second card is an Ace! how would you like your ace to be tallied? 1 or 11? You may select 0 to wait:  '))
        print('You chose:', player_choice)


        if player_choice is 1:
            card2 = 1
        elif player_choice is 11:
            card2 = 11
        elif player_choice is 0:
            card2 = 0    


    player_hand = [card1, card2]
    player_hand_total = sum(player_hand)

    print('your hand is:',player_hand, 'with a total of:',player_hand_total)

    if player_hand_total is 21:
        print('JACKPOT!.... :) you have a total of 21')
        player_bet_account.credit_player1_account(player_bet)
        
    if player_hand_total > 21:
        print('you lost!')
        player_bet_account.debit_player_account(player_bet)
        break



    computer_card1 = random.choice(deck_main)
    computer_card2 = random.choice(deck_main)

    if type(computer_card1) is int:
        print('computer first card is',random.choice(card_shape),computer_card1)

    #if type(computer_card2) is int:

    if computer_card1 is king_royal_card.card_name():
        print('computer 1st card is',computer_card1, 'which has  a value of 10')
        computer_card1 = 10

    if computer_card1 is queen_royal_card.card_name():
        print('computer 1st card is',computer_card1, 'which has a value of 10')
        computer_card1 = 10

    if computer_card1 is joker_royal_card.card_name():
        print('computer 1st card is',computer_card1, 'which has a value of 10')
        computer_card1 = 10

    if computer_card2 is king_royal_card.card_name():
        computer_card2 = 10

    if computer_card2 is queen_royal_card.card_name():
        computer_card2 = 10

    if computer_card2 is joker_royal_card.card_name():
        computer_card2 = 10

    if computer_card1 is 'Ace':
        computer_card1 = 11

    if computer_card2 is 'Ace':
        computer_card2 = 11

    computer_hand = [computer_card1, computer_card2]
    computer_hand_total = sum(computer_hand)


    print('computer hand is:', computer_hand, 'with a total of:', computer_hand_total)

    if computer_hand_total is 21:
        print('computer won :)')
        player_bet_account.debit_player_account(player_bet)

    while player_hand_total < 21:   

        hit_choice = input('would you like a HIT Or STAND?  ')
        hit_choice = hit_choice.lower()
        hit_choice = hit_choice.replace(' ', '')

        if hit_choice.startswith('h'):

            hit_number = random.choice(deck_main)

            if type(hit_number) is int:
                print('your hit number is:',random.choice(card_shape),hit_number)
                player_hand.append(hit_number)
                print(player_hand)

            if hit_number is king_royal_card.card_name():
                print('Your hit card is',hit_number, 'which has a value of 10')
                hit_number = 10
                player_hand.append(hit_number)
                print(player_hand)

            if hit_number is queen_royal_card.card_name():
                print('Your hit card is',hit_number, 'which has a value of 10')
                hit_number = 10
                player_hand.append(hit_number)
                print(player_hand)

            if hit_number is joker_royal_card.card_name():
                print('Your hit card is',hit_number, 'which has a value of 10')
                hit_number = 10
                player_hand.append(hit_number)
                print(player_hand)

            if hit_number is 'Ace':

                player_choice_for_Ace = int(input('how would you like your ace to be tallied? 1 or 11' ))
                print('You chose:', player_choice_for_Ace)
                player_hand.append(player_choice_for_Ace)
                print(player_hand)

            player_hand_total = sum(player_hand)  
            print('current hand is:', player_hand, 'with a total of:', player_hand_total)

        if player_hand_total > 21:
            print('BUST!, your hand of', player_hand, 'is greater than 21. Total:', player_hand_total, 'Computer won!' )
            #player_hand_total = 'pl'
            player_bet_account.debit_player_account(player_bet)
            break

        if player_hand_total is 21:
            print('JACKPOT!.... :) you have a total of 21')
            player_bet_account.credit_player1_account(player_bet)
            break

        if hit_choice.startswith('s'):
            if card1 is 0:
                player_final_ace_choice = int(input('how will you like your ace to be tallied?'))
                player_hand.append(player_final_ace_choice)

            if card2 is 0:
                player_final_ace_choice = int(input('how will you like your ace to be tallied?'))
                player_hand.append(player_final_ace_choice)

            player_hand_total = sum(player_hand)

            if player_hand_total > 21:
                print('BUST!, your hand of', player_hand, 'is greater than 21. Total is', player_hand_total, '. Computer won!' )
                player_bet_account.debit_player_account(player_bet)
                break
            if player_hand_total is 21:
                print('JACKPOT!.... :) you have a total of 21')
                player_bet_account.credit_player1_account(player_bet)
                break
            print(' Your final hand is', player_hand, '. Total:', player_hand_total)

            break


    if player_hand_total < 21:

        while computer_hand_total < 17:

            computer_new_hand = random.choice(deck_main)

            if type(computer_new_hand) is int:
                computer_hand.append(computer_new_hand)
                computer_hand_total= sum(computer_hand)

            if computer_new_hand is king_royal_card.card_name():
                computer_new_hand = 10
                computer_hand.append(computer_new_hand)
                computer_hand_total= sum(computer_hand)

            if computer_new_hand is queen_royal_card.card_name():
                computer_new_hand = 10
                computer_hand.append(computer_new_hand)
                computer_hand_total= sum(computer_hand)

            if computer_new_hand is joker_royal_card.card_name():
                computer_new_hand = 10
                computer_hand.append(computer_new_hand)
                computer_hand_total = sum(computer_hand)

            if computer_new_hand is 'Ace':
                computer_new_hand = 11
                computer_hand.append(computer_new_hand)
                computer_hand_total= sum(computer_hand)


            print("Computer's new card is:", computer_new_hand, "computers current hand is", computer_hand, '.Total:',computer_hand_total)

            if computer_hand_total >= 17:
                if computer_hand_total > 21:
                    print('Computer lost!')
                    player_bet_account.credit_player1_account(player_bet)
                    break
                if computer_hand_total is 21:
                    print('Jackpot for computer!')
                    player_bet_account.debit_player_account(player_bet)
                    break

 
    if player_hand_total <= 21:
        if player_hand_total > computer_hand_total:
            print('playerrrrr1 won')
            player_bet_account.credit_player1_account(player_bet)

    if computer_hand_total <= 21 :
        if computer_hand_total > player_hand_total:
            player_bet_account.debit_player_account(player_bet)
            print('computerrrrr! won')
            
    if player_hand_total == computer_hand_total:
        print('DRAW')

    player_game_choice = input('would you like to play again?')
    player_game_choice = player_game_choice.lower()
    player_game_choice = player_game_choice.replace(' ', '')

    if player_game_choice.startswith('y'):
        if player_bet_account.balance <= 100:
            print('sorry insufficient balance, your current balance of', player_bet_account.balance, 'is below the minimum $100 bet amount')
        continue
        
        
    if player_game_choice.startswith('n'):
        print('your balance is:', player_bet_account.balance)
        break
    
    



