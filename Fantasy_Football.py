#! /usr/bin/env python3
# Fantasy_Football.py - I want to calculate a league manager's draft grade in
# fantasy football based off of Yahoo's projected point totals for each player.

import sys, os, openpyxl, pprint

y = 0


# Turn the excel worksheet Fantasy_Football.xlsx into a python dictionary
wb = openpyxl.load_workbook('Fantasy_Football.xlsx')
chart = wb['Sheet1']

# create a dictionary that will have the football player as the key
# and his projected output and position as the values
PlayerData = {}

for i in range(2, 32):
    # Each row in the spreadsheet contains a key-value pair for a player.
    player = chart['A' + str(i)].value
    projected_points = chart['B' + str(i)].value
    # qb = chart['C' + str(i)].value
    
    # player = chart.cell(row=i, column=1).value
    # points = chart.cell(row=i, column=2).value

    PlayerData.setdefault(player, {projected_points})
    # PlayerData[player].setdefault(qb, {'projected_points': projected_points})


    resultFile = open('FF_draft_calc.py', 'w')
    resultFile.write('playerData = ' + pprint.pformat(PlayerData))
    resultFile.close()

theirQB = input('Who is your starting quarterback?\n') # User types in their quarterback
if theirQB in PlayerData.keys(): # if what the user inputs is a valid key in the PlayerData dictionary...
   a = PlayerData[theirQB].pop()
   y += a

for i in range(32, 49):
    player = chart['A' + str(i)].value
    projected_points = chart['B' + str(i)].value

    PlayerData.setdefault(player, {projected_points})

    resultFile = open('FF_draft_calc.py', 'a')
    resultFile.write('playerData = ' + pprint.pformat(PlayerData))
    resultFile.close()

theirDEF = input('What team\'s city are you starting at Defense?\n')
if theirDEF in PlayerData.keys():
    a = PlayerData[theirDEF].pop()
    y += a

for i in range(49, 92):
    player = chart['A' + str(i)].value
    projected_points = chart['B' + str(i)].value

    PlayerData.setdefault(player, {projected_points})

    resultFile = open('FF_draft_calc.py', 'a')
    resultFile.write('playerData = ' + pprint.pformat(PlayerData))
    resultFile.close()

theirRB1 = input('Who is your RB1?\n')
if theirRB1 in PlayerData.keys():
    a = PlayerData[theirRB1].pop()
    y += a

theirRB2 = input('Who is your RB2?\n')
if theirRB2 in PlayerData.keys():
    a = PlayerData[theirRB2].pop()
    y += a

for i in range(92, 140):
    player = chart['A' + str(i)].value
    projected_points = chart['B' + str(i)].value

    PlayerData.setdefault(player, {projected_points})

    resultFile = open('FF_draft_calc.py', 'a')
    resultFile.write('playerData = ' + pprint.pformat(PlayerData))
    resultFile.close()

theirWR1 = input('Who is your WR1?\n')
if theirWR1 in PlayerData.keys():
    a = PlayerData[theirWR1].pop()
    y += a

theirWR2 = input('Who is your WR2?\n')
if theirWR2 in PlayerData.keys():
    a = PlayerData[theirWR2].pop()
    y += a

for i in range(140, 164):
    player = chart['A'+ str(i)].value
    projected_points = chart['B' + str(i)].value

    PlayerData.setdefault(player, {projected_points})

    resultFile = open('FF_draft_calc.py', 'a')
    resultFile.write('playerData = ' + pprint.pformat(PlayerData))
    resultFile.close()

theirTE = input('Who is your starting TE?\n')
if theirTE in PlayerData.keys():
    a = PlayerData[theirTE].pop()
    y += a

for i in range(2, 183):
    player = chart['A' + str(i)].value
    projected_points = chart['B' + str(i)].value

    PlayerData.setdefault(player, {projected_points})

    resultFile = open('FF_draft_calc.py', 'a')
    resultFile.write('playerData = ' + pprint.pformat(PlayerData))
    resultFile.close()

FLEX = input('Who are you flexing with?\n')
if FLEX in PlayerData.keys():
    a = PlayerData[FLEX].pop()
    y += a

for i in range (162, 183):
    player = chart['A' + str(i)].value
    projected_points = chart['B' + str(i)].value

    PlayerData.setdefault(player, {projected_points})

    resultFile = open('FF_draft_calc.py', 'a')
    resultFile.write('playerData = ' + pprint.pformat(PlayerData))
    resultFile.close()

KICKER = input('Who is your kicker?\n')
if KICKER in PlayerData.keys():
    a = PlayerData[KICKER].pop()
    y += a
    print(y)
if y >= 1880:
    print('Draft Grade:\nA+')
elif y >= 1860:
    print('Draft Grade:\nA')
elif y >= 1820:
    print('Draft Grade:\nA-')
elif y >= 1780:
    print('Draft Grade:\nB+')
elif y >= 1760:
    print('Draft Grade:\nB')
elif y >= 1740:
    print('Draft Grade:\nB-')
elif y >= 1720:
    print('Draft Grade:\nC+')
elif y >= 1670:
    print('Draft Grade:\nC')
elif y >= 1640:
    print('Draft Grade:\nC-')
elif y >= 1550:
    print('Draft Grade:\nD')
else:
    print('Draft Grade:\nF')


    
   


# Prompt user to enter name of QB from FFP dictionary

# Prompt user to enter WR1

# Prompt user to enter WR2

# Prompt user to enter RB1

# Prompt user to enter RB2

# Prompt user to enter flex

# Prompt user to enter K

# Prompt user to enter DEF
