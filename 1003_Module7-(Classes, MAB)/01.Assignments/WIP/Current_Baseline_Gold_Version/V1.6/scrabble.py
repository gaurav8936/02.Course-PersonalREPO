import wordscore
import sys
import argparse

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
    
    ################ COMMAND LINE ARGS ###################################    
    
    # parser = argparse.ArgumentParser()
    # parser.add_argument('rack', nargs='?')
    # args = parser.parse_args()
    # if len(sys.argv) == 1:
    #     print("Please supply some letters. Ex: 'python scrabble.py RSTLNEI'")
    #     exit()
    # rack = args.rack.lower()
    
    # rack = sys.argv[1]
    # print(rack)
    # rack = str(rackin)
    
    # rack = str(sys.argv).lower()
    #renamed argv to 'rack' just to make it easier for me to read
    
    ############### INITIALIZATION ################################
    
    # converts the input rack to lower case
    rack_low = rack.lower() 
    
    
    rack_letters = list(rack_low) 
    # converts the rack to a list of letters
    
    valid_words = [] 
    # An empty list that will eventually hold all valid words from the scrabble dictionary sowpods.txt
    
    valid_rack = True
    # A boolean condition the evaluates the contents of the rack as valid or not
    
    clean_word = []
    # this removes the special characters from the rack
    # may not be really useful -- as the word is already formed
    
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
#                clean_word = ''.join([i for i in word_low if i.isalpha()])
                # removes the special characters from the rack 
                # print(clean_rack)
                # this is really not that helpful -- as it is already the fully formed word
                
                clean_rack = [letter for letter in rack_low if letter.isalpha()]
                #print(clean_rack)

                clean_word = [letter for letter in word_low if letter in clean_rack]
                # this seems to work -- matches only letter in word_low to that of the clean rack
                #print(clean_word)
                
           ####################### DUPLICATE WILDCARD (AA eg) ########################
        
                # scoring based on clean_word (aa) - clean _rack (a)
            
                # clean_word_deduplicate = [a for a in clean_word if not a in clean_rack or clean_rack.remove(a)]
                # this doesn't work either
                
                clean_word_deduplicate = set(clean_word) & set(clean_rack)
        
                #print(clean_word_deduplicate)
        
        
            ####################### WILDCARD ZERO-REWORK ########################
        
                #valid_words.append([wordscore.score_word(clean_word), word_low.upper()])
                # changing the code to take the new clean_word_deduplicate
                
                valid_words.append([wordscore.score_word(clean_word_deduplicate), word_low.upper()])
                
                # returns the scores for the words in the clean_rack
                # by using clean_word and word_low, they are both derived from word_low
                # so the basis is the same
                #print(valid_words)
                
        
            ######################################################################
    
    else:
        valid_rack = False 
    
    ################ with SORTED #######################
    valid_words_sorted = sorted(valid_words,key=lambda x:(-x[0],x[1]))
    valid_words_sorted_tuples = []
    valid_words_sorted_tuples = [tuple(l) for l in valid_words_sorted]
    return valid_words_sorted_tuples, len(valid_words)
