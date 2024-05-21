import allure
import pytest
import requests

from utils import generate_random_string, get_user_register_payload, register_new_user_and_return_payload
from static import REGISTER_URL


class TestCreateUser:

    @allure.title('Проверка очень успешного создания уникального пользователя')
    def test_success_create_unique_user(self):
        payload = get_user_register_payload()

        response = requests.post(REGISTER_URL, data=payload)
        assert response.status_code == 200

    @allure.title('Проверка неуспешного создания существующего пользователя')
    def test_error_create_existing_user(self):
        payload = get_user_register_payload()
        email, password, name = register_new_user_and_return_payload(payload)

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(REGISTER_URL, data=payload)
        assert response.status_code == 403

    @allure.title('Проверка неуспешного создания пользователя с незаполненным полем')
    @pytest.mark.parametrize('field_to_delete',
                             ['email', 'password', 'name'])
    def test_error_create_user_unfilled_field(self, field_to_delete):
        payload = get_user_register_payload()

        del payload[field_to_delete]

        response = requests.post(REGISTER_URL, data=payload)
        assert response.status_code == 403
