import json

import requests


class RegRequest:
    def __init__(self):
        self.base_url = "https://reqres.in/api/"

    def get_api_resource(self, headers):

        res = requests.get(self.base_url + "{resource}", headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_api_users(self, headers):

        res = requests.get(self.base_url + "users", headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_api_users_id(self, user_id):

        res = requests.get(self.base_url + "users/", params=user_id)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_api_resource_id(self, resource_id):

        res = requests.get(self.base_url + "{resource}/", params=resource_id)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_api_login(self, body):
        res = requests.post(self.base_url + "login", json=body)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_api_register(self, body):
        res = requests.post(self.base_url + "register", json=body)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_api_logout(self):
        res = requests.post(self.base_url + "logout")
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def put_api_users_id(self, user_id, body):

        res = requests.put(self.base_url + "users/", params=user_id, json=body)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def put_api_resource_id(self, resource_id):

        res = requests.put(self.base_url + "resource/", params=resource_id)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def patch_api_users_id(self, user_id, body):

        res = requests.patch(self.base_url + "users/", params=user_id, json=body)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def patch_api_resource_id(self, resource_id):

        res = requests.patch(self.base_url + "resource/", params=resource_id)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_api_users_id(self, user_id):
        user_id = {"id": user_id}
        res = requests.delete(self.base_url + "users/", params=user_id)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def delete_api_resource_id(self, resource_id):
        resource_id = {"id": resource_id}
        res = requests.delete(self.base_url + "resource/", params=resource_id)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
