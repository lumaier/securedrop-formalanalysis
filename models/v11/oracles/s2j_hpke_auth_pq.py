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
    '!Ltk_Source_Passphrase( $S, ~passphrase )',
    '!Pk_Newsroom( $NR, pk(x)',
    '!KU( ~passphrase )',
    '!KU( ~je_dh_sk )',
    '!KU( ~me_sk )',
    '!KU( ~j_sig_sk )',
    '!KU( ~k_pq )',
    '!KU( ~je_kem_sk )',
    '!KU( ~ltk )',
    '!KU( ~msg )',
    '!KU( kdf(<\'DH\', ~passphrase>) )',
    '!KU( kdf(<z, z.1, \'g\'^~me_sk, je_dh_pk,           \'g\'^kdf(<\'DH\', ~passphrase>)>))',
    '((∀ #x.2. (Reveal_Journalist_EDH_Key( je_dh_pk ) @ #x.2) ⇒ ⊥)',
    '!KU( aenc(<\'cipher_s2j\',',
    '!KU( kdf(~ss) )',
    '!KU( \'g\'^(~je_dh_sk*~me_sk) )',
    '!KU( je_dh_pk^~me_sk )',
    '!KU( sign(<\'ephemeral',
    '!KU( kdf(<\'g\'^(~je_dh_sk*kdf(<\'DH\', ~passphrase>)),',
    '(∀ #x. (Reveal_Journalist_EDH_Key( \'g\'^~je_dh_sk ) @ #x) ⇒ ⊥)',
    '!KU( sign(<\'signature',
    '!KU( ~'
  ], lines)
elif argv[1] in ['Auto_Injective_Agreement_Source_Message']:
  match = matchAgainstList([
    '!KU( ~passphrase )',
    '!KU( ~je_dh_sk )',
    '!KU( ~me_sk )',
    '!KU( ~j_sig_sk )',
    '!KU( kdf(<\'DH\', ~passphrase>) )',
    re.compile(r'!KU\( aenc\(<\'cipher_s2j\',\s*\'g\'\^\(\~je_dh_sk'),
    re.compile(r'!KU\( aenc\(<\'cipher_s2j\',\s*\'g\'\^\(\~me_sk'),
    re.compile(r'!KU\( aenc\(<\'cipher_s2j\',\s*\'g\'\^\~me_sk'),
    re.compile(r'!KU\( aenc\(<\'cipher_s2j\',\s*\'g\'\^x'),
    re.compile(r'!KU\( aenc\(<\'cipher_s2j\',\s*\'g\'\^\(x'),
    '!KU( \'g\'^(~je_dh_sk*kdf(<\'DH\', ~passphrase>)) )',
    '!KU( sign(<\'ephemeral\', \'g\'^~je_dh_sk, pk(x.1), pqpk(~je_kem_sk)>, ',
    'Journalist_Ephemeral_Key( ',
    '!Ltk_Journalist_SIG_Key( $J.1, ~j_sig_sk )',
    '!Ltk_Journalist_SIG_Key',
    '!Journalist_Enrolled',
    '!KU( senc(<\'msg_s2j\', ~msg,',
    '(#x2',
    '!KU( H(kdf(<\'g\'^(~je_dh_sk.1*kdf(<\'DH\', ~passphrase>))',
    '!KU( H(kdf(<\'g\'^(~je_dh_sk*kdf(<\'DH\', ~passphrase>)),             \'g\'^(~je_dh_sk*~x), \'g\'^~x, je_dh_pk, \'g\'^kdf(<\'DH\', ~passphrase>)           >),       \'g\'^~x, z, c_pq)) @ #vk.13',
    '!KU( kdf(<\'g\'^(~je_dh_sk*kdf(<\'DH\', ~passphrase>)),           \'g\'^(~je_dh_sk*~x), \'g\'^~x, je_dh_pk, \'g\'^kdf(<\'DH\', ~passphrase>)         >)) @ #vk.24',
    '!KU( ~msg )',
    '!KU( kdf(<\'g\'^(~je_dh_sk*kdf(<\'DH\', ~passphrase>)),',
    '!KU( kdf(<\'g\'^(~je_dh_sk.1*kdf(<\'DH\', ~passphrase>)),',
    'splitEqs(3)',
    '!KU( aenc',
    '!KU( \'g\'^~x'
  ], lines)
elif argv[1] in ['Auto_Secrecy_Journalist_Message']:
  match = matchAgainstList([
    'Journalist_',
    'Ltk_',
    '!KU( ~passphrase )',
    '!KU( ~me_sk',
    '!KU( ~j_dh_sk )',
    '!KU( ~k_pq.1 )',
    '!KU( kdf(<\'DH\', ~passphrase>) )',
    re.compile(r'!KU\( aenc\(<\'cipher_j2s\',\s*\'g\'\^\(\~je_dh_sk'),
    re.compile(r'!KU\( aenc\(<\'cipher_j2s\',\s*\'g\'\^\(\~me_sk'),
    re.compile(r'!KU\( aenc\(<\'cipher_j2s\',\s*\'g\'\^\~me_sk'),
    re.compile(r'!KU\( aenc\(<\'cipher_j2s\',\s*\'g\'\^x'),
    re.compile(r'!KU\( aenc\(<\'cipher_j2s\',\s*\'g\'\^\(x'),
    '!Pk_Newsroom',
    re.compile(r'!KU\( kdf\(<\s*\'g\'\^\(~j_dh_sk'),
    re.compile(r'!KU\( kdf\(<\s*\'g\'\^\(inv'),
    re.compile(r'!KU\( kdf\(<\s*\'g\'\^\(~me_sk'),
    '!KU( \'g\'^(~me_sk.1*kdf(<\'DH\', ~passphrase>)) )',
    '!Ltk_Source_Passphrase',
    '!KU( ~msg.1 )',
    '!KU( kdf(<\'g\'^(~j_dh_sk*kdf(<\'DH\', ~passphrase>)),           \'g\'^(~me_sk*kdf(<\'DH\', ~passphrase>)),',
    '(∀ #x.   (Reveal_Source_KEM_Key( pqpk',
    '!KU( kdf(<\'KEM\', ~passphrase>) )',
    '(∀ #x.   (Reveal_Source_DH_Key(',
    '!KU( kdf(<\'PKE\', ~passphrase>) )',
    '!KU( \'g\'^(~j_dh_sk*kdf(<\'DH\', ~passphrase>)) )',
    '!KU( kdf(<\'g\'^(~j_dh_sk*kdf(<\'DH\', ~passphrase>)),           \'g\'^(~me_sk.1*kdf(<\'DH\', ~passphrase>)),',
    re.compile(r'!KU\( kdf\(<\s*\'g\'\^\(x'),
    '!KU( encap(~k_pq.1, pqpk(kdf(<\'KEM\', ~passphrase>))) )',
  ], lines)
elif argv[1] in ['Auto_Non_Injective_Agreement_Journalist_Message']:
  match = matchAgainstList([
    '!KU( ~passphrase )',
    '!KU( ~ltk',
    '!KU( sign(<\'signature\', pk(~j_sig_sk), \'g\'^~x>, ~ltk.1) )',
    '!KU( ~x',
    '!KU( ~j_dh_sk',
    '!KU( kdf(<\'DH\', ~passphrase>) )',
    '!KU( \'g\'^(~je_dh_sk*kdf(<\'DH\', ~passphrase>)) ) @ #vk.41',
    '!KU( \'g\'^(~je_dh_sk*kdf(<\'DH\', ~passphrase>)) ) @ #vk.38',
    '!KU( \'g\'^(~j_dh_sk*kdf(<\'DH\', ~passphrase>))',
    '!KU( kdf(<\'g\'^(~j_dh_sk*kdf(<\'DH\', ~passphrase>))',
    re.compile(r'!KU\( aenc\(<\'cipher_j2s\',\s*\'g\'\^\(\~je_dh_sk'),
    re.compile(r'!KU\( aenc\(<\'cipher_j2s\',\s*\'g\'\^\(\~x'),
    re.compile(r'!KU\( aenc\(<\'cipher_j2s\',\s*\'g\'\^\~x'),
    re.compile(r'!KU\( aenc\(<\'cipher_j2s\',\s*\'g\'\^x'),
    re.compile(r'!KU\( aenc\(<\'cipher_j2s\',\s*\'g\'\^\(x'),
    '!Pk_Newsroom',
    '!Ltk_Source_Passphrase',
    '!KU( H(kdf(<\'g\'^(~x*kdf(<\'DH\', ~passphrase>)),',
    '!KU( H(kdf(<\'g\'^(~je_dh_sk*kdf(<\'DH\', ~passphrase>)),',
    '!KU( sign(<\'signature\', j_sig_pk, \'g\'^~x>, ~ltk) )',
    '!KU( kdf(<\'g\'^(~x*kdf(<\'DH\', ~passphrase>)),',
    '!KU( kdf(<\'g\'^(~je_dh_sk*kdf(<\'DH\', ~passphrase>)),',
    '!KU( senc(<\'msg_j2s\', ~msg, ',
    '!KU( \'g\'^(~x*kdf(<\'DH\', ~passphrase>)) )',
    '!KU( kdf(<\'g\'^(~j_dh_sk*~j_dh_sk.1',
    '!KU( kdf(<\'g\'^(~j_dh_sk.1',
    re.compile(r'!KU\( kdf\(<\s*\'g\'\^\(~j_dh_sk\*~j_dh_sk\.1'),
    re.compile(r'!KU\( kdf\(<\s*\'g\'\^\(~j_dh_sk\*x'),
    re.compile(r'!KU\( kdf\(<\s*\'g\'\^\(~j_dh_sk\*inv'),
    re.compile(r'!KU\( kdf\(<\s*\'g\'\^\(inv'),
    re.compile(r'!KU\( kdf\(<\s*\'g\'\^\(x'),
    re.compile(r'!KU\( kdf\(<\s*\'g\'\^\(~j_dh_sk\.1'),
    re.compile(r'!KU\( kdf\(<\s*\'g\'\^kdf'),
    '!KU( sign(',
    '!KU( H(kdf',
    '!KU( kdf',
    '!KU( aenc',
  ], lines)
if match is not None:
  print(match)