from typing import List


def max_len(strings: List[str]) -> int:
    length = 0
    for s in strings:
        if len(s) > length:
            length = len(s)
    return length