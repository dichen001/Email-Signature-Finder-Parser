import csv
import logging
import random
import itertools
import bisect

class RandomizedData:
    def __init__(self,csv_file_name):
        self._data = csv_to_dict_list(csv_file_name)
        self._cumdist = _build_cumulative_probability(self._data)

    def random(self,x=None):
        if x is None:
            x = random.random()
        y = self._data[bisect.bisect(self._cumdist, x)]
        return y
        
    
def _build_cumulative_probability(seq):
    '''Build the cumulative probability table'''
    x0 = seq[0]
    if 'Frequency' in x0:
        accum0 = itertools.accumulate([ float(x['Frequency']) for x in seq ])
    else:
        accum0 = itertools.accumulate([ 0.01 for x in seq ])
    accum = [ a for a in accum0 ]
    max_freq = accum[-1]
    return [ round(a/max_freq,6) for a in accum ]


def csv_to_dict_list(csv_file_name):
    '''Return a list of dictionaries. Each CSV row is a dictionary.'''
    try:
        results = []
        with open(csv_file_name,'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                results.append( row)
    except IOException:
        logging.warn("Could not read CSV file", exc_info=True)
    return results

