#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from os.path import basename
from numpy import load
from numpy import array
from random import sample
from importlib import import_module
from time import time
#from sklearn.cross_validation import KFold

def print_usage(script_name):
    print "Usage:"
    print "%s module_name train_data.npy train_labels.npy" % (script_name)

def main(argv):
    if len(argv) != 4:
        print_usage(basename(argv[0]))
        exit(1)

    start_time = time()

    module_name = argv[1]
    data = load(argv[2])
    labels = load(argv[3])

    recognizer_module = import_module(module_name)
    
    set_size = len(data)
    percent = 5
    test_set_size = (set_size * percent) / 100

    folds = 5
    test_sets_ind = [ array(sample(range(set_size), test_set_size)) for _ in range(0,folds) ]
    correctness_list = []
    for ts_ind in test_sets_ind:
        train_set_ind = array([ x for x in range(set_size) if x not in ts_ind ])
        train_data = data[train_set_ind]
        train_labels = labels[train_set_ind]
        recognizer = recognizer_module.Recognizer(train_data, train_labels)

        test_data = data[ts_ind]
        test_labels = labels[ts_ind]
        correct = 0
        for example, correct_label in zip(test_data, test_labels):
            predicted_label = recognizer.recognize(example)
            if predicted_label == correct_label:
                correct += 1
            pass
        correctness_list.append(correct)
        
    precision_list = [ float(x)/test_set_size for x in correctness_list ]

    print 'Total time: %ds' % (time() - start_time)
    print 'Folds: %d' % (folds)
    print 'Correctness list: %s' % (str(correctness_list))
    print 'Precisions list: %s' % (str(precision_list))
    avg_precision = float(sum(precision_list)) / len(precision_list)
    print 'Average precision: %f' % (avg_precision)

# ---
if __name__ == "__main__":
    main(argv)
