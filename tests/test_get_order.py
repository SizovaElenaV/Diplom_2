import requests
from static import LOGIN_URL, PATCH_URL, CREATE_ORDER_URL, GET_ORDER_URL
import allure


class TestGetOrder:

    @allure.title('Проверка успешного получения заказа')
    def test_success_get_order_with_token(self, new_user_with_tokens):
        access_token, refresh_token = new_user_with_tokens
        response = requests.get(GET_ORDER_URL, headers={'authorization': access_token})
        assert response.status_code == 200

    @allure.title('Проверка неуспешного получения заказа')
    def test_error_get_order_without_token(self):
        response = requests.get(GET_ORDER_URL)
        assert response.status_code == 401
