import requests
import config
import allure


class CancelOrder:

    @allure.step('Отмена заказа')
    def cancel_order(self, order_track):
        cancel = requests.put(f'{config.BASE_URL}{config.ORDER}/cancel?track={order_track}')

        return cancel