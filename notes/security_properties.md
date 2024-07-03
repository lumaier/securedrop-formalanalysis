# Github

## Core Properties

- SG1 - No accounts: no user authentication
- SG2 - No message flow metadata: messages can't be linked together, and different types of messages are indistinguishable from one another
- SG3 - No changes in server state are observable externally
- SG4 - No ciphertext collection or information leaks via trial decryption: a given recipient receives pertinent ciphertext only

## Also mentioned

- E2EE of communication
- One-way forward secrecy for messages flowing from source to journalist

# Security Properties (v1)

- Confidentiality: message can be decrypted and read only by its sender and intended recipients, not by any system or entity in between.
    - for the initial message, these are all the journalists
    - for all messages from journalists to source it is only the source
    - for all replies from source to journalists, these are the intended journalists
- Message Integrity: message has not been altered or tampered with during transmission from the sender to the receiver
- Message Origin Authenticity: message genuinely originates from the claimed sender and has not been altered or forged
- (Perfect) Forward Secrecy: security of ephemeral private keys even if the long-term private keys are compromised in the future
- Sender anonimity: identity of the sender is not known
    - In our context, the server can't even distinguish between sources and journalists (unless it is the source's initial message)
    - There is no per-conversation anonimity: the journalist wants to communicate with the same source each time, so it knows that the same source is replying each time
- Source's plausible deniability: allows an individual to deny knowledge of or responsibility for a specific action or piece of information
    - no traces left behind on the source's computer

## (one-way) Forward Secrecy

We only have one-way forward secrecy from the source to the journalists. In an asynchronous protocol, the receiver needs to store state to retrieve the keys for decryption (the sending party can create a key and discard it after sending). Because we don't want the source to store any state, we can't achieve forward secrecy from the journalist to the source.
This directly translates to the protocol that when the source receives a message, DH agreement is done using the public $ME_{PK}$ and its secret long-term key $S_{SK}$. So if $S_{SK}$ is compromised, an adversary can decrypt all messages sent to the source (future and past ones). The same doesn't hold for the compromise of the journalist's long-term keys. It used an ephemeral share $ME_{SK}$ for the key agreement.
On the other hand, the DH agreement for incoming messages at the journalists side uses the public $ME_{PK}$ and the secret, ephemeral $^iJE_{SK}$. So even when the long-term keys of the journalist are leaked, past messages can't be decrypted because all the past ephemeral keys have been discarded. The same holds for the compromise of the source's long-term keys. The source used an ephemeral share $ME_{SK}$ for the key agreement.
Consequently, we have forward-secrecy in the case of a compromise of the journalist's keys. When the source's long-term keys are leaked, an adversary can decrypt all past incoming messages.

## Message Forgery

https://github.com/freedomofpress/securedrop-protocol/issues/30

The server can impersonate the source when it has access to the sources public keys. In the above discussion they assume them to remain secret to the server since they only occur encrypted in the initial message.
Once they are leaked, the protocol goes downwards...