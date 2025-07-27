import pytest
import requests
import config
from methods.registrate_courier import RegistrateCourier
from data import DataWithGenerate
from methods.login_courier import LoginCourier
from methods.create_order import CreateOrder
from methods.cancel_order import CancelOrder
from methods.complete_order import CompleteOrder
from methods.get_order_by_track import GetOrderByTrack
from methods.accept_order import AcceptOrder
from methods.delete_courier import DeleteCourier


@pytest.fixture()
def delete_courier():
    data_with_generate = DataWithGenerate()
    data = data_with_generate.courier_true_data()
    yield data
    courier_id = requests.post(f'{config.BASE_URL}{config.REGISTRATE_COURIER}/login', data=data).json().get('id')
    requests.delete(f'{config.BASE_URL}{config.REGISTRATE_COURIER}/{courier_id}')

@pytest.fixture()
def cancel_order_for_get_obt():
    create_order = CreateOrder()
    data = DataWithGenerate()
    cancel_order = CancelOrder()
    response, status_code, order_track = create_order.create_an_order(data.single_order_data())
    yield order_track, response, status_code
    cancel_order.cancel_order(order_track)

@pytest.fixture()
def complete_order():
    complete_order = CompleteOrder()
    get_order_by_track = GetOrderByTrack()
    registrate_courier = RegistrateCourier()
    login = LoginCourier()
    create_order = CreateOrder()
    delete_courier = DeleteCourier()

    data_with_generate = DataWithGenerate()
    data_for_order = data_with_generate.single_order_data()
    data_for_courier = data_with_generate.courier_true_data()

    registrate_courier.registrate_courier(data_for_courier)
    create_order = create_order.create_an_order(data_for_order)
    get_order_by_track = get_order_by_track.get_order_by_track(create_order[2])
    login = login.login_courier(data_for_courier)

    yield get_order_by_track[2], login[2]
    complete_order.complete_order(get_order_by_track[2])
    delete_courier.delete_courier_with_id(login[2])
