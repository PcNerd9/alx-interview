#!/usr/bin/python3

"""
contains a function that determins if all he boxes can be opened
"""


def canUnlockAll(boxes):
    """
    return true if all the boxes can be unlocked
    otherwise return false
    """
    if len(boxes) == 1:
        return True

    # filter the keys in the box that it only contain
    # only the keys for the boxes
    filter_box = [key for key in boxes[0] if key < len(boxes)]

    # make sure that the keys are unique
    unique_filter_key = [0]
    for key in filter_box:
        if key not in unique_filter_key:
            unique_filter_key.append(key)
    queue = unique_filter_key
    i = 1

    # create a queue of keys
    while i < len(queue):
        if queue[i] < len(boxes):
            box = boxes[queue[i]]
            for key in box:
                if key not in queue and key < len(boxes):
                    queue.append(key)
        i += 1

    # check if the lenght of queue is equal to the length
    # of the boxes
    if len(queue) == len(boxes):
        return True
    else:
        return False
