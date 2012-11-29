#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from os.path import basename
from numpy import load
from numpy import array
from random import sample
#from sklearn.cross_validation import KFold

def print_usage(script_name):
    print "Usage:"
    print "%s train_data.npy train_labels.npy" % (script_name)

def main(argv):
    if len(argv) != 3:
        print_usage(basename(argv[0]))
        exit(1)

    train_data = load(argv[1])
    train_labels = load(argv[2])
        
    set_size = len(train_data)
    percent = 5
    test_set_size = (set_size * percent) / 100

    test_set_ind_1 = array(sample(range(set_size), test_set_size))
    test_set_ind_2 = array(sample(range(set_size), test_set_size))

    train_set_ind_1 = array([ x for x in range(set_size) if x not in test_set_ind_1 ])
    train_set_ind_2 = array([ x for x in range(set_size) if x not in test_set_ind_2 ])

    test_sets_ind = [ test_set_ind_1, test_set_ind_2 ]
    correctness_list = []
    for ts_ind in test_sets_ind:
        test_set = train_data[ts_ind]
        test_labels = train_labels[ts_ind]
        for example, correct_label in zip(test_set, test_labels):
            pass

# ---
if __name__ == "__main__":
    main(argv)
