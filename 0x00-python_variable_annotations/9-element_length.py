#!/usr/bin/env python3
"""Type-annotated function element_length that takes a list lst"""


from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return list of tuples, each tuple is an element and its length."""
    return [(i, len(i)) for i in lst]
