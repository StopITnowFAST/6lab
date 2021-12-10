# Дано слово s1. Получить слово s2, образованное нечетными буквами слова s1.

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':


    wordOld = 'pirates'
    wordNew = list(wordOld)

    del wordNew[1::2]

    print(''.join(wordNew))
