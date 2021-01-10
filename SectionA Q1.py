# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 05:53:47 2021

@author: lafree
"""
          
 # -*- coding: utf-8 -*-
"""

"""


#Question 1:Counting all unique four letter words in the file. 
    #creating an empty set 
words = set()
    #using with statement    
with open ("C:\words.txt", 'r') as word_stimuli::
    for line in word_stimuli:        
     #using a dictionary to define key areas to be adhered to:
          #ignoring case of word by changing all words to lower case
          #finding words with 4 characters using len function
       unique_4Lwords = {word for word in line.lower().split() if len(word)==4 and "'" not in word}
       words.update(unique_4Lwords)
    unique_word_stimuli = (len(words)) 
    #printing out the number of my unique four letter words.  
    print("Uniquefour: " + str(unique_word_stimuli))
   
#Question 2:Dividing the four letter words based upon the last two letters of the word    
    #creating a list  
word_list = []
    #Using for statement  
for word in words:  
    #Checking the last two characters and frequency   
    word_list.append(word[-2:])
def character_frequency(word_list):
    word_set = set(word_list)

    word_frequency = {}

    for ch in word_set:
        if word_list.count(ch) >= 30:
            word_frequency[ch] = word_list.count(ch)
        
    return word_frequency

#Question 3: Printing the list of word endings and their number
 
print(character_frequency(word_list))

#Question 4:Selecting one word to create a stimulus list
    #Initializing 'stimulus list' 
stimulus_list = []

for x in words:
    for word in x.split():
        if word.endswith('ps'):
    #Question 4: Print list of chosen word stimuli        
            print(word)

#Closing file
word_stimuli.close()
