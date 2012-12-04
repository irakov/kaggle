#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from os.path import basename
from os.path import join
from numpy import loadtxt, save

def print_usage(script_name):
    print "Usage:"
    print "%s [data_dir]" % (script_name)

def main(argv):
    data_dir = 'data/'
    if len(argv) == 1:
        print 'Default data directory %s is used' % data_dir
    elif len(argv) == 2:
        data_dir = argv[1]
    else:
        print_usage(basename(argv[0]))
        exit(1)

    train_csv = join(data_dir, 'train.csv')
    train_labels_npy = join(data_dir, 'train_labels.npy')
    train_data_npy = join(data_dir, 'train_data.npy')
    test_csv = join(data_dir, 'test.csv')
    test_npy = join(data_dir, 'test.npy')

    train_data = loadtxt(train_csv, dtype='uint8', delimiter=',', skiprows=1)
    save(train_labels_npy, train_data[:,0])
    save(train_data_npy, train_data[:,1:])

    test_data = loadtxt(test_csv, dtype='uint8', delimiter=',', skiprows=1)
    save(test_npy, test_data)
    pass

# ---
if __name__ == "__main__":
    main(argv)
