'''
metrics.py

Author Korbinian Randl
'''

def get_false_positives(y_true:list, y_pred:list) -> int:
    '''Returns the number of false positives.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         number of false positives.
    '''
    #TODO change this:
    return 0

def get_true_positives(y_true:list, y_pred:list) -> int:
    '''Returns the number of true positives.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         number of true positives.
    '''
    #TODO change this:
    return 0

def get_false_negatives(y_true:list, y_pred:list) -> int:
    '''Returns the number of false negatives.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         number of false negatives.
    '''
    #TODO change this:
    return 0

def get_true_negatives(y_true:list, y_pred:list) -> int:
    '''Returns the number of true negatives.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         number of true negatives.
    '''
    #TODO change this:
    return 0

def get_accuracy(y_true:list, y_pred:list) -> float:
    '''Returns the accuracy of the predictions.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         accuracy of the predictions.
    '''
    #TODO change this (hint: use the above functions):
    return 0.

def get_f1(y_true:list, y_pred:list) -> float:
    '''Returns the f1 score for the predictions.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.


    returns:         f1-score of the predictions.
    '''
    #TODO change this (hint: use the above functions):
    return 0.

def pretty_print(y_true:list, y_pred:list) -> None:
    '''Prints a confusion matrix in ascii art.

    inputs:
        y_true:      list[bool] of true labels.

        y_pred:      list[bool] of predicted labels.)
    '''
    fp = f'{get_false_positives(y_true, y_pred):4d}'
    fn = f'{get_false_negatives(y_true, y_pred):4d}'
    tp = f'{get_true_positives(y_true, y_pred):4d}'
    tn = f'{get_true_negatives(y_true, y_pred):4d}'

    print( '      |    true    |')
    print( ' pred | TRUE FALSE |')
    print( '------|------------|')
    print(f' TRUE | {tp}  {fp} |')
    print(f'FALSE | {fn}  {tn} |\n')

    print(f'Accuracy: {get_accuracy(y_true, y_pred):.4f}')
    print(f'F1-score: {get_f1(y_true, y_pred):.4f}')