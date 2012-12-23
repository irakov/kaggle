#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Recognizer:
    def __init__(self, train_data, train_labels):
        from sklearn.neighbors import KNeighborsClassifier
#        self.__train_data = train_data
#        self.__train_labels = train_labels
        self.__classifier = KNeighborsClassifier(n_neighbors=1, weights='uniform', algorithm='auto', p=1)
        self.__classifier.fit(train_data, train_labels)

    def recognize(self, digit):
        return int(self.__classifier.predict(digit)[0])

def __main():
    def print_usage(script_name):
        print "Usage:"
        print "%s train_data.npy train_labels.npy test_data.npy output_file" % (script_name)

    from sys import argv
    from numpy import load
    from os.path import basename

    if len(argv) != 5:
        print_usage(basename(argv[0]))
        exit(1)

    train_data = load(argv[1])
    train_labels = load(argv[2])
    test_data = load(argv[3])
    output_file = argv[4]

    recognizer = Recognizer(train_data, train_labels)

    results = []
    total_examples = len(test_data)
    for i, test_example in enumerate(test_data):
        predicted = recognizer.recognize(test_example)
        print 'Example %d/%d\tpredicted %d' % (i, total_examples, predicted)
        results.append(predicted)

    with open(output_file, 'w') as f:
        for r in results:
            f.write(str(r) + '\n')

# ---
if __name__ == "__main__":
    __main()
