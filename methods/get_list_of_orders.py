import requests
import config
import allure


class GetListOfOrders:

    @allure.step('Получение списка заказов')
    def get_list_of_orders(self):
        list_of_orders = requests.get(f'{config.BASE_URL}{config.ORDER}')

        return list_of_orders.json(), list_of_orders.status_code