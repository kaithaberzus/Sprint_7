from generate_data import GenerateData


class DataWithGenerate(GenerateData):

    generate = GenerateData()

    def courier_true_data(self):
        data = {
        "login": self.generate.create_login(),
        "password": self.generate.create_password()
    }
        return data

    def courier_missing_data(self):
        data = {
            "login": self.generate.create_login()
        }
        return data

    def order_data_dif_colors(self):
        return [
            {
                "firstName": self.generate.create_name(),
                "lastName": self.generate.create_surname(),
                "address": self.generate.create_address(),
                "metroStation": 4,
                "phone": self.generate.create_phone_number(),
                "rentTime": 5,
                "deliveryDate": "2025-06-06",
                "comment": self.generate.create_comment(),
                "color": ["BLACK", "GREY"]
            },
            {
                "firstName": self.generate.create_name(),
                "lastName": self.generate.create_surname(),
                "address": self.generate.create_address(),
                "metroStation": 4,
                "phone": self.generate.create_phone_number(),
                "rentTime": 5,
                "deliveryDate": "2025-06-06",
                "comment": self.generate.create_comment()
            },
            {
                "firstName": self.generate.create_name(),
                "lastName": self.generate.create_surname(),
                "address": self.generate.create_address(),
                "metroStation": 4,
                "phone": self.generate.create_phone_number(),
                "rentTime": 5,
                "deliveryDate": "2025-06-06",
                "comment": self.generate.create_comment(),
                "color": [
                    "BLACK"
                ]
            },
            {
                "firstName": self.generate.create_name(),
                "lastName": self.generate.create_surname(),
                "address": self.generate.create_address(),
                "metroStation": 4,
                "phone": self.generate.create_phone_number(),
                "rentTime": 5,
                "deliveryDate": "2025-06-06",
                "comment": self.generate.create_comment(),
                "color": [
                    "GREY"
                ]
            }
        ]

    def single_order_data(self):
        return {
                "firstName": self.generate.create_name(),
                "lastName": self.generate.create_surname(),
                "address": self.generate.create_address(),
                "metroStation": 4,
                "phone": self.generate.create_phone_number(),
                "rentTime": 5,
                "deliveryDate": "2025-06-06",
                "comment": self.generate.create_comment(),
                "color": [
                    "GREY"
                ]
            }

class TextAnswer:

        insufficient_data_for_create_profile = 'Недостаточно данных для создания учетной записи'
        reused_username = 'Этот логин уже используется. Попробуйте другой.'
        data_not_found = 'Учетная запись не найдена'
        true_ok = {'ok': True}
        lose_data = "Недостаточно данных для создания учетной записи"
        no_profile = "Учетная запись не найдена"
        not_found = "Not Found."
        no_courier_with_id = 'Курьера с таким id нет.'
        insufficient_data_for_search = 'Недостаточно данных для поиска'
        no_such_order = 'Заказ не найден'
        no_such_courier = 'Курьера с таким id не существует'
        order_not_exist = 'Заказа с таким id не существует'