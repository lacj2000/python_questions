from random import randint

tp = (randint(1, 100),randint(1, 100),randint(1, 100),randint(1, 100), randint(1, 100))

print('Os números sorteados são {}'.format(' '.join(map(str,tp))))
print('O maior numero é {}'.format(max(tp)))
print('O menor numero é {}'.format(min(tp)))
print('Os números ordenados são {}'.format(' '.join(map(str,sorted(tp)))))