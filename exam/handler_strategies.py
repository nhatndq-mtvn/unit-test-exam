import csv
import time
from abc import ABC, abstractmethod

from exam.api_client import APIClient
from exam.entities import Order
from exam.exceptions import APIException


class OrderHandler(ABC):

    @abstractmethod
    def process(self, order) -> Order:
        pass


class CSVOrderHandler(OrderHandler):

    def process(self, order) -> Order:
        csv_file = f"orders_type_A_{order.user_id}_{int(time.time())}.csv"
        try:
            with open(csv_file, "w", newline="") as file_handle:
                writer = csv.writer(file_handle)
                writer.writerow(["ID", "Type", "Amount", "Flag", "Status", "Priority"])

                writer.writerow(
                    [
                        order.id,
                        order.type,
                        order.amount,
                        str(order.flag).lower(),
                        order.status,
                        order.priority,
                    ]
                )

                if order.amount > 150:
                    writer.writerow(["", "", "", "", "Note", "High value order"])

            order.status = "exported"

        except IOError:
            order.status = "export_failed"

        finally:
            return order


class APIOrderHandler(OrderHandler):

    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def process(self, order) -> Order:
        try:
            api_response = self.api_client.call_api(order.id)

            if api_response.status == "success":
                if api_response.data >= 50 and order.amount < 100:
                    order.status = "processed"
                elif api_response.data < 50 or order.flag:
                    order.status = "pending"
                else:
                    order.status = "error"

            else:
                order.status = "api_error"

        except APIException:
            order.status = "api_failure"

        finally:
            return order


class CheckFlagOrderHandler(OrderHandler):

    def process(self, order) -> Order:
        order.status = "completed" if order.flag else "in_progress"

        return order


class DefaultOrderHandler(OrderHandler):

    def process(self, order) -> Order:
        order.status = "unknown_type"

        return order
