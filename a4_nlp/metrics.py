'''
metrics.py

Author Korbinian Randl
'''


def get_false_positives(y_true: list, y_pred: list) -> int:
    '''Returns the number of false positives.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         number of false positives.
    '''
    # TODO change this:

    fp = 0

    for i in range(len(y_true)):
        if y_true[i] == False and y_pred[i] == True:
            fp += 1

    return fp


def get_true_positives(y_true: list, y_pred: list) -> int:
    '''Returns the number of true positives.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         number of true positives.
    '''
    # TODO change this:

    tp = 0

    for i in range(len(y_true)):
        if y_true[i] == True and y_pred[i] == True:
            tp += 1

    return tp


def get_false_negatives(y_true: list, y_pred: list) -> int:
    '''Returns the number of false negatives.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         number of false negatives.
    '''
    # TODO change this:

    fn = 0

    for i in range(len(y_true)):
        if y_true[i] == True and y_pred[i] == False:
            fn += 1

    return fn


def get_true_negatives(y_true: list, y_pred: list) -> int:
    '''Returns the number of true negatives.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         number of true negatives.
    '''
    # TODO change this:

    tn = 0

    for i in range(len(y_true)):
        if y_true[i] == False and y_pred[i] == False:
            tn += 1

    return tn


def get_accuracy(y_true: list, y_pred: list) -> float:
    '''Returns the accuracy of the predictions.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         accuracy of the predictions.
    '''
    # TODO change this (hint: use the above functions):

    tp = get_true_positives(y_true, y_pred)
    tn = get_true_negatives(y_true, y_pred)

    return (tp + tn) / len(y_true)


def get_f1(y_true: list, y_pred: list) -> float:
    '''Returns the f1 score for the predictions.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         f1-score of the predictions.
    '''
    # TODO change this (hint: use the above functions):

    tp = get_true_positives(y_true, y_pred)
    fp = get_false_positives(y_true, y_pred)
    fn = get_false_negatives(y_true, y_pred)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    return 2 * (precision * recall) / (precision + recall)


def pretty_print(y_true: list, y_pred: list) -> None:
    '''Prints a confusion matrix in ascii art.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.)
    '''
    fp = f'{get_false_positives(y_true, y_pred):4d}'
    fn = f'{get_false_negatives(y_true, y_pred):4d}'
    tp = f'{get_true_positives(y_true, y_pred):4d}'
    tn = f'{get_true_negatives(y_true, y_pred):4d}'

    print('      |    true    |')
    print(' pred | TRUE FALSE |')
    print('------|------------|')
    print(f' TRUE | {tp}  {fp} |')
    print(f'FALSE | {fn}  {tn} |\n')

    print(f'Accuracy: {get_accuracy(y_true, y_pred):.4f}')
    print(f'F1-score: {get_f1(y_true, y_pred):.4f}')
