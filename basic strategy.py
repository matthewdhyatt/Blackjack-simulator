import random
import strategies

dealer_strategy=strategies.dealer_strategy
player_strategy=strategies.player_strategy

#constants
number_of_decks=6
penetration=0.75
number_of_shoes=10**4
bj_payout=1.5
deck=4*(list(range(1,10))+4*[10])

#globals
shoe=[]
dealer=[]
dealer_score=[]
player_queue=[]
player_done=[]
player_scores=[]
profit=0
hand_counter=0

class hand:
    def __init__(self,cards):
        self.cards=cards
    def __str__(self):
        return str(self.cards)
    def total(self):
        if len(self.cards)==2 and self.cards[0]==self.cards[1]:
            return ('pair',sum(self.cards))
        elif 1 in self.cards and sum(self.cards)<12:
            return ('soft',sum(self.cards)+10)
        elif sum(self.cards)<22:
            return ('hard',sum(self.cards))
        else:
            return ('bust',0)

def start_shoe():
    global shoe
    shoe=number_of_decks*deck
    random.shuffle(shoe)
    
def deal():
    global dealer
    global player_queue
    global shoe

    dealer=hand([shoe.pop(),shoe.pop()])
    player_queue=[hand([shoe.pop(),shoe.pop()])]

#x is a hand object
def dealer_play(x):
    global shoe
    global dealer_score

    keep_playing=True

    if sorted(x.cards)==[1,10]:
        #use 21.1 for blackjack
        dealer_score=[21.1]
        keep_playing=False
    while keep_playing:
        current=x.total()
        if current[0]=='bust':
            dealer_score.append(current[1])
            keep_playing=False

        elif dealer_strategy[current]=='hit':
            hand_update=x.cards
            hand_update.append(shoe.pop())
            x=hand(hand_update)

        elif dealer_strategy[current]=='stand':
            dealer_score.append(current[1])
            keep_playing=False

#y is a list of hand objects
def player_play(y):
    global shoe
    global player_scores
    global player_done
    global dealer

    while y:
        x=y.pop(0)
        keep_playing=True

        if sorted(x.cards)==[1,10] and not y and not player_done:
            #use 21.1 forblackjack
            player_scores.append(21.1)
            player_done.append(x)
            keep_playing=False
        while keep_playing:
            current=x.total()

            if current[0]=='bust':
                player_scores.append(current[1])
                player_done.append(x)
                keep_playing=False

            elif player_strategy[current+(dealer.cards[0],)]=='hit':
                hand_update=x.cards
                hand_update.append(shoe.pop())
                x=hand(hand_update)

            elif player_strategy[current+(dealer.cards[0],)]=='stand':
                player_scores.append(current[1])
                player_done.append(x)
                keep_playing=False
            
            elif player_strategy[current+(dealer.cards[0],)]=='split':
                y+=[hand([x.cards[0],shoe.pop()]),hand([x.cards[1],shoe.pop()])]
                keep_playing=False

            elif player_strategy[current+(dealer.cards[0],)]=='double':
                if len(x.cards)==2:
                    hand_update=x.cards
                    hand_update.append(shoe.pop())
                    x=hand(hand_update)
                    current=x.total()

                    player_scores.append(current[1])
                    player_scores.append(current[1])
                    player_done.append(x)
                    keep_playing=False

                else:
                    hand_update=x.cards
                    hand_update.append(shoe.pop())
                    x=hand(hand_update)

            elif player_strategy[current+(dealer.cards[0],)]=='split_aces':
                x=hand([1,shoe.pop()])
                current=x.total()
                player_scores.append(current[1])
                player_done.append(x)

                x=hand([1,shoe.pop()])
                current=x.total()
                player_scores.append(current[1])
                player_done.append(x)
                
                keep_playing=False

def play_shoe():
    global profit
    global hand_counter
    global dealer
    global dealer_score
    global player_queue
    global player_done
    global player_scores
    
    start_shoe()
    #print('!!!\nNEW SHOE\n!!!\n')
    while len(shoe)>(1-penetration)*number_of_decks*52:
        hand_counter+=1
        dealer=[]
        dealer_score=[]
        player_queue=[]
        player_done=[]
        player_scores=[]
        
        #print('current shoe')
        #print(shoe)
        #print()
        
        deal()
        #print('starting hands')
        #print(dealer)
        #for x in player_queue:
        #    print(x)
        #print()

        
        dealer_play(dealer)
        #print('results of dealer play')
        #print('score = {}'.format(dealer_score))
        #print('hand = {}'.format(dealer))
        #print()

        player_play(player_queue)
        #print('results of player play')
        #print('scores = {}'.format(player_scores))
        #for x in player_done:
        #    i=1
        #    print('hand {} = {}'.format(i,x))
        #    i+=1
        #print()

        for s in player_scores:
            if s>dealer_score[0]:
                if s==21.1:
                    profit+=bj_payout
                else:
                    profit+=1
            elif s<dealer_score[0] or s==0:
                profit-=1
        #print('current profit = {}'.format(profit))
        #print('----------------------------------------------\n')


for i in range(number_of_shoes):
    play_shoe()
    '''
    print('shoe number {}'.format(i))
    print('current profit : {}'.format(profit))
    print('number of hands played : {}'.format(hand_counter))
    print()
    '''


print('profit (in units of base bet) : {}'.format(profit))
print('number of hands played : {}'.format(hand_counter))
print('profit per hand : {}'.format(profit/hand_counter))


