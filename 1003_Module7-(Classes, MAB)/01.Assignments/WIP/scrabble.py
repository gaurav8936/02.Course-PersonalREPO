import wordscore
import sys
from collections import Counter

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
    
    clean_word = []
    # this removes the special characters from the rack
    # may not be really useful -- as the word is already formed
    
    clean_rack = []
    # this removes the special characters from the rack
   
    ################ VALIDATIONS ###################################
    if (rack_low.count('?') > 1 or  rack_low.count('*')) > 1:
        return ("You can use only one of the wildcards at a time. E.g.  you can use just the '*' or '?' or both, but not two of the same")
        valid_rack = False
        
        # checks the condition for only 1 of the special characters is allowed
        # ie the user cannot enter two * or two
        # the user can enter one * and one ?
    
    if (rack_low.count('?') +  rack_low.count('*')) > 2:
        return ("You have entered more than 2 wildcards")
        valid_rack = False
        
        # checks the condition that no more than 2 wildcards are allowed
        # the user can enter one * and one ?. which would be valid
        # however, a combination like '**?' would throw this error
    
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
            
            #iterate through the word dictionary, one word/letter at a time and compare with the rack
            # start with createing a copy of the rack as temp_rack_letters
            
            candidate = True
            # use the candidate flag to track a valid/invalid word
            
            # Iterate each letter in the word and check if the letter is in the
            # Scrabble rack. If used once in the rack, remove the letter from the rack.
            # If there's no letter in the rack, skip the letter.
                
            for letter in word_low:
                if letter in temp_rack_letters :
                    temp_rack_letters .remove(letter)
                elif '*' in temp_rack_letters :
                    temp_rack_letters .remove('*') 
                elif '?' in temp_rack_letters :
                    temp_rack_letters .remove('?')
                else:
                    candidate = False
 
        
            if candidate == True:
                clean_rack = [letter for letter in rack_low if letter.isalpha()]
                # removes the special characters from the rack 

                clean_word = list((Counter(rack_low) & Counter(word_low)).elements())
                # this finds the common letters in the rack and compares that with the word
                # handles cases of duplicate letters in rack (like ZZZZEE) 
                
                valid_words.append([wordscore.score_word(clean_word), word_low.upper()])
                
                # returns the scores for the words in the clean_rack
                # by using clean_word and word_low, they are both derived from word_low
                # so the basis is the same
                
    else:
        valid_rack = False 
    
    valid_words_sorted = sorted(valid_words,key=lambda x:(-x[0],x[1]))
    # we now sort the list on the basis of score (descending and alphabet (ascending))
    
    valid_words_sorted_tuples = [tuple(l) for l in valid_words_sorted]
    # this converts list content to one that is required by the course - a list of tuples
    
    return valid_words_sorted_tuples, len(valid_words)