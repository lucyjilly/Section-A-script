# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 05:53:47 2021

@author: lafree
"""
          
 #Count all unique four letter words in the file. 
words = set()

with open ("C:\\Users\\LUCY\\Downloads\\words (1).txt", 'r') as word_stimuli:
    for line in word_stimuli:
       unique_4Lwords = {word for word in line.lower().split() if len(word)==4 and "'" not in word}
       words.update(unique_4Lwords)
    unique_word_stimuli = (len(words))
    print("Uniquefour: " + str(unique_word_stimuli))
   
    assert unique_word_stimuli == 2981
        
word_list = []
for word in words:
    word_list.append(word[-2:])
    

def character_frequency(word_list):
    word_set = set(word_list)

    word_frequency = {}

    for ch in word_set:
        if word_list.count(ch) >= 30:
            word_frequency[ch] = word_list.count(ch)
        
    return word_frequency

        
      



