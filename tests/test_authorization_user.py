import requests
from static import LOGIN_URL, PATCH_URL, CREATE_ORDER_URL, GET_ORDER_URL
from utils import generate_random_string, get_random_ingredients
import allure
from faker import Faker


class TestAuthorizationUser:

    @allure.title('Проверка успешного обновления пользователя')
    def test_success_patch_user(self, new_user_with_tokens):
        access_token, refresh_token = new_user_with_tokens
        name = generate_random_string(10)
        email = Faker().email
        response = requests.patch(PATCH_URL, data={'name': name, 'email': email},
                                  headers={'authorization': access_token})
        assert response.status_code == 200

    @allure.title('Проверка неуспешного обновления пользователя')
    def test_error_patch_user(self):
        name = generate_random_string(10)
        email = Faker().email
        response = requests.patch(PATCH_URL, data={'name': name, 'email': email})
        assert response.status_code == 401
