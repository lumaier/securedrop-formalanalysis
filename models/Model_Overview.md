## v1

### `source_journalist.spthy`

Simple interaction between source and journalist. A source gets the journalist's keys and sends a submission.
Only the intended journalist can view the plaintext of the message.

Message fetching is omitted.

## v2

### `source_journalist_response.spthy`

This model extends `v1/source_journalist.spthy` with a response of the journalist. The response is linked to the previous message. Only the sender of the previous message can read the response.

## v3

### `source_journalist_fetching.spthy`

This model extends `v2/source_journalist_fetching.spthy` with the message fetching process on the journalist's and source's side. Instead of modelling the server, the source and journalist send the fetching messages into the network. Even under these circumstances, there should be traces where the protocol finishes (namely when the adversary imitates the server).

An attack concerning key reusage was found [here](https://github.com/freedomofpress/securedrop-protocol/issues/53).

## v4

### `source_journalist_fetching.spthy`

In this model, I investigated the fact that even by just outputting $mgdh$, Tamarin doesn't find a single trace for the protocol.

It seems that with [this fix](https://github.com/lumaier/securedrop-formalanalysis/commit/febf1527359b9dd42842f48c70e7758dc2cd1521) we can solve the problem: don't output triples (or even tuples?).

The problem wasn't the above: Instead we have to "play god" a bit by checking that $JC_{PK}$ really comes from a journalist. Since we have its signature, this is a valid assumption (and a authentic key - in reality signed by the newsroom and FPF).

We also need to check that $JC_{PK} != JE_{PK}$. Otherwise the source leaks $k = DH(JE_{PK},ME_{SK}) = DH(JC_{PK},ME_{SK}) = mgdh$ if an adversary sends the same key twice. It can then decrypt the message.

## v7

### `source_newsroom.spthy`

This model extends `v2/source_journalist_fetching.spthy`. Now, the source communicates with a newsroom (not a journalist). A valid recipient is any journalist who was verified by the newsroom.

## v8

### `source_journalist_kem.spthy`

This model extends `results/key_type/source_journalist_typed.spthy` by encrypting the message using a KEM instead of DH public key exchange. This makes the scheme more secure (PQ?) and speeds up the Tamarin proving.

### `source_journalist_fetching_kem.spthy`

This model extends `v3/source_journalist_fetching.spthy` by encrypting the message using a KEM instead of DH public key exchange.

### `source_journalist_kem_clean.spthy`

Up to v8, this is the most up-to-date version. This includes dedicated key registration and reveal rules for all the keys (and usage in the security properties).


| Model | Trusted Server | Message Fetching 
| :---------------- | :------: | :------: |
| `v11/s2j_complete_dh_vanilla` |  |  | 
| `v12/s2j_server_dh_vanilla` | &#x2705; | &#x2705; | 
| `v12/s2j_complete_dh_kenny` | | |