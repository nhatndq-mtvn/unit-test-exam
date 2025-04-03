from typing import Dict

from exam.api_client import APIClient
from exam.db_services import DatabaseService
from exam.handler_strategies import (APIOrderHandler, CheckFlagOrderHandler,
                                CSVOrderHandler, DefaultOrderHandler,
                                OrderHandler)


class OrderProcessingService:
    def __init__(self, db_service: DatabaseService, api_client: APIClient):
        self.db_service = db_service
        self.handlers: Dict[str, OrderHandler] = {
            "A": CSVOrderHandler(),
            "B": APIOrderHandler(api_client),
            "C": CheckFlagOrderHandler(),
        }

    def process_orders(self, user_id: int) -> bool:
        try:
            orders = self.db_service.get_orders_by_user(user_id)

            if not orders:
                return False

            new_orders = []

            for order in orders:
                handler = self.handlers.get(order.type, DefaultOrderHandler())
                order = handler.process(order)

                if order.amount > 200:
                    order.priority = "high"
                else:
                    order.priority = "low"

                # Comment out the following lines because updating the status after a DatabaseException is meaningless.
                # Remove update_order_status and using bulk_update_order_status to improve code
                # try:
                #     self.db_service.update_order_status(order.id, order.status, order.priority)
                # except DatabaseException:
                #     order.status = "db_error"

                new_orders.append(order)

            self.db_service.bulk_update_order_status(new_orders, ["status", "priority"])

            return True
        except Exception:
            return False
