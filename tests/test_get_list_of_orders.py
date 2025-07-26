from methods.get_list_of_orders import GetListOfOrders
import allure


class TestGetListOfOrders:

    @allure.title('Проверка статус кода 200 и наличия списка заказов в ответе при запросе списка заказов')
    def test_get_list_of_orders(self):
        list_order = GetListOfOrders()
        response, status_code = list_order.get_list_of_orders()

        assert 'orders' in response  and status_code == 200