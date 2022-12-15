import numpy as np
import random
from collections import Counter
from auction_narasimhan import User
from auction_narasimhan import Auction
from bidder_narasimhan import Bidder as Default
from bidder_A import Bidder as A
from bidder_B import Bidder as B
from bidder_C import Bidder as C
from bidder_D import Bidder as D
from bidder_E import Bidder as E
from bidder_F import Bidder as F
from bidder_G import Bidder as G
from bidder_H import Bidder as H
from bidder_I import Bidder as I
from bidder_J import Bidder as J

#b1, b2, b3, b4, b5, b6, b7, b8, b9, b10 = Bidder(1,10), Bidder(1,10), Bidder(1,10), Bidder(1,10), Bidder(1,10), Bidder(1,10), Bidder(1,10), Bidder(1,10), Bidder(1,10), Bidder(1,10)
b0 = Default(1,100)
bA = A(1,100)
bB = B(1,100)
bC = C(1,100)
bD = D(1,100)
bE = E(1,100)
bF = F(1,100)
bG = G(1,100)
bH = H(1,100)
bI = I(1,100)
bJ = J(1,100)

# b0 = Default(1,100)
# bA = A(1,1000)
# bB = B(1,1000)
# bC = C(1,1000)
# bD = D(1,1000)
# bE = E(1,1000)
# bF = F(1,1000)
# bG = G(1,1000)
# bH = H(1,1000)
# bI = I(1,1000)
# bJ = J(1,1000)


#auction = Auction( [User()for i in range(10)], [b1, b2])

#auction = Auction( [User()for i in range(10)], [b0, bA, bB, bC, bD, bE, bF, bG, bH, bI, bJ])
auction = Auction( [User()], [b0, bA, bB, bC, bD, bE, bF, bG, bH, bI, bJ])
auction.execute_round()  

bal = auction.balances
print(bal)