#!/usr/bin/python3
"""locked boxes"""


def canUnlockAll(boxes):
    """locked boxes"""
    unlocked = set([0])
    keys = [0]

    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == len(boxes)
