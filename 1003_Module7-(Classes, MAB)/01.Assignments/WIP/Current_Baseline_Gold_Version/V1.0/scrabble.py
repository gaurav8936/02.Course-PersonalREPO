from wordscore import *

def run_scrabble(rack):
    rack_low = rack.lower()
    rack_letters = list(rack_low)
    valid_words = []
    
    with open("sowpods.txt","r") as infile:
        raw_input = infile.readlines()#[0:1000]
        data = [datum.strip('\n') for datum in raw_input]
    
    for word in data:
        word_low = word.lower()
        temp_rack_letters = rack_letters.copy() # keep the original
        for letter in word_low:
            if letter in temp_rack_letters :
                temp_rack_letters .remove(letter)
            elif '*' in temp_rack_letters :
                temp_rack_letters .remove('*') 
            elif '?' in temp_rack_letters :
                temp_rack_letters .remove('?')
            else:
                break # You want to exit the loop if letter dont match
        else:
            valid_words.append([score_word(word_low), word_low])
    
    valid_words.sort(reverse = True)
    
    for entry in valid_words:
        score = entry[0]
        word_low = entry[1]
        print((score, word_low))

    print("Total number of words:", len(valid_words))
    

    
