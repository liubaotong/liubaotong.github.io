#!/usr/bin/env python3

for i in range(22, 37):
    name = 'bing/sanshiliuji/{}.txt'.format(i)
    f = open(name, 'w')
    f.write('空白')
    f.close()