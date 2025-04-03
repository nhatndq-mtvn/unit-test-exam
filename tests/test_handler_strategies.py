from unittest.mock import MagicMock, patch

from data_test import data_orders
from exam.handler_strategies import (APIOrderHandler, CheckFlagOrderHandler,
                                     CSVOrderHandler, DefaultOrderHandler)


def test_should_order_status_change_to_exported_when_export_csv_success_while_processing_type_A():
    with patch("csv.writer") as mock_csv_write:
        mock_writer_instance = MagicMock()
        mock_csv_write.return_value = mock_writer_instance

        order_process = CSVOrderHandler()
        order = order_process.process(data_orders[1])

        mock_writer_instance.writerow.assert_any_call(["", "", "", "", "Note", "High value order"])

        assert order.status == "exported"


def test_should_order_status_change_to_export_failed_when_export_csv_fail_while_processing_type_A():
    with patch("csv.writer", side_effect=IOError) as _:
        order_process = CSVOrderHandler()
        order = order_process.process(data_orders[0])

        assert order.status == "export_failed"


def test_should_order_status_change_processed_when_api_data_is_50_and_order_amount_less_than_100_while_processing_type_B(
    mock_api_client_return_success_data_50,
):

    order_process = APIOrderHandler(mock_api_client_return_success_data_50)
    order = order_process.process(data_orders[2])

    assert order.status == "processed"


def test_should_order_status_change_pending_when_api_data_is_less_than_50_and_order_flag_is_true_while_processing_type_B(
    mock_api_client_return_success_data_less_than_50,
):

    order_process = APIOrderHandler(mock_api_client_return_success_data_less_than_50)
    order = order_process.process(data_orders[4])

    assert order.status == "pending"


def test_should_order_status_change_error_when_api_data_is_50_and_order_flag_is_false_while_processing_type_B(
    mock_api_client_return_success_data_50,
):

    order_process = APIOrderHandler(mock_api_client_return_success_data_50)
    order = order_process.process(data_orders[3])

    assert order.status == "error"


def test_should_order_status_change_api_error_when_api_return_fail_while_processing_type_B(mock_api_client_return_fail):

    order_process = APIOrderHandler(mock_api_client_return_fail)
    order = order_process.process(data_orders[2])

    assert order.status == "api_error"


def test_should_order_status_change_api_failure_when_api_return_error_while_processing_type_B(
    mock_api_client_return_error
):

    order_process = APIOrderHandler(mock_api_client_return_error)
    order = order_process.process(data_orders[2])

    assert order.status == "api_failure"


def test_should_order_status_change_completed_when_order_flag_is_true_while_processing_type_C():
    CheckFlagOrderHandler

    order_process = CheckFlagOrderHandler()
    order = order_process.process(data_orders[6])

    assert order.status == "completed"


def test_should_order_status_change_in_progress_when_order_flag_is_false_while_processing_type_C():

    order_process = CheckFlagOrderHandler()
    order = order_process.process(data_orders[7])

    assert order.status == "in_progress"


def test_should_order_status_change_unknown_type_when_order_flag_is_false_while_processing_type_other():

    order_process = DefaultOrderHandler()
    order = order_process.process(data_orders[8])

    assert order.status == "unknown_type"
