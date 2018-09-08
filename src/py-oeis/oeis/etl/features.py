#!/usr/bin/env python

import numpy as np
from math import log10


# utilities

def diffs(L):
    return [y-x for (x,y) in zip(L, L[1:])]

def pct_divN(n):
    def closure(seq):
        return np.mean([(x % n) == 0 for x in seq])
    
    return closure

# features

def monotonic_inc(seq):
    '''Proportion of the sequence that is weakly monotonically increasing.'''
    return np.mean([x >= 0 for x in diffs(seq)]) if len(seq) > 1 else np.NaN

def concave_up(seq):
    '''Proportion of the sequence whose differences of differences are increasing.'''
    return np.mean([x >= 0 for x in diffs(diffs(seq))]) if len(seq) > 2 else np.NaN

def nonneg(seq):
    '''Proportion of the sequence that is non-negative.'''
    return np.mean(list(x >= 0 for x in seq))

def uniq(seq):
    '''Number of unique values in the sequence.'''
    return len(set(seq))

def length(seq):
    '''Length of the sequence.'''
    return len(seq)

def logmax(seq):
    '''Log of the largest magnitude of all the values in the sequence (plus one).'''
    return log10(np.abs(seq).max() + 1.0)

def pct_div2(seq):
    '''Proportion of the sequence that is divisible by 2 (i.e. even).'''
    return pct_divN(2)(seq)

def pct_div3(seq):
    '''Proportion of the sequence that is divisible by 3.'''
    return pct_divN(3)(seq)


feature_list = [monotonic_inc, concave_up, nonneg, uniq, length, logmax, pct_div2, pct_div3]
