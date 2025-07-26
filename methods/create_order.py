import requests
import config
import allure


class CreateOrder:

    @allure.step('Создание заказа')
    def create_an_order(self, data):
        order = requests.post(f'{config.BASE_URL}{config.ORDER}', json=data)
        order_track = order.json().get('track')

        return order.status_code, order.json(), order_track