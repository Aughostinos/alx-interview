#!/usr/bin/python3
"""Lockboxes problem"""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened"""
    
    # the first box unlocked
    unlocked = {0}
    # Get keys from the first box
    keys = boxes[0]
    
    for key in keys:
        if key not in unlocked and key < len(boxes):
            # Unlock the box
            unlocked.add(key)
            # Add the keys from this new box to the list
            keys.extend(boxes[key])
    # Check if all boxes are unlocked
    return len(unlocked) == len(boxes)