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
    re.compile(r'^\(last'),
    re.compile(r'^(Client|Server)Source'),
    '!Submission',
    'KU( senc',
  ], lines)
elif argv[1] == 'FetchingSharedSecretSecrecySourceSubmission':
  match = matchAgainstList([
    re.compile(r'!Submission\(.+\'g\'(,|>)'),
    re.compile(r'∃.+Reveal'),
    '!KU( ~r',
    '!KU( ~j',
    '!KU( ~x',
    '!KU( ~ltk',
    re.compile(r'!Submission\(.+\) ▶. #t1'),
    '!KU( sign(<\'long-term\', pk(x), j_fetch_pk, j_apke_pk>, ~ltk)',
    '!KU( \'g\'^(~j_fetching_sk*~r*~x) ) @ #t4',
    'splitEqs(4)',
  ], lines)
elif argv[1] == 'FetchingSharedSecretSecrecyJournalistSubmission':
  match = matchAgainstList([
    re.compile(r'∃.+Reveal'),
    '!Ltk_Source',
    'splitEqs(9)',
    'splitEqs(8)',
    '!KU( ~r',
    '!KU( ~s_',
    '!KU( ~x',
    'splitEqs(13)',
    re.compile(r'!Submission\(.+\) ▶. #t1'),
    '!KU( \'g\'^(~r*~s_fetching_sk*~x) ) @ #t5',
  ], lines)
elif argv[1] == 'FetchingChallengeSecrecy':
  match = matchAgainstList([
    '∃',
    'senc(~chall,',
    re.compile(r'Client_Out\(.+~chall'),
    re.compile(r'!Submission.+ ▶. #t1'),
    '!KU( ~chall',
  ], lines)
elif argv[1] == 'SourceSubmission_Secrecy':
  match = matchAgainstList([
    re.compile(r'!Submission\(.+\'g\'(,|>)'),
    'Reveal_Newsroom_Key',
    'Reveal_Journalist_SIG',
    '!Ltk',
    '!Pk',
    '!KU( sign(<\'ephemeral\'',
    '!KU( sign(<\'long-term\'',
    '!Submission',
    '!KU( ~msg',
    '∀',
    re.compile(r'Client_Out\(.+~chall'),
    '∃',
  ], lines)
elif argv[1] == 'JournalistSubmission_Secrecy':
  match = matchAgainstList([
    '!JournalistEnrolled',
    '!!Ltk_Journalist_APKE_Key',
    re.compile(r'!Submission\(.+\'g\'(,|>)'),
    # '!Submission',
    '!KU( ~msg',
    'Fetched( ~id ) @ #x',
    re.compile(r'Client_Out\(.+~chall'),
    '∀',
    '∃',
  ], lines)
elif argv[1] == 'Source_Authentication' or argv[1] == 'Journalist_Authentication':
  match = matchAgainstList([
    re.compile(r'!Submission\(.+\'g\','),
    re.compile(r'!Submission\(.+\'g\'>'),
  ], lines)
elif argv[1] == 'SessionSecrecy':
  match = matchAgainstList([
    re.compile(r'(Source|Journalist)(Queried|Responded)'),
    '!KU( ~sess )',
  ], lines)
elif argv[1] == 'EphemeralDHSecrecy':
  match = matchAgainstList([
    'ClassicSecret',
    '!KU( ~x',
  ], lines)
elif argv[1] == 'SubmissionEquality':
  match = matchAgainstList([
    'Submi',
  ], lines)

if match is not None:
  print(match)
