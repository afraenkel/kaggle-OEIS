

data/raw/sequences:
	mkdir -p data/raw
	curl --output $@.gz https://oeis.org/stripped.gz
	gunzip $@.gz
