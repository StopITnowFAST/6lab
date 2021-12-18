#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано слово s1. Получить слово s2, образованное нечетными буквами слова s1.

if __name__ == '__main__':

    word_old = input("enter word")
    word_new = ""
    
    for i in range(len(word_old)):
        if (i % 2 == 0):
            word_new += word_old[i]

    print(word_new)
