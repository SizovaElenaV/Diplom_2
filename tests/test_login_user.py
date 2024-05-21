import allure
import requests
from static import LOGIN_URL, PATCH_URL, CREATE_ORDER_URL, GET_ORDER_URL
from utils import generate_random_string, get_random_ingredients

from faker import Faker


class TestLoginUser:

    @allure.title('Проверка успешного логинизирования пользователя')
    def test_success_login_user(self, new_user_with_payload):
        email, password, name = new_user_with_payload
        payload = {'email': email, 'password': password}
        response = requests.post(LOGIN_URL, data=payload)
        assert response.status_code == 200

    @allure.title('Проверка неуспешного логинизирования пользователя')
    def test_error_login_user(self):
        payload = {'email': Faker().email, 'password': generate_random_string(10)}
        response = requests.post(LOGIN_URL, data=payload)
        assert response.status_code == 401

