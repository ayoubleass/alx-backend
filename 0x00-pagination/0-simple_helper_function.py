#!/usr/bin/env python3
"""
This module has a helper  function that  return a tuple of size 2.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for any given page.
    """
    return ((page - 1) * page_size, (page - 1) * page_size + page_size)
