import wordscore

def run_scrabble(rack):
    
    """
    This is a modified version of the traditional scrabble game. The user plays the game
    from the command promt by running run_scrabble and provides the 'rack' as the input.
    The rack is the selection of between 2-7 words and special characters (* or ? only)
    
    The highlights of the game are
    
    1. Allow anywhere from 2-7 character tiles (letters A-Z, upper or lower case)
    2. Do not restrict the number of same tiles (e.g., a user is allowed to input ZZZZZQQ).
    3. There can be a total of only two wild cards in any user input 
       that is, one of each character: one `*` and one `?`). 
       Only use the `*` and `?` as wildcard characters. 
    4. A wildcard character can take any value A-Z. 
    5. Wildcard characters are scored as 0 points, just like in the real Scrabble game. 
       A word that just consists of two wildcards can be made, should be outputted and 
       scored as 0 points.  
    """
    
    ############### INITIALIZATION ################################
    
    # converts the input rack to lower case
    rack_low = rack.lower() 
    
    
    rack_letters = list(rack_low) 
    # converts the rack to a list of letters
    
    valid_words = [] 
    # An empty list that will eventually hold all valid words from the scrabble dictionary sowpods.txt
    
    valid_rack = True
    # A boolean condition the evaluates the contents of the rack as valid or not
    
    clean_rack = []
    # this removes the special characters from the rack

    ################ VALIDATIONS ###################################    
    
    
    if (rack_low.count('?') > 1 or  rack_low.count('*')) > 1:
        return ("You have entered more than 2 special characters")
        valid_rack = False
        
        # checks the condition for only 1 of the special characters is allowed
        # ie the user cannot enter two * or two ?
        # the user can enter one * and one ?
    
    
    elif len(rack_low) > 7 or len(rack_low) < 2:
        return ("You have entered more than 7 characters or less than 2")
        valid_rack = False
        
        # checks the number of letters in the rack for a minimum of 2 and maximum of 7

    ######################################################################
    
    elif all(x.isalpha() or x in ('?', '*') for x in rack_low):
        valid_rack = True
        pass
    
         # checks if the contains only alphabets or special characters (* ?)
    
    else:
        return ('You have entered non-permitted characters. Please enter only alphabets and/or special characters * and ?')

        valid_rack = False
        
         # this condition needs rework
         # would 
    
    ######################################################################

    #    Deprecated code: Replaced with condition above (would like to make this work
    #    but condition is not tight enough

    #     elif all(x.isalpha() == False and x not in ('?', '*') for x in rack_low):
    #         valid_rack = False
    #         return ('You have entered non-permitted characters. Please enter only alphabets and/or special characters * and ?')
            
        
    #         # checks if the contains only alphabets or special characters (* ?)
        
    #     else:
    #         valid_rack = True
            
    #         # this condition needs rework
        
    ######################################################################    
        
    
    if valid_rack:

        # reads the scrabble reference dictionary and creates a data list
        # after stripping the line breaks
        
        with open("sowpods.txt","r") as infile:
            raw_input = infile.readlines()#[0:1000]
            data = [datum.strip('\n') for datum in raw_input]
        
        # this is the matching algorithm that iterates through each word in the
        # scrabble dictionary (data) and checks whether the letters exists in the 
        # user input (rack). This also accounts for the two special characters (*, ?)
        # and by a process of elimination is able to implicitly substitute them for 
        # other alphabets
        
        for word in data:
            word_low = word.lower()
            temp_rack_letters = rack_letters.copy() 
            for letter in word_low:
                if letter in temp_rack_letters :
                    temp_rack_letters .remove(letter)
                elif '*' in temp_rack_letters :
                    temp_rack_letters .remove('*') 
                elif '?' in temp_rack_letters :
                    temp_rack_letters .remove('?')
                else:
                    break 
            
            ####################### WILDCARD ZERO-ORIGINAL ###################
            
            # else:
            #     valid_words.append([score_word(word_low), word_low.upper()])
        
            ####################### WILDCARD ZERO-REWORK ########################
        
            else:
                clean_rack = ''.join([i for i in rack_low if i.isalpha()])
                # removes the special characters from the rack 
                
                valid_words.append([score_word(clean_rack), word_low.upper()])
                # returns the scores for the words in the clean_rack
        
            ######################################################################
        
        
        
        # Sort the valid words list in descending order of score 
        
        valid_words.sort(reverse = True)

        
        # this is the section where we print the score and word
        # note this is already in descending order in valid_words
        
        for entry in valid_words:
            score = entry[0]
            word_low = entry[1]
            print((score, word_low))

        # this is the final print of the count of all valid words
        print(len(valid_words))
    
    else:
        valid_rack = False 
        
    