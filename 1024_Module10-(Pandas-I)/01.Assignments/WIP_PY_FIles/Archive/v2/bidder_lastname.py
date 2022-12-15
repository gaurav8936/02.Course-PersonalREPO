class Bidder:
    
    """
    This is the bidder class where we track bidding details, patterns and history. 
    In addition to the required functions, there are five other functions that have been 
    created to model bidding strategies -- listed below
    
    Note the acronyms user
    BWCY: Bidder Won, Clicked Yes
    BWCN: Bidder Won, Clicked No
    BLOS: Bidder Lost
    """
    import numpy as np
    import random
    from collections import Counter
    
    def __init__(self, num_users, num_rounds):
            
    ############ Initialize Attributes for bid and history  ###########################################
    ###################################################################################################
        
        ########### initializing basic attributes ###########
        self.num_users = num_users
        self.num_rounds = num_rounds
        self.bidding_round = 0
        self.bid_price = 0
        self.active_bidder = True

        ########### Basic tracking metrics - dictionaries ###########
        self.bid_participate = {i: 0 for i in range(num_users)} #whether bidder bids or not (USER: BID COUNT)
        self.bid_wins_no_click = {i: 0 for i in range(num_users)} # if bidder wins
        self.bid_win_user_clicks = {i: 0 for i in range(num_users)} # if user clicks
        self.bid_lost = {i: 0 for i in range(num_users)}

        ########### Historical transaction tracking for trend analysis ###########
        self.bid_win_click_no = []
        self.bid_win_click_yes = []
        self.bid_lost_list = []
        self.bid_360 = []
        
    ############ SUBMIT BID  ########### initiated by auction #########################################
    ###################################################################################################
    
    def __repr__(self):
        return "This is a bidder participating in a second price auction with " + str(self.num_rounds) + " rounds of bidding"     
    def __str__(self):
        return self.__repr__()   
    
    
    def bid(self, user_id):
        """
        Function to set teh default (aka base) bid price
        The bid price is called from a separate function that determines the bid strategy
        """

        self.bidding_round += 1
        self.user_id = user_id
        self.bid_price = self.bid_strategy(user_id)
        return self.bid_price

    ############  NOTIFIED OF BID OUTCOME  ########### initiated by auction ###########################
    ###################################################################################################
    
    def notify(self, auction_winner, price, clicked):
        bid_y_n_won = 0
        self.auction_winner = auction_winner
        self.price = price
        self.clicked = clicked
        
        if auction_winner == True and clicked == True:
            self.bid_win_user_clicks[self.user_id] = (self.bid_win_user_clicks).get(self.user_id, 0)+1
            self.bid_win_click_yes.append(['BWCY', self.bidding_round, id(self), self.user_id, self.auction_winner,self.bid_price, self.price, self.clicked])
            self.bid_360.append(['BWCY', self.bidding_round, id(self), self.user_id, self.auction_winner,self.bid_price, self.price, self.clicked])

        elif auction_winner == True and clicked == False:
            self.bid_wins_no_click[self.user_id] = (self.bid_wins_no_click).get(self.user_id, 0)+1
            self.bid_win_click_no.append(['BWCN', self.bidding_round, id(self), self.user_id, self.auction_winner,self.bid_price, self.price, self.clicked])
            self.bid_360.append(['BWCN', self.bidding_round, id(self), self.user_id, self.auction_winner,self.bid_price, self.price, self.clicked])
        
        else:
            self.bid_lost[self.user_id] = (self.bid_lost).get(self.user_id, 0)+1
            self.bid_lost_list.append(['BLOS',self.bidding_round, id(self), self.user_id, self.auction_winner,self.bid_price, self.price, self.clicked])
            self.bid_360.append(['BLOS',self.bidding_round, id(self), self.user_id, self.auction_winner,self.bid_price, self.price, self.clicked])
    
    ############  BID STRATEGY - CONTROL FLOW  ########################################################
    ###################################################################################################
    
    def bid_strategy(self, user_id):

        """
        This function controls the strategy and changes this with what it learns from the bidding process
        There are two basic - default strategies that will be followed for the first 50 rounds which are
        (1) start slow and observe bidding behavior for first 10 rounds
        (2) go aggressive and match max price of past rounds and in crease base bid by 10%
        After the first 50 rounds, the strategy revolves through 4 models (A, B, C & D) aso detailed below
        """
        
        ########## SET THE BASE BID PRICE  ##### Revise this based on Strategy ############################
        #################### Ranges from 0 to $1 ##########################################################
        
        self.base_bid_price = random.randint(0, 10000)/10000 #random.uniform(0, 1)
        
        ###################################################################################################
        
        trx_master = [x for x in self.bid_360]
        strategy_list = ['A', 'B', 'C', 'D']
        strategy = random.choice(strategy_list)
        
        for item in trx_master:
        
        ########## Observe: Start Slow for the first 10 rounds  ###########################################
        ###################################################################################################
        
            if item[1] < 10:
                self.bid_price = 0.01
            
        ########## Next 40 rounds, match max price + 10%  #################################################
        ###################################################################################################
            
            elif item[1] >= 10 and item[1] <= 50 :
                self.bid_price = max(self.bid_360, key=lambda x: x[6])[6]*1.10
                if self.bid_price > self.base_bid_price * 100:
                    self.bid_price = self.base_bid_price
        
        ########## Rounds 50+ Learn, Optimize, Mitigate Losses and Win  ###################################
        ###################################################################################################
        
            elif strategy == 'A':
                self.bid_price = self.strategy_a()
            
            elif strategy == 'B':
                self.bid_price = self.strategy_b()
                
            elif strategy == 'C':
                self.bid_price = self.strategy_c()
                
            elif strategy == 'D':
                self.bid_price = self.strategy_d()
            
            else:
                self.bid_price = self.base_bid_price
            
        
        return self.bid_price
        
    
    ############  STRATEGY A - Identify losses and counter  ###########################################
    ###################################################################################################
        
    def strategy_a(self):
            
        """
        Setting min bid above average difference of loss for prior 10 bids  was greater than 10%
        then adjust you next bid to in increase by that amount
        """

        # filter last 10 losses  
        a = [x for x in self.bid_360[-10:] if x[0] == 'BLOS' and (x[6]-x[5]) > (.1*x[5])]

        # calculated the average percentage loss (> 10%)
        avg_loss_10percent = ((sum(i[6] for i in a) - sum(i[5] for i in a))/(max(1, len(a))))

        #adjust bid price
        self.bid_price = self.base_bid_price + avg_loss_10percent
        if self.bid_price > self.base_bid_price * 2:
            self.bid_price = self.base_bid_price
        return self.bid_price

    ############  STRATEGY B - Exploit/Focus on top User   ############################################
    ###################################################################################################
    
    def strategy_b(self):
        #self.user_id = user_id
        
        """
        Focus on most successful user --- ie where bidder has worn atleast 5 times for same user
        For this user, double the base bid price to increase odds of winning again
        """
        
        a = [x for x in self.bid_360[-100:] if x[0] == 'BWCY']
        #print(a)
        b = (Counter([x[3] for x in a]))
        #print(b)
        # filter for success > 5 times
        c = { k: v for k, v in b.items() if v >= 0 }
        # get max user (most successful thus far)
        d = max(c, key=c.get, default=0) # get user with max wins
        
        if d == None:
            self.bid_price = self.base_bid_price
        elif self.user_id ==  d:
            self.bid_price = self.base_bid_price*2
        else:    
            self.bid_price = self.base_bid_price
        return self.bid_price
        
    
    ############  STRATEGY C - Identify Max leaders and counter   #####################################
    ###################################################################################################
    
    def strategy_c(self):
        
        """
        Find Max winning bid in past 10 bids and increase your base bid by 20%
        """

        a = [x for x in self.bid_360[-10:] if x[0] == 'BLOS']
        
        if a == []:
        #if max(a, key=lambda x: x[6]) == []:
        # if max(a, key=lambda x: x[6])[6] == False:
            self.bid_price = self.base_bid_price
        else:
            self.bid_price = max(a, key=lambda x: x[6])[6]*1.20
            if self.bid_price > self.base_bid_price * 5:
                self.bid_price = self.base_bid_price
        return self.bid_price
    
    
    ############  STRATEGY D - Conserve cash when <-500   #############################################
    ###################################################################################################
    
    def strategy_d(self):
            
        """
        Monitor if balance goes < -500 then scale back on the bids by 10% of the base price
        Conserve cash and wait for other random strategies A, B or C to try again
        """

        # sum all bids that were won, but user not clicked (ie BWCN)
        a = [x for x in self.bid_360 if x[0] == 'BWCN'] 

        # calculate cost of bids in BWCN
        b = (sum(i[6] for i in a))
        
        # sum of all bids where user clicked (ie BWCY)
        c = [x for x in self.bid_360 if x[0] == 'BWCY']
        # sum of total cost
        d = (sum(i[6] for i in c) )

        # earnings till date (ie $1 for every BWCY)
        e = len(c)
        f = e * 1

        current_balance = (b + d -f)
        
        if current_balance < -500:
            self.bid_price = 0.01
        return self.base_bid_price