import requests
import config
import allure


class CompleteOrder:

    @allure.step('Завершение заказа')
    def complete_order(self, order_id):
        complete_order = requests.put(f'{config.BASE_URL}{config.ORDER}/finish/{order_id}')

        return complete_order




