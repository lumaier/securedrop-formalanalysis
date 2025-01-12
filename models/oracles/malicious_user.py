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
if argv[1] in ['Auto_Executability_Submission', 'Auto_Executability_Journalist_Response']:
  match = matchAgainstList([
    re.compile(r'^(?!split).*')
  ], lines)
elif argv[1] in ['Auto_Secrecy_Source_Ciphertext']:
  match = matchAgainstList([
    '!Ltk_',
    '!Pk_',
    '!Newsroom_',
    '!KU( ~re_sk',
    '!KU( ~j_fetch_sk )',
    '!KU( \'g\'^(~j_fetch_sk*~re_sk*~x) )',
    '!KU( ~id',
    'Server_In( ~sess, $Server,           <\'ciphertext\', <~msg',
    'Server_In( ~sess.3, $Server.1,           <\'ciphertext\', <~msg',
    'Server_In( ~sess.1, $Server, <\'solution\', ~id> )',
    '~ltk',
    '!KU( ~sess )',
    '!KU( ~sess.1 )',
    '!KU( sign(<\'signature\', j_fetch_pk>, ~ltk) )'
  ], lines)
elif argv[1] in ['Auto_Secrecy_Journalist_Ciphertext']:
  match = matchAgainstList([
    '!Ltk_',
    '!Pk_',
    '!Newsroom_',
    '!KU( ~re_sk',
    '!KU( kdf(',
    '!KU( ~pass',
    '!KU( \'g\'^(~x*~re_sk.1*kdf(<\'Fetch\', ~passphrase>)) )',
    '!KU( ~id.1',
    'Server_In( ~sess, $Server,           <\'ciphertext\', <~msg',
    'Server_In( ~sess.3, $Server.1,           <\'ciphertext\', <~msg',
    'Server_In( ~sess.1, $Server, <\'solution\', ~id> )',
    'Server_In( ~sess.2, $Server, <\'solution\', ~id.1> )',
    '~ltk',
    '!KU( ~sess.1 )',
    '!KU( ~sess.2 )',
    '!KU( sign(<\'signature\', j_fetch_pk>, ~ltk) )',
    re.compile(r'^(?!split).*')
  ], lines)

if match is not None:
  print(match)