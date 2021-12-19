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
        
        item_id = random.randint(0,1000000000)
        query = ("INSERT INTO item (id, description, available_amount) VALUES (%s,%s,%s)")
        vals = (item_id,description,0)
        cnx = self.db.get_connection()
        cnx.execute(query, vals)
        cnx.commit()
        cnx.close()
                
        return Item(item_id, description, 0)

    def to_list(self, amount=None, order_by=None, order=None) -> List[Item]:
        
        query = ("SELECT * FROM item LIMIT %s ORDER BY %s %s")
        vals = (amount,order_by,order)
        cnx = self.db.get_connection()
        cnx.execute(query,vals)
        records = cnx.fetchall()
        cnx.close()
        items = jsons.load(records, List[Item])

        return items

    def find_by_id(self, item_id: int, lock=False) -> Optional[Item]:
        query = ("SELECT * FROM item WHERE id = %s ")
        val = item_id
        cnx = self.db.get_connection()
        cnx.execute(query,val)
        records = cnx.fetchall()
        cnx.close()
        
        if not records:
            return None

        item = jsons.load(records[0], Item)
        return item

    def increment(self, item: Item) -> Item:
        # the increment is done by 1
        query = ("UPDATE item SET available_amount = available amount + 1 WHERE id = %s")
        val = item.id
        cnx = self.db.get_connection()
        cnx.execute(query,val)
        cnx.commit()
        cnx.close()

        return item
