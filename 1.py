#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано слово s1. Получить слово s2, образованное нечетными буквами слова s1.

if __name__ == '__main__':


    word_old = input("enter word")
    word_new = list(word_old)

    del word_new[1::2]

    print(''.join(word_new))
