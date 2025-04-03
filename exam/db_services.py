from abc import ABC, abstractmethod
from typing import List

from exam.entities import Order


class DatabaseService(ABC):
    @abstractmethod
    def get_orders_by_user(self, user_id: int) -> List[Order]:
        pass

    @abstractmethod
    def bulk_update_order_status(self, orders: List[Order], fields: List[str]) -> None:
        pass
