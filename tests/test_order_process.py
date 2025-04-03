from unittest.mock import MagicMock, patch

from data_test import data_orders
from exam.handler_strategies import APIOrderHandler, CheckFlagOrderHandler, CSVOrderHandler, DefaultOrderHandler
from exam.services import OrderProcessingService


def test_should_return_true_and_write_csv_when_processing_order_type_A(mock_db_service_return_order_type_A, api_client):
    with patch("csv.writer") as mock_csv_writer:
        order_process = OrderProcessingService(mock_db_service_return_order_type_A, api_client)
        result = order_process.process_orders(1)

        assert mock_csv_writer.call_count == 2

        mock_db_service_return_order_type_A.bulk_update_order_status.assert_called_once()

        assert result is True


def test_should_return_true_and_not_call_api_when_processing_order_type_A(
    mock_db_service_return_order_type_A, api_client
):
    order_process = OrderProcessingService(mock_db_service_return_order_type_A, api_client)
    result = order_process.process_orders(1)

    api_client.call_api.assert_not_called()

    mock_db_service_return_order_type_A.bulk_update_order_status.assert_called_once()

    assert result is True


def test_should_return_true_and_not_write_csv_when_processing_order_type_B(
    mock_db_service_return_order_type_B, api_client
):
    with patch("csv.writer") as mock_csv_writer:
        order_process = OrderProcessingService(mock_db_service_return_order_type_B, api_client)
        result = order_process.process_orders(1)

        mock_csv_writer.assert_not_called()

        mock_db_service_return_order_type_B.bulk_update_order_status.assert_called_once()

        assert result is True


def test_should_return_true_and_call_api_when_processing_order_type_B(mock_db_service_return_order_type_B, api_client):
    order_process = OrderProcessingService(mock_db_service_return_order_type_B, api_client)
    result = order_process.process_orders(1)

    assert api_client.call_api.call_count == 4

    mock_db_service_return_order_type_B.bulk_update_order_status.assert_called_once()

    assert result is True


def test_should_return_true_and_not_write_csv_when_processing_order_type_C(
    mock_db_service_return_order_type_C, api_client
):
    with patch("csv.writer") as mock_csv_writer:
        order_process = OrderProcessingService(mock_db_service_return_order_type_C, api_client)
        result = order_process.process_orders(1)

        mock_csv_writer.assert_not_called()

        mock_db_service_return_order_type_C.bulk_update_order_status.assert_called_once()

        assert result is True


def test_should_return_true_and_not_call_api_when_processing_order_type_C(
    mock_db_service_return_order_type_C, api_client
):
    order_process = OrderProcessingService(mock_db_service_return_order_type_C, api_client)
    result = order_process.process_orders(1)

    api_client.call_api.assert_not_called()

    mock_db_service_return_order_type_C.bulk_update_order_status.assert_called_once()

    assert result is True


def test_should_return_true_and_not_write_csv_when_processing_order_type_other(
    mock_db_service_return_order_type_other, api_client
):
    with patch("csv.writer") as mock_csv_writer:
        order_process = OrderProcessingService(mock_db_service_return_order_type_other, api_client)
        result = order_process.process_orders(1)

        mock_csv_writer.assert_not_called()

        mock_db_service_return_order_type_other.bulk_update_order_status.assert_called_once()

        assert result is True


def test_should_return_true_and_not_call_api_when_processing_order_type_other(
    mock_db_service_return_order_type_other, api_client
):
    order_process = OrderProcessingService(mock_db_service_return_order_type_other, api_client)
    result = order_process.process_orders(1)

    api_client.call_api.assert_not_called()

    mock_db_service_return_order_type_other.bulk_update_order_status.assert_called_once()

    assert result is True


def test_should_return_true_and_priority_is_high_when_processing_order_amount_large_than_200(
    mock_db_service_return_order_large_amount, api_client
):
    order_process = OrderProcessingService(mock_db_service_return_order_large_amount, api_client)
    result = order_process.process_orders(1)

    mock_db_service_return_order_large_amount.bulk_update_order_status.assert_called_once()
    assert (
        mock_db_service_return_order_large_amount.bulk_update_order_status.call_args_list[0][0][0][0].priority == "high"
    )

    assert result is True


def test_should_return_false_when_not_order_processing(mock_db_service_return_empty_order, api_client):
    order_process = OrderProcessingService(mock_db_service_return_empty_order, api_client)
    result = order_process.process_orders(1)

    mock_db_service_return_empty_order.bulk_update_order_status.assert_not_called()

    assert result is False


def test_should_return_false_when_function_get_orders_by_user_error(
    mock_db_service_with_get_order_function_get_error, api_client
):
    order_process = OrderProcessingService(mock_db_service_with_get_order_function_get_error, api_client)
    result = order_process.process_orders(1)

    mock_db_service_with_get_order_function_get_error.bulk_update_order_status.assert_not_called()

    assert result is False


def test_should_return_false_when_function_bulk_update_order_status_error(
    mock_db_service_with_bulk_update_function_get_error, api_client
):
    order_process = OrderProcessingService(mock_db_service_with_bulk_update_function_get_error, api_client)
    result = order_process.process_orders(1)

    mock_db_service_with_bulk_update_function_get_error.bulk_update_order_status.assert_called_once()

    assert result is False
