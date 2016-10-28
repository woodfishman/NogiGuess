#!usr/bin/env/python
#-*- coding=utf 8 -*-

# This is a very simple guess game.
# I may add hints to it sometime.

import pandas as pd
import sys
import random
import csv


def prepare(df):
    name = random.sample(list(df.index.values), 1)
    qlist = list(df.columns.values)
    qs = random.sample(qlist, 6)
    return name, qs


def gameloop(name, qs, qt, df):
    if name != 'HirateYurina':
        for q in qs:
            question = qt[q]
            value = df.ix[name[0]][q]
            answer = input('Question is: %s %s' % (question, value))
            if answer == name[0]:
                print('Bingo!')
                break
            else:
                print('Wrong!')
        print('Your Luck ran out. Try again!')
        print('The member is:', name[0])
    else:
        for q in qs:
            question = qt[q]
            value = df.ix[name[0]][q]
            answer = input('Question is: %s %s' % (question, value))
            if answer == name[0]:
                print('Bingo!')
                break
            else:
                print('Wrong!')
        new_an = input('The member is not one of Nogichans! So what is your answer?')
        if new_an == name[0]:
            print('Finally!')
        else:
            print('Your Luck ran out. Try again!')


def main():
    df = pd.read_csv('ngzkdata.csv', header=0, index_col=0)
    names = df.index.values
    names = names[names != 'Hirate Yurina']
    names = names.tolist()
    reader = csv.reader(open('questions.csv'))
    qt = {}
    for row in reader:
        k, v = row
        qt[k] = v
    while True:
        print('Now member is ready!')
        print('Remember answers only in these NAMES:\n', names)
        (name, qs) = prepare(df)
        gameloop(name, qs, qt, df)
        r2 = input('Now type any key to play again or x for exit')
        if r2 == 'x':
            break

if __name__ == '__main__':
    main()
