# Formal Analysis of the SecureDrop Protocol

This repository contains the Tamarin models from Luca Maier's thesis "Formal Analysis of the SecureDrop protocol".

There are two separate models: `malicious_user` and `malicious_server`.

The proofs have been constructed using `Tamarin 1.8.0`.

## `malicious_user.spthy`

This model is addresses the weaker adversarial setting: malicious user.

To reconstruct the proofs from `proofs/malicious_user_analyzed.spthy` open the model in the GUI. All lemmas with the name `Auto_` can be automatically proven (there is an oracle `oracles/malicious_user.py`). The other lemmas can be proven by repeatedly pressing `1` in the interactive mode.

## `malicious_server.spthy`

This model addresses the stronger adversarial setting: malicious server.

To reconstruct the proofs from `proofs/malicious_server_analyzed.spthy` open the model in the GUI. All lemmas with the name `Auto_` can be automatically proven (there is an oracle `oracles/malicious_server.py`). The other lemmas can be proven by repeatedly pressing `1` in the interactive mode.