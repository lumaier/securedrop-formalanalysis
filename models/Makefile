TAMARIN_RELEASE=tamarin-prover
N_THREADS=10
PORT=1611 # used port for port-forwarding the GUI
DIR="v1/"
USER:=$(shell whoami)

# run for different model on the tamarin-server with:
# make run DIR="path/to/model/"
run:
	@$(TAMARIN_RELEASE) +RTS -N$(N_THREADS) -RTS interactive "$(DIR)" --port=$(PORT)

# proves all lemmas with "Auto" prefix and stores theory in DIR/theories
# make download DIR="path/to/model" FILE="theory.spthy"
download:
	@if [ ! -d "./$(DIR)/theories" ]; then \
		mkdir "./$(DIR)/theories"; \
	fi
	@$(TAMARIN_RELEASE) +RTS -N$(N_THREADS) -RTS --Output="./$(DIR)/theories" --prove=Auto* "$(DIR)/$(FILE)"

# run for different model on local machine with:
# make run DIR="path/to/model/"
run_local:
	@tamarin-prover +RTS -N$(N_THREADS) -RTS interactive "$(DIR)"

# proves all lemmas with "Auto" prefix and stores theory in DIR/theories
# make download_local DIR="path/to/model" FILE="theory.spthy"
download_local:
	@if [ ! -d "./$(DIR)/theories" ]; then \
		mkdir "./$(DIR)/theories"; \
	fi
	@tamarin-prover +RTS -N$(N_THREADS) -RTS --Output="./$(DIR)/theories" --prove "$(DIR)/$(FILE)"

# cleans up the graph images from interactive mode
# (necessary to prevent disk space issues)
clean:
	@rm /tmp/tamarin-prover-cache-$(USER)/img/*
