from methods.accept_order import AcceptOrder
from data import *
import allure
from methods.login_courier import LoginCourier
from methods.registrate_courier import RegistrateCourier
from data import DataWithGenerate
from methods.create_order import CreateOrder
from methods.get_order_by_track import GetOrderByTrack


class TestAcceptOrder:

    @allure.title('Проверка статуса заказа и теста ответа при принятии заказа с валидными id курьера и id заказа')
    def test_accept_order(self, complete_order):
        accept_order = AcceptOrder()
        response, status_code = accept_order.accept_order(complete_order[0], complete_order[1])
        assert response == TextAnswer.true_ok and status_code == 200

    @allure.title('Проверка статуса заказа и теста ответа при принятии заказа с отсутствующим id курьера и валидным id заказа')
    def test_accept_order_no_courier_id(self, complete_order):
        accept_order = AcceptOrder()

        response, status_code = accept_order.accept_order_no_courier_id(complete_order[0])

        assert response['message'] == TextAnswer.insufficient_data_for_search and status_code == 400

    @allure.title('Проверка статуса заказа и теста ответа при принятии заказа с валидными id курьера и отсутствующим id заказа')
    def test_accept_order_no_order_id(self, complete_order):
        accept_order = AcceptOrder()

        response, status_code = accept_order.accept_order_no_order_id(complete_order[1])

        assert response['message'] == TextAnswer.not_found and status_code == 404

    @allure.title('Проверка статуса заказа и теста ответа при принятии заказа с валидными id курьера и не существующим id заказа')
    def test_accept_order_false_order_id(self):
        accept_order = AcceptOrder()
        registrate_courier = RegistrateCourier()
        login = LoginCourier()

        data_with_generate = DataWithGenerate()
        data = data_with_generate.courier_true_data()

        registrate_courier.registrate_courier(data)
        login_courier = login.login_courier(data)
        response, status_code = accept_order.accept_order_no_order_id(login_courier[2])

        assert response['message'] == TextAnswer.not_found and status_code == 404

    @allure.title('Проверка статуса заказа и теста ответа при принятии заказа с не существующим id курьера и валидным id заказа')
    def test_accept_order_false_courier_id(self):
        accept_order = AcceptOrder()
        create_order = CreateOrder()
        get_order_by_track = GetOrderByTrack()

        data_with_generate = DataWithGenerate()
        data = data_with_generate.single_order_data()

        track = create_order.create_an_order(data)
        order_id = get_order_by_track.get_order_by_track(track[2])
        response, status_code = accept_order.accept_order_no_courier_id(order_id[2])

        assert response['message'] == TextAnswer.insufficient_data_for_search and status_code == 400