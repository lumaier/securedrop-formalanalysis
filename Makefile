TAMARIN_RELEASE=tamarin-prover
N_THREADS=10
PORT=1611 # used port for port-forwarding the GUI
DIR="v1/"
USER:=$(shell whoami)

# run models on the tamarin-server with:
run:
	@$(TAMARIN_RELEASE) +RTS -N$(N_THREADS) -RTS interactive "models/" --port=$(PORT)

# run models on local machine with:
run_local:
	@tamarin-prover +RTS -N$(N_THREADS) -RTS interactive "models/"

# cleans up the graph images from interactive mode
# (necessary to prevent disk space issues)
clean:
	@rm /tmp/tamarin-prover-cache-$(USER)/img/*
