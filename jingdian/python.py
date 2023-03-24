#!/usr/bin/env python3

for i in range(1, 82):
    name = 'qihuang/lingshu/{}.txt'.format(i)
    f = open(name, 'w')
    f.write('空白')
    f.close()

    name = 'qihuang/nanjing/{}.txt'.format(i)
    f = open(name, 'w')
    f.write('空白')
    f.close()

    name = 'qihuang/suwen/{}.txt'.format(i)
    f = open(name, 'w')
    f.write('空白')
    f.close()