# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 15:32:10 2021

@author: tmori
"""

import random

def hangman(word):
    wrong = 0
    stages = ["",
              "_________        ",
              "|                ",
              "|        |       ",
              "|        O       ",
              "|       /|\      ",
              "|       / \      "]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("Welcome to HUNGMAN!")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Please estimate one character.: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("You lose! The answer is \"{}\".".format(word))




ans = ["lemon",
       "berry",
       "banana"]

word = random.choice(ans)

hangman(word)