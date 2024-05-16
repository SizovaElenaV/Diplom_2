import pytest

from utils import register_new_user_and_return_payload, register_new_user_and_return_tokens, get_user_register_payload


@pytest.fixture
def new_user_with_payload():
    payload = get_user_register_payload()
    return register_new_user_and_return_payload(payload)


@pytest.fixture
def new_user_with_tokens():
    payload = get_user_register_payload()
    return register_new_user_and_return_tokens(payload)
