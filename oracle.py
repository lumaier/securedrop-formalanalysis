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

re_keys = re.compile(r'^!?[\w_]+_Key\(')
re_signed_keys = re.compile(r'!KU\( sign\(<\'[\w-]+\'')
re_illegal_submission = re.compile(r'!Submission\(.+\'g\'(,|>)')

match = None
if argv[1] == 'Auto_SecureChannelSources':
  match = matchAgainstList([
    '~~>',
    re.compile(r'^\(∃'),
    re.compile(r'Client_Out\( ~sess(\.\d*), \$Server(\.\d*), ~id(\.\d*)'),
    re.compile(r'^\(last'),
    re.compile(r'^(Client|Server)Source'),
    '!Submission',
    'KU( senc',
  ], lines)
elif argv[1] == 'Auto_FetchingSharedSecretSecrecySourceSubmission':
  match = matchAgainstList([
    re_illegal_submission,
    re.compile(r'∃.+Reveal'),
    '!KU( ~r',
    '!KU( ~j',
    '!KU( ~x',
    '!KU( ~ltk',
    re.compile(r'!Submission\(.+\) ▶. #t1'),
    '!KU( sign(<\'j-sig-ltk\', j_fetch_pk, j_apke_pk>, ~',
    '!KU( \'g\'^(~j_fetching_sk*~r*~x) ) @ #t4',
    'splitEqs(4)',
  ], lines)
elif argv[1] == 'Auto_FetchingSharedSecretSecrecyJournalistSubmission':
  match = matchAgainstList([
    re_illegal_submission,
    re.compile(r'∃.+Reveal'),
    '!KU( \'g\'^(~r*~s_fetching_sk*~x) ) @ #t5',
    'splitEqs(4)',
  ], lines)
elif argv[1] == 'Auto_FetchingChallengeSecrecy':
  match = matchAgainstList([
    '∃',
    'senc(~chall,',
    re.compile(r'Client_Out\(.+~chall'),
    re.compile(r'!Submission.+ ▶. #t1'),
    '!KU( ~chall',
  ], lines)
elif argv[1] == 'Auto_SourceSubmission_Secrecy':
  match = matchAgainstList([
    re_illegal_submission,
    'Reveal_Newsroom_Key',
    'Reveal_Journalist_SIG_Key',
    '!LongTerm',
    '!Public',
    '!KU( sign(<\'j-sig-eph\'',
    '!KU( sign(<\'j-sig-ltk\'',
    '!KU( sign(<\'nr-sig\'',
    '!Submission',
    '!KU( ~msg',
    '∀',
    re.compile(r'Client_Out\(.+~chall'),
    '∃',
  ], lines)
elif argv[1] == 'JournalistSubmission_Secrecy':
  match = matchAgainstList([
    '!JournalistEnrolled',
    '!LongTerm_Journalist_APKE_Key',
    re_illegal_submission,
    '!KU( ~msg )',
    'Fetched( ~id ) @ #x',
    re.compile(r'Client_Out\(.+~chall \)'),
    re.compile(r'!Submission\( \$Server'),
    '!LongTerm_Source',
    re.compile(r'^\(*∃'),
    re.compile(r'^\(*∀'),
  ], lines)
elif argv[1] == 'Agreement_Source' or argv[1] == 'Agreement_Journalist':
  match = matchAgainstList([
    re_illegal_submission,
    re.compile(r'∃.+Reveal'),
    re_keys,
    'APKE_Enc',
    re_signed_keys,
    re.compile(r'(Source|Journalist)Responded'),
  ], lines)
elif argv[1] == 'Easy_SessionSecrecy':
  match = matchAgainstList([
    re.compile(r'(Source|Journalist)(Queried|Responded)'),
    '!KU( ~sess )',
  ], lines)
elif argv[1] == 'Easy_EphemeralDHSecrecy':
  match = matchAgainstList([
    'ClassicSecret',
    '!KU( ~',
  ], lines)
elif argv[1] == 'Easy_SubmissionEquality':
  match = matchAgainstList([
    'Submi',
  ], lines)

if match is not None:
  print(match)
