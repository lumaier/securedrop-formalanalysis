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
if argv[1] in ['Auto_Secrecy_Source_Message']:
  match = matchAgainstList([
    '!KU( ~msg',
    re.compile(r'Server_In\(.+msg_s2j'),
    '!KU( sign(<\'ephemeral',
    re.compile(r'!KU\( ~je?_sk')
  ], lines)
elif argv[1] in ['Auto_PFS_Source_Message']:
  match = matchAgainstList([
    '!KU( ~msg',
    re.compile(r'!KU\( ~je?_sk'),
    '!KU( ~ltk',
    re.compile(r'Server_In\(.+msg_s2j'),
    '!KU( sign(<\'msg_s2j',
    '!KU( sign(<\'signing',
    '!KU( sign(<\'ephemeral'
  ], lines)
elif argv[1] in ['Auto_Secrecy_Journalist_Message']:
  match = matchAgainstList([
    '!KU( ~msg',
    re.compile(r'Server_In\(.+msg_s2j'),
    '!KU( ~ltk'
  ], lines)
elif argv[1] in ['Auto_Non_Injective_Agreement_Source_Message']:
  match = matchAgainstList([
    re.compile(r'Client_In\(.+msg_s2j'),
    re.compile(r'Server_In\(.+msg_s2j'),
    re.compile(r'!KU\( aenc.+msg_s2j'),
    re.compile(r'!KU\( sign.+msg_s2j'),
    '!KU( ~ltk'
  ], lines)

if match is not None:
  print(match)