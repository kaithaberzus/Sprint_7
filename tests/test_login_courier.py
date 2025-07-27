from data import *
import allure
from methods.login_courier import LoginCourier
from methods.registrate_courier import RegistrateCourier


class TestLoginCourier:

    @allure.title('Проверка статус кода при логине курьера с корректными данными')
    def test_login_courier_status_code_true(self, delete_courier):
        registrate_courier = RegistrateCourier()
        login_courier = LoginCourier()
        registrate_courier.registrate_courier(delete_courier)
        response, status_code, courier_id = login_courier.login_courier(delete_courier)
        assert status_code == 200

    @allure.title('Проверка текста ответа при логине курьера с несуществующим паролем и логином')
    def test_login_courier_text_message_incorrect_password(self):
        data_with_generate = DataWithGenerate()
        login = LoginCourier()
        registrate_courier = RegistrateCourier()
        data = data_with_generate.courier_true_data()
        registrate_courier.registrate_courier(data)
        response, status_code, courier_id = login.login_courier(data)

        assert response["message"] == TextAnswer.no_profile and status_code == 404

    @allure.title('Проверка текста ответа при логине курьера с отсутствующим паролем')
    def test_login_courier_text_message_no_password(self):
        data_with_generate = DataWithGenerate()
        login = LoginCourier()
        registrate_courier = RegistrateCourier()
        data = data_with_generate.courier_missing_data()
        registrate_courier.registrate_courier(data)
        response, status_code, courier_id = login.login_courier(data)

        assert response["message"] == TextAnswer.lose_data and status_code == 400

    @allure.title('Проверка наличия id в тексте ответа при логине курьера')
    def test_after_login_courier_is_id_in_response(self, delete_courier):
        login_courier = LoginCourier()
        registrate_courier = RegistrateCourier()
        registrate_courier.registrate_courier(delete_courier)
        response, status_code, courier_id = login_courier.login_courier(delete_courier)
        assert "id" in response