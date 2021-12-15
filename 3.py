#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Удалить из него все символы с n-го по m-й.

if __name__ == '__main__':

    wordsOld = 'Удалить из предложения символы с n по m'
    n = 7
    m = 20

    wordsNew = wordsOld[n:m]
    print(wordsNew)
