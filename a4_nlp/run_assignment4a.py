'''
run_assignment4a.py

Author Korbinian Randl
'''

from decision_tree import BinaryDecisionTree
from random_forest import BinaryRandomForest
import metrics
import json

####################################################################################################
# Functions:                                                                                       #
####################################################################################################


def print_data(X: dict, y: list, n: int = 10, column_width: int = 9) -> None:
    '''Prints a sample of the data.

    inputs:
        X:              dictionary str->list[float] of attributes and their values.

        y:              list[bool] of labels.

        n:              number of rows.

        column_width:   width of the printed columns.
    '''
    # get feature names:
    rows = [[' '*column_width]*len(X) for _ in range(3)]
    for j, column in enumerate(X):
        for i, s in enumerate(column.split()):
            rows[i][j] = s + ' '*(column_width-len(s))

    # add label:
    rows[0].append('good   ')
    rows[1].append('quality')
    rows[2].append('wine   ')

    # print header:
    for row in rows:
        print('|'.join(row))

    # print divider:
    print('|'.join([('-'*column_width)]*len(rows[0])))

    # print data:
    for i in range(n):
        row = []
        for column in X:
            s = f'{X[column][i]:.2f}'
            row.append(' '*(column_width-len(s)) + s)
        row.append(f'{str(y[i])}')
        print('|'.join(row))

    print()

####################################################################################################
# Load Data:                                                                                       #
####################################################################################################


with open('wines.json', 'r') as file:
    X = json.load(file)
y = X.pop('class')
ratio = int(len(y) * 0.75)


def test_train_split(X, y):
    X_train = {}
    X_test = {}
    for attr in X:
        X_train[attr] = X[attr][:ratio]
        X_test[attr] = X[attr][ratio:]

    y_train = y[:ratio]
    y_test = y[ratio:]
    return (X_test, y_test, X_train, y_train)


X_test, y_test, X_train, y_train = test_train_split(X, y)

####################################################################################################
# Main Function:                                                                                   #
####################################################################################################

if __name__ == '__main__':
    # print a sample of the data:
    print('Winequality Dataset By P. Cortez et al 2009 (doi:10.24432/C56S3T):')
    print('[Published under CC BY 4.0]')
    print_data(X_train, y_train)

    # train a decision tree classifier and predict the test set:
    print('Training Decision Tree ...')
    tree = BinaryDecisionTree(X_train, y_train, bias=.5, max_depth=2)
    predictions_tree = tree.predict(X_test)
    print('Done.\n')

    # print decision tree:
    print('Final Decision Tree:')
    tree.pretty_print()
    print()

    # print confusion matrix:
    print('Performance Decision Tree:')
    metrics.pretty_print(y_test, predictions_tree)

    # train a random forrest classifier and predict the test set:
    print('\nTraining Random Forest ...')
    forest = BinaryRandomForest(
        X_train, y_train, n_trees=20, bias=.5, max_depth=2)
    predictions_forest = forest.predict(X_test)
    print('Done.\n')

    # print confusion matrix:
    print('Performance Random Forest:')
    metrics.pretty_print(y_test, predictions_forest)
