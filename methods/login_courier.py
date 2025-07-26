import requests
import config
import allure
from methods.registrate_courier import RegistrateCourier


class LoginCourier:

    @allure.step('Логин курьера')
    def login_courier(self, data):
        login = requests.post(f'{config.BASE_URL}{config.REGISTRATE_COURIER}/login', data=data)
        courier_id = login.json().get('id')

        return login.json(), login.status_code, courier_id
