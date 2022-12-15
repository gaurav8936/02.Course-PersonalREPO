import numpy as np
import random
from collections import Counter
#import bidder_narasimhan
#from bidder_narasimhan import Bidder

class User:
    """
    This is a relatively simple class that models the user (i,e the one that clicks the ad linkk or not)
    The primary function is the user response to when an ad is shown (ie show_ad)
    """

    #import numpy as np
    # import random
    # from collections import Counter
    # #import bidder_narasimhan
    # from bidder_narasimhan import Bidder
    
    def __init__(self):
        # Initializes the probability with the random-uniform distribution
        self.__probability = random.uniform(0, 1)

    def __repr__(self):
        return "this is a user with a secret click probability of " + str(self.__probability)
    
    def __str__(self):
        return self.__repr__()
    
    
    def show_ad(self):
        # The show ad function is simple in that it returns a True / False value based on 
        # a random choice of the probability distribution
        return  np.random.choice((True, False), p = [self.__probability, 1-self.__probability])

class Auction:
    
    """
    The auction class sets the bidding rules and manages both the bidders and users
    It also determines the winning bid and the price (which is the second highest)
    Also, included is the interaction with the bidder to request and then notify the bidder of the outcome
    The user function models the user (i,e the one that clicks the ad linkk or not)
    
    Key Assumption: Given the max reward is $1, we will limit max bids to at most $5
    """
    # import numpy as np
    # import random
    # from collections import Counter
    # from bidder_narasimhan import Bidder

    def __init__(self, users, bidders):
        
        # Initializes the auction class with users, bidders, auction history
        # balances are tracked by bidder
        
        self.users = users
        self.bidders = bidders
        self.auction_history = []
        
        # To note, I have used id(bidder) instead of (bidder) as that is incomprehensible
        self.balances = {id(bidder): 0 for bidder in bidders} ########### NEW LINE
        
        #print("*"*100, '\n')
        #print('Beginning balances : ',self.balances, '\n','-'*100)
        
        self.num_rounds = 0
        self.auction_active_bidder = True
        
    def __repr__(self):
        return "This is a second price auction with " + str(len(self.users)) + " users and " + str(len(self.bidders)) + " bidders"
    
    def __str__(self):
        return self.__repr__()    
    
    def execute_round(self):
        
        while self.auction_active_bidder == True:
        
            ############  EXECUTE ROUND  #### This is the principal function orchestrator #####################
            ###################################################################################################

            ############ NUMBER OF AUCTION ROUNDS -- Passed from Bidder #######################################

            for bidder in self.bidders:
                
                self.num_rounds = bidder.num_rounds
            
            all_invalid_bidders = any(x > -1000 for x in self.balances.values())


            #########  if the -ve balance of ALL bidders is < -1000, then break ###############################

            while not all_invalid_bidders:
                return "no bidders are qualifed as all balances are below -1000"
                break

            #########  Proceed with the auction is even 1 bidder has a balance > -1000 #########################
            ####################################################################################################

            else:
                # Initialize dictionary and lists for tracking bids
                bids_dict = {}
                bids_list = []
                bids_list_raw = []

                ########## STEP 1. SELECT USER (from the pool of users) ########################################

                chosen_user = random.randint(0, len(self.users)-1)
                #print('Selected User: ', id(chosen_user), '\n','-'*100) 

                ########### STEP 2. COLLECT BIDS (send to all bidders) #########################################

                for bidder in self.bidders:
                    if self.balances[id(bidder)] > -1000:
                        bids_dict[bidder] = bidder.bid(chosen_user)
                        self.bidding_round = bidder.bidding_round

                        self.auction_history.append((id(bids_dict[bidder]), bids_dict[bidder])) #bidder
                        highest_bid = 0
                        winning_price = 0
                    else:
                        print("Bidder ", id(bidder), "balance is less than -1000. Cannot continue bid" )
         #               #raise Exception("Bidder's balance is less than -1000. Cannot continue bid")
                        continue

                #print("Current bidding Round: ", self.bidding_round, '\n','-'*100)

                ############ STEP 3. DETERMINE WINNING BID ####################################################

                for bidder, bid_value in bids_dict.items():

                    bids_list_raw.append((bidder, bid_value))
                    ## only needed to track a human readable bidder id
                    bids_list.append((id(bidder), bid_value))

                ########### STEP 4. SORT THE Bids List based on price #########################################

                sorted_list = sorted(bids_list, key=lambda t:t[1])    
                #print('Sorted bids list', sorted_list, '\n','-'*100 )

                #------------- for analysis only - creating a copy with id(bidder) ---------------------------
                sorted_list_raw = sorted(bids_list_raw, key=lambda t:t[1])
        #        print('sorted bids list RAW', sorted_list_raw, '\n','-'*100 )


                ########### STEP 5. Select second highest price ###############################################

                if len(sorted_list) > 1:
                    winning_price = (sorted_list_raw)[-2][1]
                    winning_bidder = (sorted_list_raw)[-1][0]
                else:
                    winning_price = (sorted_list_raw)[0][-1]
                    winning_bidder = (sorted_list_raw)[0][0]

        #        print('Winning Price: ', winning_price, '\n','-'*100)
        #        print('winning bidder', winning_bidder, '\n','-'*100)

                ########### STEP 6. Determine if there are more than 1 bidders with same price ################

                multiple_winning_bidders = [tup for tup in sorted_list_raw if tup[1] == winning_price]

                if len(multiple_winning_bidders)>1:
                    #print('List of biders that submitted similar bids: ' , multiple_winning_bidders, '\n','-'*100)
                    randindex = random.randint(0, len(multiple_winning_bidders)-1)
                    winning_bidder = multiple_winning_bidders[randindex][0]
                    #print('Winning bidder from list of similar priced bids: ', winning_bidder, '\n','-'*100)
                else: 
                    pass
                    #winning_bidder = multiple_winning_bidders[0][0]

                #print('Winning Bidder: ', id(winning_bidder), '\n','-'*100)
                #print('Winning Price: ', winning_price, '\n','-'*100)

                ############ STEP 7. Validate USER CLICK after SHOW AD ###########################################

                ad_result = self.users[chosen_user].show_ad()
                #print('User Clicked on Ad?: ', ad_result,'\n','-'*100)

                ############# STEP 8.NOTIFY BIDDER & UPDATE BALANCES #############################################

                for bidder in self.bidders:
                    if bidder == winning_bidder and ad_result == True:
                        #print(id(bidder), "bidder == winning_bidder and ad_result == True:")
                        self.balances[id(bidder)] -= winning_price
                        self.balances[id(bidder)] += 1

                        bidder.notify(True, winning_price, ad_result)

                    elif bidder == winning_bidder and ad_result == False:
                        #print(id(bidder), "bidder == winning_bidder and ad_result == False")
                        self.balances[id(bidder)] -= winning_price

                        bidder.notify(True, winning_price, ad_result)

                    else:
                        #print(id(bidder), "Did not win bid - only notify")
                        bidder.notify(False, winning_price, None)
                #print('-'*100, '\n','balances at end of bidding round', self.balances,'\n','-'*100)
                
                ############# STEP 9.EXIT AUCTION ##### based on num_rounds #######################################
                
                self.bidding_round += 1
                
                if self.bidding_round >  self.num_rounds:
                    #print("End of bidding round")
                    self.auction_active_bidder = False
                    break
