##############################################################
#DEALER
##############################################################
dealer_strategy={}
for i in range(17,22):
    dealer_strategy['hard',i]='stand'
for i in range(5,17):
    dealer_strategy['hard',i]='hit'
for i in range(18,22):
    dealer_strategy['soft',i]='stand'
for i in range(3,18):
    dealer_strategy['soft',i]='hit'
for i in range(18,22):
    dealer_strategy['pair',i]='stand'
for i in range(2,17):
    dealer_strategy['pair',i]='hit'


##############################################################
#PLAYER
##############################################################
player_strategy={}

for i in range(1,11):
    player_strategy['hard',21,i]='stand'
    
for i in range(1,11):
    player_strategy['hard',20,i]='stand'
    
for i in range(1,11):
    player_strategy['hard',19,i]='stand'
    
for i in range(1,11):
    player_strategy['hard',18,i]='stand'
    
for i in range(1,11):
    player_strategy['hard',17,i]='stand'
    
player_strategy['hard',16,2]='stand'
player_strategy['hard',16,3]='stand'
player_strategy['hard',16,4]='stand'
player_strategy['hard',16,5]='stand'
player_strategy['hard',16,6]='stand'
player_strategy['hard',16,7]='hit'
player_strategy['hard',16,8]='hit'
player_strategy['hard',16,9]='hit'
player_strategy['hard',16,10]='hit'
player_strategy['hard',16,1]='hit'

player_strategy['hard',15,2]='stand'
player_strategy['hard',15,3]='stand'
player_strategy['hard',15,4]='stand'
player_strategy['hard',15,5]='stand'
player_strategy['hard',15,6]='stand'
player_strategy['hard',15,7]='hit'
player_strategy['hard',15,8]='hit'
player_strategy['hard',15,9]='hit'
player_strategy['hard',15,10]='hit'
player_strategy['hard',15,1]='hit'

player_strategy['hard',14,2]='stand'
player_strategy['hard',14,3]='stand'
player_strategy['hard',14,4]='stand'
player_strategy['hard',14,5]='stand'
player_strategy['hard',14,6]='stand'
player_strategy['hard',14,7]='hit'
player_strategy['hard',14,8]='hit'
player_strategy['hard',14,9]='hit'
player_strategy['hard',14,10]='hit'
player_strategy['hard',14,1]='hit'

player_strategy['hard',13,2]='stand'
player_strategy['hard',13,3]='stand'
player_strategy['hard',13,4]='stand'
player_strategy['hard',13,5]='stand'
player_strategy['hard',13,6]='stand'
player_strategy['hard',13,7]='hit'
player_strategy['hard',13,8]='hit'
player_strategy['hard',13,9]='hit'
player_strategy['hard',13,10]='hit'
player_strategy['hard',13,1]='hit'

player_strategy['hard',12,2]='hit'
player_strategy['hard',12,3]='hit'
player_strategy['hard',12,4]='stand'
player_strategy['hard',12,5]='stand'
player_strategy['hard',12,6]='stand'
player_strategy['hard',12,7]='hit'
player_strategy['hard',12,8]='hit'
player_strategy['hard',12,9]='hit'
player_strategy['hard',12,10]='hit'
player_strategy['hard',12,1]='hit'

player_strategy['hard',11,2]='double'
player_strategy['hard',11,3]='double'
player_strategy['hard',11,4]='double'
player_strategy['hard',11,5]='double'
player_strategy['hard',11,6]='double'
player_strategy['hard',11,7]='double'
player_strategy['hard',11,8]='double'
player_strategy['hard',11,9]='double'
player_strategy['hard',11,10]='double'
player_strategy['hard',11,1]='hit'

player_strategy['hard',10,2]='double'
player_strategy['hard',10,3]='double'
player_strategy['hard',10,4]='double'
player_strategy['hard',10,5]='double'
player_strategy['hard',10,6]='double'
player_strategy['hard',10,7]='double'
player_strategy['hard',10,8]='double'
player_strategy['hard',10,9]='double'
player_strategy['hard',10,10]='hit'
player_strategy['hard',10,1]='hit'

player_strategy['hard',9,2]='hit'
player_strategy['hard',9,3]='double'
player_strategy['hard',9,4]='double'
player_strategy['hard',9,5]='double'
player_strategy['hard',9,6]='double'
player_strategy['hard',9,7]='hit'
player_strategy['hard',9,8]='hit'
player_strategy['hard',9,9]='hit'
player_strategy['hard',9,10]='hit'
player_strategy['hard',9,1]='hit'

for i in range(1,11):
    player_strategy['hard',8,i]='hit'

for i in range(1,11):
    player_strategy['hard',7,i]='hit'

for i in range(1,11):
    player_strategy['hard',6,i]='hit'

for i in range(1,11):
    player_strategy['hard',5,i]='hit'

for i in range(1,11):
    player_strategy['soft',21,i]='stand'

for i in range(1,11):
    player_strategy['soft',20,i]='stand'

for i in range(1,11):
    player_strategy['soft',19,i]='stand'

player_strategy['soft',18,2]='stand'
player_strategy['soft',18,3]='double'
player_strategy['soft',18,4]='double'
player_strategy['soft',18,5]='double'
player_strategy['soft',18,6]='double'
player_strategy['soft',18,7]='stand'
player_strategy['soft',18,8]='stand'
player_strategy['soft',18,9]='hit'
player_strategy['soft',18,10]='hit'
player_strategy['soft',18,1]='hit'

player_strategy['soft',17,2]='hit'
player_strategy['soft',17,3]='double'
player_strategy['soft',17,4]='double'
player_strategy['soft',17,5]='double'
player_strategy['soft',17,6]='double'
player_strategy['soft',17,7]='hit'
player_strategy['soft',17,8]='hit'
player_strategy['soft',17,9]='hit'
player_strategy['soft',17,10]='hit'
player_strategy['soft',17,1]='hit'

player_strategy['soft',16,2]='hit'
player_strategy['soft',16,3]='hit'
player_strategy['soft',16,4]='double'
player_strategy['soft',16,5]='double'
player_strategy['soft',16,6]='double'
player_strategy['soft',16,7]='hit'
player_strategy['soft',16,8]='hit'
player_strategy['soft',16,9]='hit'
player_strategy['soft',16,10]='hit'
player_strategy['soft',16,1]='hit'

player_strategy['soft',15,2]='hit'
player_strategy['soft',15,3]='hit'
player_strategy['soft',15,4]='double'
player_strategy['soft',15,5]='double'
player_strategy['soft',15,6]='double'
player_strategy['soft',15,7]='hit'
player_strategy['soft',15,8]='hit'
player_strategy['soft',15,9]='hit'
player_strategy['soft',15,10]='hit'
player_strategy['soft',15,1]='hit'

player_strategy['soft',14,2]='hit'
player_strategy['soft',14,3]='hit'
player_strategy['soft',14,4]='hit'
player_strategy['soft',14,5]='double'
player_strategy['soft',14,6]='double'
player_strategy['soft',14,7]='hit'
player_strategy['soft',14,8]='hit'
player_strategy['soft',14,9]='hit'
player_strategy['soft',14,10]='hit'
player_strategy['soft',14,1]='hit'

player_strategy['soft',13,2]='hit'
player_strategy['soft',13,3]='hit'
player_strategy['soft',13,4]='hit'
player_strategy['soft',13,5]='double'
player_strategy['soft',13,6]='double'
player_strategy['soft',13,7]='hit'
player_strategy['soft',13,8]='hit'
player_strategy['soft',13,9]='hit'
player_strategy['soft',13,10]='hit'
player_strategy['soft',13,1]='hit'

for i in range(1,11):
    player_strategy['pair',2,i]='split_aces'

for i in range(1,11):
    player_strategy['pair',20,i]='stand'

player_strategy['pair',18,2]='split'
player_strategy['pair',18,3]='split'
player_strategy['pair',18,4]='split'
player_strategy['pair',18,5]='split'
player_strategy['pair',18,6]='split'
player_strategy['pair',18,7]='stand'
player_strategy['pair',18,8]='split'
player_strategy['pair',18,9]='split'
player_strategy['pair',18,10]='stand'
player_strategy['pair',18,1]='stand'

for i in range(1,11):
    player_strategy['pair',16,i]='split'

player_strategy['pair',14,2]='split'
player_strategy['pair',14,3]='split'
player_strategy['pair',14,4]='split'
player_strategy['pair',14,5]='split'
player_strategy['pair',14,6]='split'
player_strategy['pair',14,7]='split'
player_strategy['pair',14,8]='hit'
player_strategy['pair',14,9]='hit'
player_strategy['pair',14,10]='hit'
player_strategy['pair',14,1]='hit'

player_strategy['pair',12,2]='hit'
player_strategy['pair',12,3]='split'
player_strategy['pair',12,4]='split'
player_strategy['pair',12,5]='split'
player_strategy['pair',12,6]='split'
player_strategy['pair',12,7]='hit'
player_strategy['pair',12,8]='hit'
player_strategy['pair',12,9]='hit'
player_strategy['pair',12,10]='hit'
player_strategy['pair',12,1]='hit'

player_strategy['pair',10,2]='double'
player_strategy['pair',10,3]='double'
player_strategy['pair',10,4]='double'
player_strategy['pair',10,5]='double'
player_strategy['pair',10,6]='double'
player_strategy['pair',10,7]='double'
player_strategy['pair',10,8]='double'
player_strategy['pair',10,9]='double'
player_strategy['pair',10,10]='hit'
player_strategy['pair',10,1]='hit'

for i in range(1,11):
    player_strategy['pair',8,i]='hit'

player_strategy['pair',6,2]='hit'
player_strategy['pair',6,3]='hit'
player_strategy['pair',6,4]='split'
player_strategy['pair',6,5]='split'
player_strategy['pair',6,6]='split'
player_strategy['pair',6,7]='split'
player_strategy['pair',6,8]='hit'
player_strategy['pair',6,9]='hit'
player_strategy['pair',6,10]='hit'
player_strategy['pair',6,1]='hit'

player_strategy['pair',4,2]='hit'
player_strategy['pair',4,3]='hit'
player_strategy['pair',4,4]='split'
player_strategy['pair',4,5]='split'
player_strategy['pair',4,6]='split'
player_strategy['pair',4,7]='split'
player_strategy['pair',4,8]='hit'
player_strategy['pair',4,9]='hit'
player_strategy['pair',4,10]='hit'
player_strategy['pair',4,1]='hit'
