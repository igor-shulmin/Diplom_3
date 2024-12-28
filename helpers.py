import string
import random
import requests
from data import Url


class Generate:

    @staticmethod
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))

        return random_string

    @staticmethod
    def generate_mail(length=10):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))

        return random_string + '@mail.com'


class User:

    def __init__(self):
        self.response = None
        self.email = None
        self.password = None

    def register_new_user_and_return_login_password(self):
        email = Generate.generate_mail()
        password = Generate.generate_random_string()
        name = Generate.generate_random_string()

        payload = {
            'email': email,
            'password': password,
            'name': name
        }

        self.response = requests.post(f'{Url.BASE_PAGE}/{Url.API_REGISTER}', data=payload)

        if self.response.status_code == 200:
            self.email = email
            self.password = password

    def login_user(self):
        payload = {
            'email': self.email,
            'password': self.password
        }
        self.response = requests.post(f'{Url.BASE_PAGE}/{Url.API_LOGIN}', data=payload)

        return self.response.json()['accessToken']

    def delete_user(self):
        headers = {'Authorization': self.login_user()}
        self.response = requests.delete(f'{Url.BASE_PAGE}/{Url.API_USER}', headers=headers)
