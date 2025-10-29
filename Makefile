TAMARIN_RELEASE=tamarin-prover
N_THREADS=10
PORT=3001
LEMMAS="Auto_*"

well-formed:
	@$(TAMARIN_RELEASE) --quit-on-warning --derivcheck-timeout=-1 "securedrop.spthy"

interactive:
	@$(TAMARIN_RELEASE) +RTS -N$(N_THREADS) -RTS interactive --image-format=SVG --derivcheck-timeout=0 --port=$(PORT) "./"

prove:
	@$(TAMARIN_RELEASE) +RTS -N$(N_THREADS) -RTS --derivcheck-timeout=0 --prove=$(LEMMAS) "securedrop.spthy"
