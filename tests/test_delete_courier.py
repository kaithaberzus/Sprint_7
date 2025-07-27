from methods.delete_courier import DeleteCourier
from data import *
from methods.login_courier import LoginCourier
from methods.registrate_courier import RegistrateCourier
import allure


class TestDeleteCourier:

    @allure.title('Проверка удаления курьера с валидными данными')
    def test_delete_courier_true(self):
        delete_courier = DeleteCourier()
        registrate_courier = RegistrateCourier()
        login = LoginCourier()

        data_with_generate = DataWithGenerate()
        data = data_with_generate.courier_true_data()

        registrate_courier.registrate_courier(data)
        login_courier = login.login_courier(data)
        response, status_code = delete_courier.delete_courier_with_id(login_courier[2])

        assert status_code == 200 and response == TextAnswer.true_ok

    @allure.title('Проверка удаления курьера с отсутствующим id курьера')
    def test_delete_courier_missing_id(self):
        delete_courier = DeleteCourier()
        response, status_code = delete_courier.delete_courier_without_id()

        assert response["message"] == TextAnswer.not_found and status_code == 404

    @allure.title('Проверка удаления курьера с не существующим id курьера')
    def test_delete_courier_false_id(self):
        delete_courier = DeleteCourier()
        response, status_code = delete_courier.delete_courier_with_not_stated_id()

        assert response["message"] == TextAnswer.no_courier_with_id and status_code == 404