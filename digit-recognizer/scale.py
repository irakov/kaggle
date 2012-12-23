#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import basename
from sys import argv
from numpy import load
from numpy import save
#from sklearn import preprocessing
from time import time

def print_usage(script_name):
    print "Usage:"
    print "%s input_train_data.npy input_test_data.npy output_train_data.npy output_test_data.npy" % (script_name)

def main():
    if len(argv) != 5:
        print_usage(basename(argv[0]))
        exit(1)

    print_log = True

    train_data = load(argv[1]).astype('float')
    test_data = load(argv[2]).astype('float')
    output_train_data_file = argv[3]
    output_test_data_file = argv[4]

    def transf (vec, min_v, max_v):
        d = max_v - min_v
        d2 = d/2
        for i in range(len(vec)):
            if d2 != 0:
                vec[i] = (vec[i] - min_v)/d2 - 1
            else:
                vec[i] = vec[i] - 1

    for i in range(train_data.shape[1]):
        min_v = min(train_data[:,i])
        max_v = max(train_data[:,i])
        transf(train_data[:,i], min_v, max_v)
        transf(test_data[:,i], min_v, max_v)

    save(output_train_data_file, train_data)
    save(output_test_data_file, test_data)

# ---
if __name__ == "__main__":
    main()
