from unittest.mock import MagicMock, patch

import pytest

from data_test import data_orders
from exam.api_client import APIClient
from exam.db_services import DatabaseService
from exam.exceptions import APIException, DatabaseException
from exam.response import APIResponse


@pytest.fixture(autouse=True)
def mock_open():
    with patch("builtins.open", MagicMock()) as mock_file:
        yield mock_file


@pytest.fixture(name="api_client")
def mock_api_client():
    api_client = MagicMock(spec=APIClient)

    return api_client


@pytest.fixture
def mock_db_service_return_order_type_A():
    db_service = MagicMock(spec=DatabaseService)
    db_service.get_orders_by_user.return_value = [order for order in data_orders if order.type == "A"]

    return db_service


@pytest.fixture
def mock_db_service_return_order_type_B():
    db_service = MagicMock(spec=DatabaseService)
    db_service.get_orders_by_user.return_value = [order for order in data_orders if order.type == "B"]

    return db_service


@pytest.fixture
def mock_db_service_return_order_type_C():
    db_service = MagicMock(spec=DatabaseService)
    db_service.get_orders_by_user.return_value = [order for order in data_orders if order.type == "C"]

    return db_service


@pytest.fixture
def mock_db_service_return_order_type_other():
    db_service = MagicMock(spec=DatabaseService)
    db_service.get_orders_by_user.return_value = [order for order in data_orders if order.type == "Z"]

    return db_service


@pytest.fixture
def mock_db_service_return_order_large_amount():
    db_service = MagicMock(spec=DatabaseService)
    db_service.get_orders_by_user.return_value = [order for order in data_orders if order.amount > 200]

    return db_service


@pytest.fixture
def mock_db_service_return_empty_order():
    db_service = MagicMock(spec=DatabaseService)
    db_service.get_orders_by_user.return_value = []

    return db_service


@pytest.fixture
def mock_db_service_with_get_order_function_get_error():
    db_service = MagicMock(spec=DatabaseService)
    db_service.get_orders_by_user.side_effect = DatabaseException

    return db_service


@pytest.fixture
def mock_db_service_with_bulk_update_function_get_error():
    db_service = MagicMock(spec=DatabaseService)
    db_service.get_orders_by_user.return_value = [data_orders[0]]
    db_service.bulk_update_order_status.side_effect = DatabaseException

    return db_service


@pytest.fixture
def mock_api_client_return_success_data_50():
    api_client = MagicMock(spec=APIClient)
    api_client.call_api.return_value = APIResponse(status="success", data=50)

    return api_client


@pytest.fixture
def mock_api_client_return_success_data_less_than_50():
    api_client = MagicMock(spec=APIClient)
    api_client.call_api.return_value = APIResponse(status="success", data=49)

    return api_client


@pytest.fixture
def mock_api_client_return_fail():
    api_client = MagicMock(spec=APIClient)
    api_client.call_api.return_value = APIResponse(status="fail", data="")

    return api_client


@pytest.fixture
def mock_api_client_return_error():
    api_client = MagicMock(spec=APIClient)
    api_client.call_api.side_effect = APIException

    return api_client
