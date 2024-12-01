#!/usr/bin/env python3

from sys import argv, stdin, exit
import re

def splitter(line):
  splitted = line.split(':')
  return (splitted[0], splitted[1].strip())

lines = list(map(splitter, stdin.readlines()))
if not lines:
  exit(0)

def subToken(token, line):
  (num, goal) = line
  if isinstance(token, str):
    return num if token in goal else None
  else:
    return num if token.search(goal) is not None else None

def matchAgainstList(priorityList, lines):
  for token in priorityList:
    try:
      return next(filter(bool, map(lambda line: subToken(token, line), lines)))
    except StopIteration:
      pass

match = None
if argv[1] in ['Auto_Secrecy_Journalist_Message']:
  match = matchAgainstList([
    '!KU( ~msg.1 )',
    '!KU( kdf(<kdf(~ss),',
    '!KU( kdf(~ss) )',
    '!KU( ~ss )',
    '!KU()'
  ], lines)
elif argv[1] in ['Auto_PFS_Journalist_Message']:
  match = matchAgainstList([
    '!KU( pk(',
    '!KU( sign',
    '!KU( ~msg',
    '!KU( hkdf(<\'g\'^(~j_dh_sk*hkdf(<\'DH\', ~passphrase>)),',
    '!KU( hkdf(<\'DH\'',
    '!KU( ~passphrase',
    '!KU( senc(<\'msg_s2j',
    '!KU( aenc(<\'s_pk',
    '!KU( \'g\''
  ], lines)

if match is not None:
  print(match)