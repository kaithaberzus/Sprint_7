import requests
import config
import allure


class GetOrderByTrack:

    @allure.step('Получение заказа по трек номеру')
    def get_order_by_track(self, order_track):
        get_order = requests.get(f'{config.BASE_URL}{config.ORDER}/track?t={order_track}')

        if get_order.status_code == 200:
            order_id = get_order.json()['order']['id']

            return get_order.json(), get_order.status_code, order_id

        else: return get_order.json(), get_order.status_code
