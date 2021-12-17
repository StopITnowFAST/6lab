#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дан текст. Определить количество букв и в первом предложении. 
# Рассмотреть два случая:
# 1. известно, что буквы и в этом предложении есть;
# 2. букв и в тексте может не быть.

if __name__ == '__main__':

    text = input("enter some text")

    if (text.find('.') > 0):
        index = text.find('.')
    elif (text.find('!') > 0):
        index = text.find('!')
    elif (text.find('?') > 0):
        index = text.find('?')

    new_text = text[0:index]
    if (new_text.count('и') > 0):
        print(new_text.count('и'))
    else:
        print("not found")
