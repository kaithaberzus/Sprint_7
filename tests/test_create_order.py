from data import DataWithGenerate
from methods.create_order import CreateOrder
from methods.cancel_order import CancelOrder
import pytest
import allure


class TestCreateOrder:

    @allure.title('Проверка статус кода и наличия трек номера в ответе при создании заказа с разными цветами самоката')
    @pytest.mark.parametrize("data", DataWithGenerate().order_data_dif_colors())
    def test_put_diff_colors_of_scooter_in_body_response_true(self, data):
        create_order = CreateOrder()
        cancel_order = CancelOrder()
        status_code, response, order_track = create_order.create_an_order(data)

        assert status_code == 201 and 'track' in response

        cancel_order.cancel_order(order_track)