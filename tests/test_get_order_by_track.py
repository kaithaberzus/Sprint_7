import allure
from methods.get_order_by_track import GetOrderByTrack
from data import *


class TestGetOrderByTrack:

    @allure.title('Проверка получение заказа по трек номеру с валидным трек номером')
    def test_get_order_by_true_track(self, cancel_order_for_get_obt):
        get_order_by_track = GetOrderByTrack()
        response, status_code, order_id = get_order_by_track.get_order_by_track(cancel_order_for_get_obt[0])

        assert status_code == 200 and response['order']['id']

    @allure.title('Проверка получение заказа без трек номера')
    def test_get_order_by_track_no_track(self, cancel_order_for_get_obt):
        get_order_by_track = GetOrderByTrack()
        response, status_code = get_order_by_track.get_order_by_track('')

        assert response['message'] == TextAnswer.insufficient_data_for_search and status_code == 400

    @allure.title('Проверка получение заказа с не существующим трек номером')
    def test_get_order_by_track_not_stated_id(self):
        get_order_by_track = GetOrderByTrack()
        response, status_code = get_order_by_track.get_order_by_track('0')

        assert status_code == 404 and response['message'] == TextAnswer.no_such_order



