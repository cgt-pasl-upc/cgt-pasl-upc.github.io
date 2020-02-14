#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import json
import sys
import re

LABEL_PUBLIC = 'Public'
LIST_DOING = 'Doing'
LIST_DONE = 'Done'

def assertDate(value, message):
    try:
        datetime.datetime.strptime(value, '%Y-%m-%d')
    except ValueError:
        assert(False, message)

def findUniqueByAtribute(elems, name, value):
    for elem in elems:
        if elem[name] == value:
            return elem
    assert(False, '"' + value + '" object not found.')

def printCards(cards, actions):
    for card in cards:
        print('## ' +  card['name'])
        print(' ')
        print(card['desc'])
        print('')
        actions = [ a for a in actions if a['type'] == 'commentCard' ]
        actions = [ a for a in actions if a['data']['card']['id'] == card['id'] ]
        actions = [ a for a in actions if '[PUBLIC]' in a['data']['text'] ]
        for action in actions:
            print(re.sub('^.*\[PUBLIC\].*\r?\n', '', action['data']['text'], re.MULTILINE))
            print('')

def getCardsDoingToDone(start, end, cards, actions):
    actions = [ a for a in actions if a['date'] >= start and a['date'] <= end ]
    actions = [ a for a in actions if a['type'] != 'deleteCard' ]
    actions = [ a for a in actions if 'card' in a['data'] ]
    actions = [ a for a in actions if 'listBefore' in a['data'] and a['data']['listBefore']['id'] == listDoing['id'] ]
    actions = [ a for a in actions if 'listAfter' in a['data'] and a['data']['listAfter']['id'] == listDone['id'] ]
    cardsIds = [ a['data']['card']['id'] for a in actions ]
    return [ c for c in cards if c['id'] in cardsIds ]

def getCardsDoing(cards):
    return [ c for c in cards if listDoing['id'] == c['idList'] ]

assert(len(sys.argv) == 3, 'Falten les dates d\'inici i final.')
assertDate(sys.argv[1], 'La data d\'inici no és correcta')
assertDate(sys.argv[2], 'La data de finalització no és correcta')

startDate = sys.argv[1]
endDate = sys.argv[1]

json = json.load(sys.stdin)
publicLabel = findUniqueByAtribute(json['labels'], 'name', LABEL_PUBLIC)
listDoing = findUniqueByAtribute(json['lists'], 'name', LIST_DOING)
listDone = findUniqueByAtribute(json['lists'], 'name', LIST_DONE)
cards = [ c for c in json['cards'] if publicLabel['id'] in c['idLabels'] ]

print('Setmana del ' + startDate + ' ' + endDate)
print('-----------------------------')
print('')
print('# Què hem fet?')
print('')
printCards(getCardsDoingToDone(startDate, endDate, cards, json['actions']), json['actions'])
print('')
print('# Què estem fent?')
print('')
printCards(getCardsDoing(cards), json['actions'])
