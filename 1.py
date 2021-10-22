# Дано слово s1. Получить слово s2, образованное нечетными буквами слова s1.

wordOld = 'pirates'
wordNew = list(wordOld)

del wordNew[1::2]

print(''.join(wordNew))
