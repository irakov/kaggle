#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from numpy import load
from numpy import save
from os.path import basename
from sklearn.decomposition import ProbabilisticPCA
from time import time

def print_usage(script_name):
    print "Usage:"
    print "%s n_components input_train_data.npy input_test_data.npy output_train_data.npy output_test_data.npy" % (script_name)

def main():
    if len(argv) != 6:
        print_usage(basename(argv[0]))
        exit(1)

    print_log = True

    n_components = int(argv[1])
    input_train_data = load(argv[2])
    input_test_data = load(argv[3])
    output_train_data_file = argv[4]
    output_test_data_file = argv[5]

    t = time()
    pca = ProbabilisticPCA(n_components=n_components)
    output_train_data = pca.fit_transform(input_train_data)
    t = time()-t
    if print_log:
        print 'PCA fitting to {0} with {1} components to save (with transformation): {2[0]:d}m {2[1]:02d}s'.format(input_train_data.shape, n_components, (int(t//60), int(t%60)) )
        print 'New shape: {}'.format(output_train_data.shape)

    t = time()
    output_test_data = pca.transform (input_test_data)
    t = time()-t
    if print_log:
        print 'PCA transformation of {0} with {1} components to save: {2[0]:d}m {2[1]:02d}s'.format(input_test_data.shape, n_components, (int(t//60), int(t%60)) )
        print 'New shape: {}'.format(output_test_data.shape)

    save(output_train_data_file, output_train_data)
    save(output_test_data_file, output_test_data)

# ---
if __name__ == "__main__":
    main()
