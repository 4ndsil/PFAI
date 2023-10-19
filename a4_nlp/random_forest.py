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

        return random.choice(predictions)

    def get_sample(self, X: dict, y: list) -> dict:
        '''Implements feature bagging for X.

        inputs:
            X:          dictionary str->list[float] of attributes and their values.

            y:          list[bool] of labels.


        returns:        a bootstrap sample of X and y
        '''
        # TODO change this

        selected_sample_size = int(0.7 * len(X))

        selected_sample = random.sample(X, selected_sample_size)

        bootstrap_sample_X = {}
        bootstrap_sample_y = []

        for attr, idx in selected_sample:
            bootstrap_sample_X[attr].append(selected_sample[attr][idx])
            bootstrap_sample_y = y[idx]

        return bootstrap_sample_X, bootstrap_sample_y
