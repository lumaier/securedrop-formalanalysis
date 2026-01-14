# A Formal Analysis of the SecureDrop Protocol

This repository contains the Tamarin models for the SecureDrop protocol.
The proofs have been constructed using the current Tamarin development version at commit [`df2fd84dbb3b3def8309c2a84c04d653d7c4db77`](https://github.com/tamarin-prover/tamarin-prover/tree/df2fd84dbb3b3def8309c2a84c04d653d7c4db77).
The GUI can be started on your local machine with the command `make interactive` if Tamarin is installed.

## Setup

Our proofs require optimizations to Tamarin that have not been integrated into an official release yet.
Thus, you must compile Tamarin from source to construct or verify proofs.
To do so, follow the instructions here: https://tamarin-prover.com/install.html

First, you must install Tamarin's dependencies, including [maude](https://maude.cs.illinois.edu/get-maude), and have it in PATH.

```sh
curl -OL https://github.com/maude-lang/Maude/releases/download/Maude3.5/Maude-3.5-linux-x86_64.zip
unzip -o Maude-3.5-linux-x86_64.zip
```

You can find further documentation when following the link above.
Second, compile Tamarin from the `develop` branch.
As of writing, that is commit `df2fd84dbb3b3def8309c2a84c04d653d7c4db77`.
You can compile Tamarin by executing the following commands:

```sh
git clone https://github.com/tamarin-prover/tamarin-prover
cd tamarin-prover/
git checkout df2fd84dbb3b3def8309c2a84c04d653d7c4db77
curl -sSL https://get.haskellstack.org/ | sh  # install Haskell stack
make
```

After all that, add the resulting `tamarin-prover` binary to your `PATH`, or provide its path to `make` using the `TAMARIN_RELEASE` environment variable.

## Repository Structure

| File | Description |
|------|-------------|
| `parts/` | Models for cryptographic primitives and the secure channel. |
| `proof/*` | Proofs for each lemma that has a prefix matching the respective file name.
| `oracle.py` | Custom heuristics for proof search. |
| `securedrop.spthy` | Protocol model file. |

## Proof Construction and Verification

To construct proofs, run `make proof/PREFIX.spthy`.
The file will contain proofs for all lemmas that have a prefix `PREFIX`.
You can verify constructed or stored proofs by executing:

```sh
tamarin-prover --derivcheck-timeout=0 proof/FILE
```
