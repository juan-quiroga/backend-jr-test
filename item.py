import random
from dataclasses import dataclass
from typing import List, Optional

import jsons

from db import DB


@dataclass
class Item(object):
    id: int
    description: str
    available_amount: int


class ItemDAO(object):
    table_name = 'item'

    def __init__(self):
        self.db = DB()

    def create(self, description: str) -> Item:
        #############################
        #### WRITE YOUR CODE HERE ###
        #############################

        #############################
        return Item(item_id, description, 0)

    def list(self, amount=None, order_by=None, order=None) -> List[Item]:
        #############################
        #### WRITE YOUR CODE HERE ###
        #############################

        #############################
        items = jsons.load(records, List[Item])
        return items

    def find_by_id(self, item_id: int, lock=False) -> Optional[Item]:
        #############################
        #### WRITE YOUR CODE HERE ###
        #############################

        #############################

        if not records:
            return None

        item = jsons.load(records[0], Item)
        return item

    def increment(self, item: Item) -> Item:
        #############################
        #### WRITE YOUR CODE HERE ###
        #############################

        #############################
        return item
