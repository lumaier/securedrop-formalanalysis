# A Formal Analysis of the SecureDrop Protocol

This repository contains the Tamarin models from Luca Maier's master's thesis "A Formal Analysis of the SecureDrop protocol".

There are two separate models in `./models/`: `malicious_user` and `malicious_server`.

The proofs have been constructed using `Tamarin 1.8.0`. The GUI can be started on your local machine with the command `make run_local` if Tamarin is installed.

## `malicious_user.spthy`

This model is addresses the weaker adversarial setting: malicious user.

To reconstruct the proofs from `models/proofs/malicious_user_analyzed.spthy` open the model in the GUI. All lemmas can be automatically proven by pressing `a` (there is an oracle `models/oracles/malicious_user.py`).

## `malicious_server.spthy`

This model addresses the stronger adversarial setting: malicious server.

To reconstruct the proofs from `models/proofs/malicious_server_analyzed.spthy` open the model in the GUI. All lemmas with the name `Auto_` can be automatically  proven by pressing `a` (there is an oracle `models/oracles/malicious_user.py`). The other lemmas can be proven by repeatedly pressing `1` in the interactive mode.
