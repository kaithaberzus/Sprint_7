from methods.registrate_courier import RegistrateCourier
from data import *
import allure


class TestRegistrateCourier:

    @allure.title('Проверка статус кода и текста ответа при создании курьера с валидными данными')
    def test_registration_true_status_code(self, delete_courier_for_registrate_tests):
        registrate_courier = RegistrateCourier()
        response, status_code = registrate_courier.registrate_courier(delete_courier_for_registrate_tests)
        assert status_code == 201 and response == TextAnswer.true_ok

    @allure.title('Проверка текста ответа при регистрации курьера с отсутствующим паролем')
    def test_registrate_courier_error_text_message(self):
        register = RegistrateCourier()
        data_with_generate = DataWithGenerate()
        response, status_code = register.registrate_courier(data_with_generate.courier_missing_data())

        assert response["message"] == TextAnswer.insufficient_data_for_create_profile and status_code == 400

    @allure.title('Регистрация курьера с паролем и логином, которые уже использовались')
    def test_text_message_after_register_two_same_couriers(self, delete_courier_for_registrate_tests):
        registrate_courier = RegistrateCourier()
        registrate_courier.registrate_courier(delete_courier_for_registrate_tests)
        response, status_code = registrate_courier.registrate_courier(delete_courier_for_registrate_tests)

        assert response["message"] == TextAnswer.reused_username and status_code == 409