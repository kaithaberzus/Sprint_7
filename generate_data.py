from faker import Faker
from datetime import date

class GenerateData:

    fake_en = Faker()
    fake_ru = Faker(locale='ru_RU')

    def create_name(self):
        return self.fake_en.name()

    def create_password(self):
        return self.fake_en.password()

    def create_login(self):
        return self.fake_en.word()

    def create_surname(self):
        return self.fake_en.last_name()

    def create_address(self):
        return self.fake_en.address()

    def create_phone_number(self):
        return self.fake_ru.phone_number()

    def create_comment(self):
        return self.fake_en.text()

    def create_date(self):
        return date.today()
