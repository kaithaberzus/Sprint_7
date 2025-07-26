import requests
import config
import allure
from methods.login_courier import LoginCourier
from methods.registrate_courier import RegistrateCourier


class DeleteCourier:

    @allure.step('Удаление курьера')
    def delete_courier_with_id(self, courier_id):
        delete = requests.delete(f'{config.BASE_URL}{config.REGISTRATE_COURIER}/{courier_id}')

        return delete.json(), delete.status_code

    @allure.step('Удаление курьера без id')
    def delete_courier_without_id(self):
        delete = requests.delete(f'{config.BASE_URL}{config.REGISTRATE_COURIER}')

        return delete.json(), delete.status_code

    @allure.step('Удаление курьера с несуществующим id')
    def delete_courier_with_not_stated_id(self):
        delete = requests.delete(f'{config.BASE_URL}{config.REGISTRATE_COURIER}/1000000')

        return delete.json(), delete.status_code
