# Actors

## Freedom of the Press Foundation (FPF)

# Threat Model



## Threat Model Summary

mainly from https://github.com/freedomofpress/securedrop-protocol?tab=readme-ov-file (section "Threat model summary")

parts are derived from https://docs.securedrop.org/en/latest/threat_model/threat_model.html

### FPF

- "generally" trusted
- based in the US -> legal concerns
    - TODO: search an example where US jurisdicition "vorladen" someone (see Google case)
- might get compromised technically or legally
- develops and signs all components
- enrolls newsrooms

### Newsroom

- "generally" trusted
- based anywhere (potentially in the US)
- might get compromised technically or legally
- manages a server instance (full control)
- enrolls journalists

### Server

- "generally" untrusted
- compromise requires effort
- there may be backups/snapshots from any given point in time
- RAM may be silently read
- managed and paid for by _Newsroom_ or by a third party on their behalf (not recommended)

### Journalist

- varying number
- "generally" trusted
- can travel
- Physical and endpoint security depends on the workstation and client; out of scope here
- can be compromised
- reads submissions
- replies to submissions
- identity is generally known

### Source

- completely untrusted
- anyone can be a source
- can read _journalist_ replies
- can send messages to _journalists_
- can attach files

### Submission

- always from _source_ to _journalist_
- specific to a single SecureDrop instance
- can be anything
- content is secret
- origin is secret

## Threat Model (1st version)

### Random Person on the Internet

- DoS SecureDrop server
    - out of scope, availability is not a requirement
- submit empty, forged or inaccurate documents
    - out of scope -> legitimacy of documents must be checked by journalists/newsroom
- submit malicious documents (e.g., malware) that will compromise the journalists workstation
    - journalists should use dedicated client provided by the protocol
- retrieve sensitive information from a SecureDrop user's browser session (e.g., source's codename)
- compromise SecureDrop server (e.g., Tor, Apache, TLS implementation)
    - out of scope

### Local Network Attackes

- observe when they are using Tor
- block Tor and prevent from accessing SecureDrop
    - out of scope
- website fingerprinting to deduce that a user is using SecureDrop
    - research suggests that this is very difficult (https://blog.torproject.org/critique-website-traffic-fingerprinting-attacks/)

### Global Adversary

- observe all Internet traffic (-> website fingerprinting)
- link a source to a specific SecureDrop server
- link a source to a specific journalist
- correlate data points during investigation (who has read up on SecureDrop, who has used Tor, etc.)
- forge SSL certificate and spoof organization's HTTPS Landing page

## Threat Model (2nd version)

### Dolev-Yao

- standard attacker in Tamarin
- read, reorder, intercept, replay, and send any message to any participant

### Cloud Attacker

- compromise the server
- get snapshots from any given point in time

### Compromised Journalist

- compromised legally or technically

### Compromised Newsroom

- compromised legally or technically
- can then enroll new journalists

### Compromised FPF

- compromised legally or technically
- can then enroll new newsrooms
- develop and sign malicious components

### Assumptions

- Upon registration of a newsroom, FPF validates the newsroom successfully.
- devices use strong randomness (secure KDF)
- cryptographic primitives like DH and PK-crypto are secure against adversary

## Open Questions

- Threat Model: "generally" trusted

- How secure is the enrollement process? Let's say if "NZZ" (a major newspaper in Switzerland) wants to run a SecureDrop instance. How does the FPF ensure that it indeed is NZZ who will run the instance? (Impersonation of a legitimate newsroom). As a source I believe to communicate with a trustworthy newspaper and in the process of authenticating the documents I need to reveal (parts of) my identity.
    - "a global adversary may be able to forge SSL certificate and spoof organization's HTTPS Landing page" -> is the landing page signed by FPF? security comes from verifying Newsroom keys? (i.e., no communication possible)

- Routing Attacks: when a user accesses xyz.securedrop.tor.onion (from "List of SecureDrops"), can we assume that it will land on the "legitimate" webpage and all the traffic is encrypted and authenticated? (There is a remark "If the .onion address information on Aftenposten AS’s landing page below does not match our records, do not contact this SecureDrop.")

- DoS attacks are out of scope -> availability is not a requirement?
    - no it is not

- journalist can access server from anywhere? (doesn't have to be within _newsroom's_ network)

# Threat Model (3rd version)

- We assume the presence of a Dolev-Yao network adversary, capable of reading, reordering, intercepting, replaying, and sending any message to any participant.
- Exclusively the journalist's enrollment into the newsroom occurs through a secure channel. This is a reasonable assumption, as newsrooms must have such channels for various purposes (e.g., verifying journalists to grant access to internal tools). Moreover, this is a one-time process for each journalist.
- We assume that the FPF enrolls only legitimate newsrooms. By "legitimate," we mean that the SecureDrop landing page is managed by the newsroom itself, and the legitimate entity behind the news organization has authority over which journalists are enrolled.
- The SecureDrop protocol does not rely on any assumptions about the server's environment. It offers strong security guarantees even if a potentially malicious third party, such as a legally compromised cloud hosting service, has full access to the server, including all past snapshots.
- Similar threats arise when a journalist is compromised, either legally or technically. Unlike the server, there are no security guarantees for any future messages sent to this journalist after the compromise.
- The newsroom or the FPF can also be compromised. In such cases, the security guarantees between sources and journalists remain unaffected. However, the issue of the initial message being sent to all journalists within a newsroom is out of scope. A compromised newsroom can enroll a malicious journalist and gain full control over the conversation. Similarly, a compromised FPF can enroll new, malicious newsrooms, preventing sources from avoiding communication with these entities and their journalists. Nevertheless, in both scenarios, the anonymity and plausible deniability of the source must be guaranteed.
- Even if sources are compromised, whether legally or technically, SecureDrop still provides robust security guarantees regarding deniability and repudiation. This includes maintaining the confidentiality of past outgoing messages.
- For the protocol, we assume that no adversary can compromise well-established cryptographic primitives, such as digital signature schemes and (generalized) Diffie-Hellman key agreement, and that a reliable source of randomness is used.
