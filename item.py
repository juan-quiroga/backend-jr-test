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
        # Write code

        # Fix next line
        item_id = random.randint(0, 1000000)
        return Item(item_id, description, 0)

    def list(self, amount=None, order_by=None, order=None) -> List[Item]:
        # Write code

        # Fix next line
        records = []

        items = jsons.load(records, List[Item])
        return items

    def find_by_id(self, item_id: int, lock=False) -> Optional[Item]:
        # Write code

        # Fix next line
        records = []

        if not records:
            return None

        item = jsons.load(records[0], Item)
        return item

    def increment(self, item: Item) -> Item:
        # Write code

        return item
