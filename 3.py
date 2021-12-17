#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Удалить из него все символы с n-го по m-й.

if __name__ == '__main__':

    words_old = input("enter some text")
    n = int(input("enter start cut")) - 1
    m = int(input("enter finish cut"))

    words_new = words_old[0:n] + words_old[m:]
    print(words_new)
