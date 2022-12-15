# this is the original name of the function (had word_low)
# I know this doesn't mean much, but wanted it to be symbolic and help me understand
# the code better

#def score_word(word_low):

# renamed the function to take the parameter (rack_low
# this is symbolic as note above

def score_word(rack_low):
    
    # Deprecating the scores (from original dictionary)
    
    # scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
    #       "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
    #       "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
    #       "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
    #       "x": 8, "z": 10}
    
    # modifying scores to include the two special characters: ? and *
    
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10, "?": 0, "*": 0}    
    
    total = 0
    
#    this is the original code (with word_low)
#    for letter in word_low:
    
    # Run through all letters in the word and return the score (ie total)
    # trying to run program with letters from the rack
    
    for letter in rack_low:
        total = total + scores[letter]
    return total
