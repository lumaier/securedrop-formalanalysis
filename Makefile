TAMARIN_RELEASE=tamarin-prover
N_THREADS=10
PORT=3001

well-formed:
	@$(TAMARIN_RELEASE) --quit-on-warning --derivcheck-timeout=-1 "securedrop.spthy"

interactive:
	@$(TAMARIN_RELEASE) +RTS -N$(N_THREADS) -RTS interactive --derivcheck-timeout=0 --port=$(PORT) "./"

prove-auto:
	@$(TAMARIN_RELEASE) +RTS -N$(N_THREADS) -RTS --derivcheck-timeout=0 --prove="Auto_*" "securedrop.spthy"

prove-easy:
	@$(TAMARIN_RELEASE) +RTS -N$(N_THREADS) -RTS --derivcheck-timeout=0 --prove="Easy_*" "securedrop.spthy"
