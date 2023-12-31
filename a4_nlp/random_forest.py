'''
random_forest.py

Author Korbinian Randl
'''
from decision_tree import BinaryDecisionTree
import random


class BinaryRandomForest:
    def __init__(self, X: dict, y: list, n_trees: int, bias: float = .5, max_depth: int = float('inf')) -> None:
        '''Creates and trains a binary random forest.

        inputs:
            X:          dictionary str->list[float] of attributes and their values.

            y:          list[bool] of labels.

            n_trees:    number of trees in the forest.

            bias:       decision bias for non-pure leaves.

            max_depth:  max_depth of the tree.
        '''
        self.trees = [BinaryDecisionTree(
            *self.get_sample(X, y), **{'bias': bias, 'max_depth': max_depth}) for _ in range(n_trees)]

    def predict(self, X: dict) -> bool:
        '''Predict the class of the input.

        inputs:
            X:          dictionary str->list[float] of attributes and their values.


        returns:        predicted boolean class
        '''
        predictions = [tree.predict(X) for tree in self.trees]

        majority_pred = None
        majority_count = 0
        curr_count = 0
        for pred in predictions:
            curr_count = predictions.count(pred)
            if curr_count > majority_count:
                majority_count = curr_count
                majority_pred = pred

        return majority_pred

    def get_sample(self, X: dict, y: list) -> dict:
        '''Implements feature bagging for X.

        inputs:
            X:          dictionary str->list[float] of attributes and their values.

            y:          list[bool] of labels.


        returns:        a bootstrap sample of X and y
        '''
        # TODO change this

        sample_size = int(0.35*len(y))  # sample size of 35%

        sampled_indices = random.choices(
            range(len(y)), k=sample_size)

        bootstrapped_X = {}
        bootstrapped_y = []

        for attr in X:
            bootstrapped_X[attr] = []
            for i in sampled_indices:
                bootstrapped_X[attr].append(X[attr][i])

        for i in sampled_indices:
            bootstrapped_y.append(y[i])

        return bootstrapped_X, bootstrapped_y
