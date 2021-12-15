#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано слово. Определить, сколько различных букв в нем.

if __name__ == '__main__':


    word = 'heheheha'
    counter = 0

    for i in range(len(word)):
        if word[i] in word[i+1:len(word)]:
            counter += 1

    print(len(word)-(counter))
