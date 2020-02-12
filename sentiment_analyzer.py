#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:51:41 2019

@author: mariobeck
"""

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

s = SentimentIntensityAnalyzer()

liste = ["I love python", "I hate python"]

for each in liste:
    print(each)
    print(s.polarity_scores(each))
    print("---------------------------------------------------------------")

#sentiment = s.polarity_score("I hate America")