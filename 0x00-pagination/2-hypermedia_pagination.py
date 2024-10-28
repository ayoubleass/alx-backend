#!/usr/bin/env python3
"""
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for any given page.
    """
    return ((page - 1) * page_size, (page - 1) * page_size + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a dataset from csv file.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data = self.dataset()
        if len(data) < start_index:
            return []
        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dataset from csv file.
        """
        res = {}
        start, end = index_range(page, page_size)
        data = self.get_page(page, page_size)
        res['page_size'] = len(data)
        res['page'] = page
        res['data'] = data
        res['next_page'] = page + 1 if end < len(self.__dataset) else None
        res['prev_page'] = page - 1 if start > 0 else None
        res['total_pages'] = math.ceil(len(self.dataset()) / page_size)
        return res
