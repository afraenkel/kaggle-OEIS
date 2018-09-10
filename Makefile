

data/raw/sequences:
	mkdir -p data/raw
	curl --output $@.gz https://oeis.org/stripped.gz
	gunzip $@.gz

data/interim/training.csv: data/raw/sequence
	mkdir -p data/interim
