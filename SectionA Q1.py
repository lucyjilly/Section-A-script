# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 05:53:47 2021

@author: LUCY
"""
#Count all unique four letter words in the file. 
words = set()

with open ("C:\\Users\\LUCY\\Downloads\\words (1).txt", 'r') as fd:
     for line in fd:
        unique_4Lwords = {word for word in line.lower().split() if len(word)==4 and "'" not in word}
        words.update(unique_4Lwords)
        x = (len(words))
        print("Uniquefour: " + str(x))
        
      



