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
        return self.__classifier.predict(digit)[0]
