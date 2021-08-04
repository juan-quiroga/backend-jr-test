from db import DB
from item import ItemDAO, Item


class ItemService(object):
    def __init__(self):
        self.item_dao = ItemDAO()
        self.db = DB()

    def create(self, description) -> Item:
        item = self.item_dao.create(description)
        return item

    def list(self, amount: int = None, order_by: str = None, order: str = None):
        return self.item_dao.list(amount, order_by, order)

    def find_by_id(self, item_id: int) -> Item:
        item = self.item_dao.find_by_id(item_id)
        if item is None:
            raise ItemNotFoundException()

        return item

    def increment(self, item_id) -> Item:
        self.db.start_transaction()

        item = self.item_dao.find_by_id(item_id, lock=True)
        if item is None:
            raise ItemNotFoundException()

        item = self.item_dao.increment(item)

        self.db.commit()
        return item


class ItemNotFoundException(Exception):
    pass
