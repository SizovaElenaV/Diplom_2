import allure
import requests
from static import LOGIN_URL, PATCH_URL, CREATE_ORDER_URL, GET_ORDER_URL
from utils import generate_random_string, get_random_ingredients


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа с токеном и ингредиентами')
    def test_success_order_with_token_and_ingredients(self, new_user_with_tokens):
        access_token, refresh_token = new_user_with_tokens
        ingredient_ids = get_random_ingredients()
        payload = {'ingredients': ingredient_ids}
        response = requests.post(CREATE_ORDER_URL, payload,
                                 headers={'authorization': access_token})
        assert response.status_code == 200

    @allure.title('Проверка неуспешного создания заказа с токеном и без ингредиентов')
    def test_error_order_with_token_and_no_ingredients(self, new_user_with_tokens):
        access_token, refresh_token = new_user_with_tokens
        response = requests.post(CREATE_ORDER_URL,
                                 headers={'authorization': access_token})
        assert response.status_code == 400

    @allure.title('Проверка неуспешного создания заказа без токена и с ингредиентами')
    def test_error_order_with_no_token_and_ingredients(self):
        response = requests.post(CREATE_ORDER_URL)
        assert response.status_code == 400
