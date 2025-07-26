import requests
import config
import allure
from data import DataWithGenerate
from methods.login_courier import LoginCourier
from methods.get_order_by_track import GetOrderByTrack
from methods.create_order import  CreateOrder


class AcceptOrder:

    @allure.step('Принятие заказа')
    def accept_order(self, order_id, courier_id):
        acceptance = requests.put(f'{config.BASE_URL}{config.ORDER}/accept/{order_id}?courierId={courier_id}')

        return acceptance.json(), acceptance.status_code

    @allure.step('Принятие заказа без id заказа')
    def accept_order_no_order_id(self, courier_id):
        acceptance = requests.put(f'{config.BASE_URL}{config.ORDER}/accept/{''}?courierId={courier_id}')

        return acceptance.json(), acceptance.status_code

    @allure.step('Принятие заказа без id курьера')
    def accept_order_no_courier_id(self, order_id):
        acceptance = requests.put(f'{config.BASE_URL}{config.ORDER}/accept/{order_id}?courierId={''}')

        return acceptance.json(), acceptance.status_code

    @allure.step('Принятие заказа с неверным id заказа')
    def accept_order_false_order_id(self, courier_id):
        acceptance = requests.put(f'{config.BASE_URL}{config.ORDER}/accept/{'0'}?courierId={courier_id}')

        return acceptance.json(), acceptance.status_code

    @allure.step('Принятие заказа с неверным id курьера')
    def accept_order_false_courier_id(self, order_id):
        acceptance = requests.put(f'{config.BASE_URL}{config.ORDER}/accept/{order_id}?courierId={'100000'}')

        return acceptance.json(), acceptance.status_code


