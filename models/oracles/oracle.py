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
if argv[1] == 'SecureChannelSources':
  match = matchAgainstList([
    '~~>',
    re.compile(r'^\(∃'),
    re.compile(r'Client_Out\( ~sess(\.\d*), \$Server(\.\d*), ~id(\.\d*)'),
    '!Submission',
    re.compile(r'^\(last'),
    re.compile(r'^(Client|Server)Source'),
    'KU( senc',
  ], lines)
elif argv[1] == 'FetchingSecrecy':
  lines.reverse()
  match = matchAgainstList([
    'Honest( \'g\' )',
    re.compile(r'!Submission\(.+\'g\','),
    re.compile(r'!Submission\(.+\'g\'>'),

    re.compile(r'KU\( ~(r|x|(j|s)_fetching_sk)\.?\d* \)'),
    re.compile(r'\'g\'\^\(~[\w\d_\.]+\*~[\w\d_\.]+\*~[\w\d_\.]+\)'),
    re.compile(r'!Submission\(.+\) ▶₁ #t'),
    '!KU( ~chall )',
    re.compile(r'!Submission\(.*senc\(~chall\.?\d*, kdf\(<\$Server\.?\d*,.*\)'),
    '!KU( senc(~chall',
    'splitEqs(10)',
    'Honest',
    re.compile(r'Client_Out\(.+~chall'),
  ], lines)
elif argv[1] == 'SourceSubmission_Secrecy':
  match = matchAgainstList([
    re.compile(r'!Submission\(.+\'g\','),
    re.compile(r'!Submission\(.+\'g\'>'),
    '!KU( ~chall )',
    'splitEqs(4)',
    '!KU( ~j_fetching',
    '!KU( ~j_eapke_sk',
    '!KU( ~j_epke_sk',
    '!KU( ~j_sig_sk',
    '!KU( ~r',
    '!KU( ~x',
    '!KU( ~ltk',
    '!KU( senc(~chall, kdf(<$Server',
    '!Submission',
    '!KU( \'g\'^(~j_fetching_sk*~r*~x) )',
    re.compile(r'!KU\( \'g\'\^\(~x\.\d\*~x\.\d\) \)'),
    re.compile(r'Client_Out\(.+~chall'),
    '!Ltk',
    '!Pk',
    '!KU( sign(<\'ephemeral\'',
    '!KU( sign(<\'long-term\'',
    '!KU( ~msg',
    '!KU( ~sess.1',

    # 'splitEqs',
    # re.compile(r'!KU\( senc.+\) @ #vk\.21'),
    # re.compile(r'!KU\( senc.+\) @ #vk\.\d+'),
    # re.compile(r'Client_In\(.+\) ▶. #vr\.23'),
  ], lines)
elif argv[1] == 'Source_Authentication':
  match = matchAgainstList([
    re.compile(r'!Submission\(.+\'g\','),
    re.compile(r'!Submission\(.+\'g\'>'),
  ], lines)

if match is not None:
  print(match)
