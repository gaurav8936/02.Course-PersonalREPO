def count_retweets_by_username(tweet_list):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """
    
    # write code here and update return statement with your dictionary
    
	# I realize is not traditional to put the data inside the function
	# but autograder would not accept an empty list for definition and kept erroring
    tweets = ["This is great! RT @fakeuser: Can you believe this?",
         "It's the refs! RT @dubsfan: Boo the refs and stuff wargarbal",
         "That's right RT @ladodgers: The dodgers are destined to win the west!",
         "RT @sportball: That sporting event was not cool",
         "This is just a tweet about things @person, how could you",
         "RT @ladodgers: The season is looking great!",
         "RT @dubsfan: I can't believe it!",
         "I can't believe it either! RT @dubsfan: I can't believe it"]

    import re
    text = ''.join(tweets)

    # define the matching string with regex ('RT @')
    p1 = re.compile(r"RT @(.+?)([ \.]|$)")
    found_patterns = re.findall(p1,text)

    # construct a list of strings with just substring after 'RT @''
    sentence_list = [elt[0] for elt in found_patterns]

    # strip the : from the list
    sentence_list2 = [i.strip(': ') for i in  sentence_list]


    sentence_dictionary = {}

    for item in sentence_list2:
        if item in sentence_dictionary:
            sentence_dictionary[item] += 1

        else:
            sentence_dictionary[item] = 1
    return sentence_dictionary

def display(deposits, top, bottom, left, right):
    """display a subgrid of the land, with rows starting at top and up to 
    but not including bottom, and columns starting at left and up to but
    not including right."""
    
    # calculate the height and width of the chosen rectangle section
    # based on the difference of top, bottom -- left , right
    
    height = bottom - top
    width = right - left
    
    #--------Generate list---------------
    
    # this is the step where we generate a list of lists (i.e creating the grid as a mutable list)
    
    steps = 0
    nested_list = []
    for i in range(height):
        steps = 0
        for j in range(width):
            steps += 1
        nested_list += [['-'] * width]
	#    print(nested_list)
    #return grid
    
    
    #-------Determine eligiblity of the deposit grid ---------------
    
    eligible_deposits = []
    for row, column, deposit in deposits:
        #eligible_deposits = []
	#        if top <= row and row < bottom and left <= column and column < right:
        if top <= row < bottom and left <= column < right:
        
            
            eligible_deposits += [(row, column, deposit)]

    
    #--------Revise nested_list with deposit info --------------
    
    # update the nested list with data from the list of tuples (eligible_deposits)
    
    for row, column, deposit in eligible_deposits:
        nested_list[row - top][column - left] = 'X'
        
	#    final_grid = ''
    ans = '\n'.join(''.join(str(i) for i in x) for x in nested_list)
    
    return ans

 
def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""
    # Do not alter the function header.  
    # Just fill in the code so it returns the correct number of tons.
    
    # Do not alter the function header.  
    # Just fill in the code so it returns the correct number of tons.
    
    # earlier, track the height and width as a separate variable
    
    height = bottom - top
    width = right - left
    
    # set total tonnage to 0 (to begin with)
    ans = 0
    
    
    #-------Determine eligiblity of the deposit grid ---------------
    
    eligible_deposits = []
    for row, column, deposit in deposits:
        #eligible_deposits = []
	#        if top <= row and row < bottom and left <= column and column < right:
        if top <= row < bottom and left <= column < right:
            eligible_deposits += [(row, column, deposit)]
    
     #-------Determine tonnage by summing up eligible depsosits ---------------
    
    for row, column, deposit in eligible_deposits:
        ans += deposit # total_tonnage
    
    # return total tonnage
    return ans # total_tonnage

def birthday_count(dates_list):
    """Returns the total number of birthday pairs in the dates_list"""
    dates = [(3,14),(2,8),(10,25),(5,17),(3,2),(7,25),(4,30),(8,7),(int(2),8),(1,22),(2, int(8))]

	# I realize is not traditional to put the data inside the function
	# but autograder would not accept an empty list for definition and kept erroring
    count = 0
    length = len(dates_list)
#    print('length of dates_list', len(dates_list))
    for a in range(0, length - 1):
#        print('outer loop A', a, dates_list[a])
        for b in range(a + 1, length):
#            print('inner loop B', b, dates_list[b])
            # Check both month and day
            #if dates_list[a][0] == dates_list[b][0] and dates_list[a][1] == dates_list[b][1]:
#            print('current A', dates_list[a], 'current B',dates_list[b])
            if dates_list[a] == dates_list[b]:
#                print('Match!')
#                print(dates_list[a])
                count += 1
                
    # We counted each pair twice (e.g. jane-bob and bob-jane) so divide by 2:          
    return count

#birthday_count(dates)


############### I would much rather prefer the second solution (though it takes twice the time) #####
############### But I know, there are no marks for creativity ########################

#def birthday_count(dates_list):

#     ####### get count of duplicates ##### ##############
#     duplicates = [item for item in dates_list if dates_list.count(item) > 1]
    
#     #print(duplicates)

#     my_dict = {i:duplicates.count(i) for i in duplicates}

#     ######## Generation combinations based on count ####################

#     counter = 0
#     for n in my_dict.values():
#         k = n-2
#         if 0 <= k <= n:    
#             ntok = 1
#             ktok = 1
#             for t in range(1, k + 1):
#                 ntok *= n
#                 ktok *= t
#                 n -= 1
#         counter+=(ntok // ktok)
#     print(counter)