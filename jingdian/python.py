#!/usr/bin/env python3

for i in range(1, 22):
    name = 'dao/honglie/{}.txt'.format(i)
    f = open(name, 'w')
    f.write('空白')
    f.close()