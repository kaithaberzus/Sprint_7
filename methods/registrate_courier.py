import requests
import config
import allure


class RegistrateCourier:

    @allure.step('Регистрация курьера')
    def registrate_courier(self, data):
        registration = requests.post(f'{config.BASE_URL}{config.REGISTRATE_COURIER}', data=data)

        return registration.json(), registration.status_code
