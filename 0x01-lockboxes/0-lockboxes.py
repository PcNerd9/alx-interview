#!/usr/bin/env python3

"""
contains a function that determins if all he boxes can be opened
"""


def canUnlockAll(boxes):
    """
    return true if all the boxes can be unlocked
    otherwise return false
    """

    queue = [0] + boxes[0]
    i = 0

    while i < len(queue):
        box = boxes[queue[i]]
        for key in box:
            if key not in queue:
                queue.append(key)
        i += 1
    if len(queue) == len(boxes):
        return True
    else:
        return False
