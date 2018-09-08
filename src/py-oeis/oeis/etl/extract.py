#!/usr/bin/env python

import os
import pandas as pd

from oeis.etl.features import feature_list

basedir = os.path.dirname(__file__)
DATA = os.path.join(basedir, '..', '..', '..', '..', 'data', 'raw', 'sequences')

def load_sequences():
    seqs = {}
    with open(DATA) as f:
        for seq in f:
            if seq[0] != '#':
                seq_id, seq_array = seq.split()
                seq_array = [int(x) for x in seq_array.split(',') if x]

                if seq_array:
                    seqs[seq_id] = seq_array
    return seqs


def load_features():
    feats = {}
    with open(DATA) as f:
        for seq in f:
            if seq[0] != '#':
                seq_id, seq_array = seq.split()
                seq_array = [int(x) for x in seq_array.split(',') if x]

                if seq_array:
                    feats[seq_id] = {f.__name__: f(seq_array) for f in feature_list}

    return pd.DataFrame(feats).T
