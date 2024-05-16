import requests
import random
import string

from faker import Faker

from static import REGISTER_URL, INGREDIENTS_URL


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def get_user_register_payload():
    email = Faker().email()
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload


def register_new_user_and_return_payload(payload):

    login_pass = []

    response = requests.post(REGISTER_URL, data=payload)

    if response.status_code == 200:
        login_pass.append(payload['email'])
        login_pass.append(payload['password'])
        login_pass.append(payload['name'])

    return login_pass


def register_new_user_and_return_tokens(payload):

    login_pass = []

    response = requests.post(REGISTER_URL, data=payload)
    data = response.json()
    if response.status_code == 200:
        login_pass.append(data['accessToken'])
        login_pass.append(data['refreshToken'])

    return login_pass


def get_random_ingredients():
    payload = get_user_register_payload()
    access_token, refresh_token = register_new_user_and_return_tokens(payload)
    response = requests.get(INGREDIENTS_URL, headers={'authorization': access_token})
    response_data = response.json()['data']
    data = []

    if response.status_code == 200:
        data.append(random.choice(response_data)['_id'])
        data.append(random.choice(response_data)['_id'])
        data.append(random.choice(response_data)['_id'])

    return data
