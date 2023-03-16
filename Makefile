install:
	mamba install --file $(shell pwd)/requirements.txt

list:
	mamba list --export > $(shell pwd)/requirements.txt