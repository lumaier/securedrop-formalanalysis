TOOLS_DIR := $(CURDIR)/tools
TAMARIN_RELEASE := $(TOOLS_DIR)/tamarin-prover
N_THREADS ?= 10
PORT ?= 3001

# Tamarin will look for maude and inherit it
export PATH := $(PATH):$(TOOLS_DIR)

# Linux setup (Tested on Ubuntu 24.04)
.PHONY: setup
setup:
	mkdir -p tools
	cd tools && \
		curl -OL https://github.com/tamarin-prover/tamarin-prover/releases/download/1.10.0/tamarin-prover-1.10.0-linux64-ubuntu.tar.gz && \
		tar -xvzf tamarin-prover-1.10.0-linux64-ubuntu.tar.gz && \
		curl -OL https://github.com/maude-lang/Maude/releases/download/Maude3.5/Maude-3.5-linux-x86_64.zip && \
		unzip -o Maude-3.5-linux-x86_64.zip

.PHONY: well-formed
well-formed:
	@$(TAMARIN_RELEASE) --quit-on-warning --derivcheck-timeout=-1 "securedrop.spthy"

.PHONY: interactive
interactive:
	@$(TAMARIN_RELEASE) +RTS -N$(N_THREADS) -RTS interactive --image-format=SVG --derivcheck-timeout=0 --port=$(PORT) "./"

proof/%.spthy: securedrop.spthy oracle.py parts/*.spthy
	mkdir -p proof
	@$(TAMARIN_RELEASE) +RTS -N$(N_THREADS) -RTS --derivcheck-timeout=0 --prove="$**" --output="$@" "securedrop.spthy"

debug/%.spthy: securedrop.spthy oracle.py parts/*.spthy
	mkdir -p debug
	@$(TAMARIN_RELEASE) +RTS -N$(N_THREADS) -RTS --derivcheck-timeout=0 --oracle-only --stop-on-trace=sorry --prove="$**" --output="$@" "securedrop.spthy"
