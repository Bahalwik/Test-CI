import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_numbers_square(number: int, expected: int):
    assert number ** 2 == expected


@pytest.mark.parametrize('os', ['macos', 'windows', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0


@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request: SubRequest):
    return request.param


def test_open_browser(browser: str):
    print(f'Running test on browser: {browser}')


@pytest.mark.parametrize('user', ['Sasha', 'Misha'])
class TestOperations:

    @pytest.mark.parametrize('account', ['Credit card', 'Debit card'])
    def test_func_1(self, user: str, account: str):
        ...

    def test_func_2(self, user: str):
        ...



# @pytest.mark.parametrize(
#     'phone_number',
#     ['+799999999', '+7912312321', '+79123123123'],
#     ids=[
#         'User with money',
#         'User with no money',
#         'User with operations',
#     ]
# )

users = {
    '+799999999': 'User with money',
    '+7912312321': 'User with no money',
    '+79123123123': 'User with operations'
}

@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number}: {users[phone_number]}'
)
def test_identifiers(phone_number: str):
    ...

